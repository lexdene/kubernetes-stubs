from typing import (
    TypeVar, ParamSpec, TypedDict, Generic, Literal, Union, Protocol,
)
from collections.abc import Callable, Iterable

_T = TypeVar("T")
_P = ParamSpec("P")


class _ObjectEvent(TypedDict, Generic[_T]):
    type: Literal["ADDED", "MODIFIED", "DELETED"]
    object: _T


class _BookmarkEvent(TypedDict):
    type: Literal["BOOKMARK"]


_Event = Union[_ObjectEvent[_T], _BookmarkEvent, None]


class _ListResponse(Protocol[_T]):
    items: list[_T]


class Watch:
    def stream(
        self,
        func: Callable[_P, _ListResponse[_T]],
        *argv: _P.args,
        **kwargs: _P.kwargs
    ) -> Iterable[_Event[_T]]:
        ...
