set -euxo pipefail

python -m scripts.migrations create

# Run server
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload