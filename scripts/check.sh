#!/usr/bin/env sh

set -eu

uv sync --frozen
ORIGINAL_VERSION=$(uv run --no-sync toml get --toml-path pyproject.toml tool.poetry.version)
trap 'uv run --no-sync toml set --toml-path pyproject.toml tool.poetry.version "$ORIGINAL_VERSION"' EXIT

bash scripts/manually-release.sh 36.0.2
uv pip install --python .venv/bin/python \
    dist/kubernetes_stubs_elephant_fork-36.0.2-*.whl
rm -rf kubernetes-client-python kubernetes-stubs kubernetes_ext

uv run --no-sync ty check
uv run --no-sync mypy
uv run --no-sync pyright
