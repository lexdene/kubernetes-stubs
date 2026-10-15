# kubernetes-stubs-elephant-fork

fork of [kubernetes-stubs][1]

## deprecated

This library is deprecated.

The official Kubernetes Python client has supported typing since version 37.0.0,
making `kubernetes-stubs-elephant-fork` obsolete.

Thank you to everyone who installed and used `kubernetes-stubs-elephant-fork` over the past few years.
Working on this has been such a wonderful time for me,
but now it's time to say goodbye.

Wishing you all the best and good luck in the days ahead!

## why fork?

[kubernetes-stubs][1] has not provided stubs for [kubernetes][2] >= 23.0 yet (2023-05-30).

`kubernetes-stubs-elephant-fork` provides stubs for all releases after 7.0 of [kubernetes][2],
even includes any release in the future automatically.

I run a crontab by github actions which looks for new releases of [kubernetes][2]
and build stubs for it.

[1]: https://pypi.org/project/kubernetes-stubs
[2]: https://pypi.org/project/kubernetes
