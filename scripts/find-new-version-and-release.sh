for version in $(python scripts/get_unpublished_version.py); do
    bash scripts/release.sh $version
done
