import os
from pathlib import Path
import subprocess
import sys


# Render Free filesystem: use writable temporary storage
DATA_DIR = Path(
    os.getenv("MLFLOW_DATA_DIR", "/tmp/mlflow")
)

DATA_DIR.mkdir(parents=True, exist_ok=True)

DB_PATH = DATA_DIR / "mlflow.db"
ARTIFACT_DIR = DATA_DIR / "artifacts"

ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)


# Render provides PORT automatically
HOST = "0.0.0.0"
PORT = os.getenv("PORT", "10000")


# SQLite backend
BACKEND_STORE_URI = f"sqlite:///{DB_PATH}"


# Start MLflow server
cmd = [
    sys.executable,
    "-m",
    "mlflow",
    "server",
    "--host",
    HOST,
    "--port",
    PORT,
    "--workers",
    "1",
    "--backend-store-uri",
    BACKEND_STORE_URI,
    "--artifacts-destination",
    f"file://{ARTIFACT_DIR}",
]


print("Starting PCS Remote MLflow Server...")
print(f"Backend: {BACKEND_STORE_URI}")
print(f"Artifacts: {ARTIFACT_DIR}")
print(f"Host: {HOST}")
print(f"Port: {PORT}")
print("Workers: 1")


subprocess.run(cmd, check=True)