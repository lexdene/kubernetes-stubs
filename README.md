# kubernetes-stubs-elephant-fork

fork of [kubernetes-stubs][1]

## why fork?

[kubernetes-stubs][1] has not provided stubs for [kubernetes][2] >= 23.0 yet (2023-05-30).

`kubernetes-stubs-elephant-fork` provides stubs for all releases after 7.0 of [kubernetes][2],
even includes any release in the future automatically.

I run a crontab by github actions which looks for new releases of [kubernetes][2]
and build stubs for it.

[1]: https://pypi.org/project/kubernetes-stubs
[2]: https://pypi.org/project/kubernetes
