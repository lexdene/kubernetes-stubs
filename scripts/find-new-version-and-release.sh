set -e

for version in $(uv run --frozen python scripts/pypi_version.py get-unpublished); do
    bash scripts/release.sh $version
done
