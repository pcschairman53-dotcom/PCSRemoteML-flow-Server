# PCS Remote MLflow Server

Lightweight remote MLflow Tracking Server for PCS Model Health Guard.

## Local Run

Create virtual environment:

python -m venv .venv

Activate on Windows:

.venv\Scripts\activate

Install:

pip install -r requirements.txt

Run:

python start_mlflow.py

Open:

http://127.0.0.1:10000

## Remote Client

Set:

MLFLOW_TRACKING_URI=https://YOUR-MLFLOW-URL

The PCS Model Health Guard application can then connect to this server.

## Persistent Storage

Production deployment should use a persistent storage location.

Expected data directory:

/var/data/mlflow