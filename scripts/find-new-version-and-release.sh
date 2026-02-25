set -e

for version in $(python scripts/pypi_version.py get-unpublished); do
    bash scripts/release.sh $version
done
