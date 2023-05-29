set -e

VERSION=$1
echo 'version:' $VERSION

# clean up
rm -rf kubernetes-client-python \
    kubernetes-stubs \
    kubernetes_ext \
    dist

# install
pip install --upgrade pip wheel setuptools
pip install -r scripts/requirements.txt

mkdir -p kubernetes-client-python/scripts
pushd kubernetes-client-python/scripts
wget https://github.com/kubernetes-client/python/raw/v${VERSION}/scripts/swagger.json
popd

poetry run python codegen

./bin/fmt

# Is there any better way to update version from command line?
toml set --toml-path pyproject.toml tool.poetry.version "${VERSION}.dev0"

poetry build
