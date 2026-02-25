set -e

KUBERNETES_VERSION=$1
SUFFIX=$2

if [ -z "${KUBERNETES_VERSION}" ];
then
  KUBERNETES_VERSION=$(python scripts/pypi_version.py get-latest)
fi

bash scripts/release.sh "$KUBERNETES_VERSION" "$SUFFIX"
