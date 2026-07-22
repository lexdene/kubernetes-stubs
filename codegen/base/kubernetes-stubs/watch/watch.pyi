import typing

_ReturnMode = typing.TypeVar("_ReturnMode")
_P = typing.ParamSpec("_P")
_T = typing.TypeVar("_T")
_ListItemT_co = typing.TypeVar("_ListItemT_co", covariant=True)

# Watch deserializes ordinary events to the inferred model, but leaves bookmark
# objects untouched:
# https://github.com/kubernetes-client/python/blob/01b1642b835f5195a8f81a788908f2cb3991c671/kubernetes/base/watch/watch.py#L119-L149
class _ObjectEvent(typing.TypedDict, typing.Generic[_T]):
    type: typing.Literal["ADDED", "MODIFIED", "DELETED"]
    raw_object: object
    object: _T

class _BookmarkEvent(typing.TypedDict):
    type: typing.Literal["BOOKMARK"]
    raw_object: object
    object: object

_DecodedWatchItem = typing.Union[_ObjectEvent[_T], _BookmarkEvent, None]

# Without an explicit return type, Watch drops `List` from the API return type;
# generated list stubs expose the same relationship through `items`:
# https://github.com/kubernetes-client/python/blob/01b1642b835f5195a8f81a788908f2cb3991c671/kubernetes/base/watch/watch.py#L105-L111
class _WatchList(typing.Protocol[_ListItemT_co]):
    @property
    def items(self) -> typing.Sequence[_ListItemT_co]: ...

# ApiClient accepts either a class literal or a class-name string as an
# explicit return type:
# https://github.com/kubernetes-client/python/blob/01b1642b835f5195a8f81a788908f2cb3991c671/kubernetes/client/api_client.py#L265-L285
class _InferReturn: ...
class _FixedReturn(typing.Generic[_T]): ...

class Watch(typing.Generic[_ReturnMode]):
    resource_version: typing.Optional[str]
    @typing.overload
    def __init__(self: Watch[_InferReturn], return_type: None = ...) -> None: ...
    @typing.overload
    def __init__(self: Watch[_FixedReturn[_T]], return_type: type[_T]) -> None: ...
    # Arbitrary class-name strings cannot be resolved statically.
    @typing.overload
    def __init__(self: Watch[_FixedReturn[object]], return_type: str) -> None: ...
    def stop(self) -> None: ...
    # Watch() infers the event object type from the API method's list type.
    # deserialize is consumed by Watch rather than forwarded to func. False
    # bypasses model deserialization, so an explicit value has a broad result:
    # https://github.com/kubernetes-client/python/blob/01b1642b835f5195a8f81a788908f2cb3991c671/kubernetes/base/watch/watch.py#L185-L210
    # PEP 612 cannot express a keyword consumed before forwarding a ParamSpec,
    # so the explicit overload intentionally overlaps ordinary calls.
    @typing.overload
    def stream(  # type: ignore[overload-overlap]
        self: Watch[_InferReturn],
        func: typing.Callable[..., object],
        *args: object,
        deserialize: bool,
        **kwargs: object,
    ) -> typing.Iterator[object]: ...
    @typing.overload
    def stream(
        self: Watch[_InferReturn],
        func: typing.Callable[_P, _WatchList[_T]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> typing.Iterator[_DecodedWatchItem[_T]]: ...
    @typing.overload
    def stream(
        self: Watch[_InferReturn],
        func: typing.Callable[_P, object],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> typing.Iterator[object]: ...
    # Watch(return_type) uses that type instead of the API method's item type.
    @typing.overload
    def stream(  # type: ignore[overload-overlap]
        self: Watch[_FixedReturn[_T]],
        func: typing.Callable[..., object],
        *args: object,
        deserialize: bool,
        **kwargs: object,
    ) -> typing.Iterator[object]: ...
    @typing.overload
    def stream(
        self: Watch[_FixedReturn[_T]],
        func: typing.Callable[_P, _WatchList[object]],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> typing.Iterator[_DecodedWatchItem[_T]]: ...
    @typing.overload
    def stream(
        self: Watch[_FixedReturn[_T]],
        func: typing.Callable[_P, object],
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> typing.Iterator[object]: ...
