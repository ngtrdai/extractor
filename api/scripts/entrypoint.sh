set -euxo pipefail

# Run server
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload