import json
from argparse import ArgumentParser
from packaging.version import Version
from urllib.request import urlopen


def _get_versions(url):
    with urlopen(url, timeout=10) as resp:
        content = resp.read()

    data = json.loads(content)
    return sorted([
        Version(key)
        for key in data['releases'].keys()
    ])


def get_stubbed_versions():
    url = 'https://pypi.org/pypi/kubernetes-stubs-elephant-fork/json'
    versions = _get_versions(url)

    return set([
        Version(v.base_version)
        for v in versions
    ])


def get_upstream_versions():
    url = 'https://pypi.org/pypi/kubernetes/json'
    return _get_versions(url)


def get_unpublished_version():
    limit = 1
    count = 0

    stubbed_versions = get_stubbed_versions()

    for version in get_upstream_versions():
        if version.is_prerelease:
            continue

        if version < Version('7'):
            continue

        if version in stubbed_versions:
            continue

        print(version)

        count += 1
        if count >= limit:
            break


def get_latest_version():
    rs = get_upstream_versions()
    for version in reversed(rs):
        if version.is_prerelease:
            continue

        return version


def parse_args():
    parser = ArgumentParser()

    actions = parser.add_subparsers(dest='action')
    actions.add_parser('get-unpublished')
    actions.add_parser('get-latest')

    return parser.parse_args()


def main():
    args = parse_args()

    if args.action == 'get-latest':
        print(get_latest_version())
        return
    elif args.action == 'get-unpublished':
        return get_unpublished_version()


if __name__ == '__main__':
    main()
