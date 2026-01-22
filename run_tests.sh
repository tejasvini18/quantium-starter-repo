#!/usr/bin/env bash
set -e

echo "Activating virtual environment..."

# Activate virtual environment
source venv/bin/activate

echo "Running test suite with pytest..."

# Run tests
if pytest; then
    echo "✅ All tests passed."
    exit 0
else
    echo "❌ Tests failed."
    exit 1
fi
