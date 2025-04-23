from flask import Flask, jsonify, render_template
import requests
import os
from dotenv import load_dotenv

# Carga .env con tus credenciales
load_dotenv()

app = Flask(__name__)

TENANT_ID = os.getenv("TENANT_ID")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
WORKSPACE_ID = os.getenv("WORKSPACE_ID")
REPORT_ID = os.getenv("REPORT_ID")
DATASET_ID = os.getenv("DATASET_ID")

def get_access_token():
    url = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "scope": "https://analysis.windows.net/powerbi/api/.default"
    }
    headers = { "Content-Type": "application/x-www-form-urlencoded" }
    response = requests.post(url, data=data, headers=headers)
    response.raise_for_status()
    return response.json()["access_token"]

def get_embed_token():
    access_token = get_access_token()
    url = "https://api.powerbi.com/v1.0/myorg/GenerateToken"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    body = {
        "datasets": [
            { "id": DATASET_ID }
        ],
        "reports": [
            {
                "id": REPORT_ID,
                "groupId": WORKSPACE_ID
            }
        ],
        "accessLevel": "View",
        "lifetimeInMinutes": 55
    }

    print("🔧 Enviando body:", body)
    print("🔧 Con token (parcial):", access_token[:20], "...")

    response = requests.post(url, headers=headers, json=body)
    if not response.ok:
        print("❌ Error Power BI:", response.status_code, response.text)
    response.raise_for_status()
    return {
        "token": response.json()["token"],
        "reportId": REPORT_ID,
        "groupId": WORKSPACE_ID,
        "expiration": response.json()["expiration"]
    }

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/getEmbedToken")
def embed_token():
    return jsonify(get_embed_token())

if __name__ == "__main__":
    app.run(port=10000, debug=True)
