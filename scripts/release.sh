set -e

VERSION=$1
SUFFIX=$2

if [ -z "${SUFFIX}" ];
then
  PUBLISH_VERSION=$VERSION
else
  PUBLISH_VERSION="${VERSION}.${SUFFIX}"
fi

echo 'version:' $VERSION
echo 'publish version:' $PUBLISH_VERSION

# clean up
rm -rf kubernetes-client-python \
    kubernetes-stubs \
    kubernetes_ext

mkdir -p kubernetes-client-python/scripts
curl --fail --location \
    --output kubernetes-client-python/scripts/swagger.json \
    "https://github.com/kubernetes-client/python/raw/v${VERSION}/scripts/swagger.json"

uv run --frozen python codegen

uv run --frozen black codegen kubernetes-stubs kubernetes_ext
uv run --frozen isort codegen kubernetes-stubs kubernetes_ext

# Is there any better way to update version from command line?
uv run --frozen toml set --toml-path pyproject.toml tool.poetry.version "${PUBLISH_VERSION}"

uv build
