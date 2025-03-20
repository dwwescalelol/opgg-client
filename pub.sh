#!/bin/bash

set -e  # Stop on any error

echo "🚀 Uninstalling old version..."
pip uninstall -y opgg-client || true

echo "🧹 Cleaning old build artifacts..."
rm -rf dist build *.egg-info

echo "📦 Building new package..."
python -m build

# echo "📦 Installing package..."
# pip install dist/opgg_client-0.1.2-py3-none-any.whl

# echo "📋 Checking package contents..."
# python -c "import opgg.clients; print(opgg.clients.__file__)"

echo "📋 Checking package contents..."
twine check dist/*

echo "📤 Uploading to PyPI..."
twine upload dist/*

echo "✅ Published successfully!"
