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
pushd kubernetes-client-python/scripts
wget https://github.com/kubernetes-client/python/raw/v${VERSION}/scripts/swagger.json
popd

poetry run python codegen

poetry run black codegen kubernetes-stubs kubernetes_ext
poetry run isort codegen kubernetes-stubs kubernetes_ext

# Is there any better way to update version from command line?
toml set --toml-path pyproject.toml tool.poetry.version "${PUBLISH_VERSION}"

poetry build
