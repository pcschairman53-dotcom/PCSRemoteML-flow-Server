import os
from pathlib import Path
import subprocess
import sys


DATA_DIR = Path(
    os.getenv("MLFLOW_DATA_DIR", "/tmp/mlflow")
)

DATA_DIR.mkdir(parents=True, exist_ok=True)

DB_PATH = DATA_DIR / "mlflow.db"
ARTIFACT_DIR = DATA_DIR / "artifacts"

ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)

HOST = "0.0.0.0"
PORT = os.getenv("PORT", "10000")

BACKEND_STORE_URI = f"sqlite:///{DB_PATH}"

cmd = [
    sys.executable,
    "-m",
    "mlflow",
    "server",
    "--host",
    HOST,
    "--port",
    PORT,
    "--backend-store-uri",
    BACKEND_STORE_URI,
    "--artifacts-destination",
    f"file://{ARTIFACT_DIR}",
]

print("Starting PCS Remote MLflow Server...")
print(f"Backend: {BACKEND_STORE_URI}")
print(f"Artifacts: {ARTIFACT_DIR}")
print(f"Port: {PORT}")

subprocess.run(cmd, check=True)