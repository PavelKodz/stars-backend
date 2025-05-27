from flask import Flask, jsonify
import os
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
BOT_TOKEN = os.getenv("BOT_TOKEN")

@app.route("/get_invoice")
def get_invoice():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/createInvoiceLink"
    data = {
        "title": "Сбросить лимит",
        "description": "Оплата сброса ограничений",
        "payload": "reset_limit",
        "provider_token": "",
        "currency": "XTR",
        "prices": [{"label": "Сброс", "amount": 1000}]
    }
    response = requests.post(url, json=data)
    return jsonify(response.json())