import requests
import os

def send_whatsapp_alert(product, days_left):
    ACCESS_TOKEN = os.getenv("WHATSAPP_ACCESS_TOKEN", "your_token")
    PHONE_NUMBER_ID = os.getenv("WHATSAPP_PHONE_ID", "your_id")
    RECEIVER_PHONE = os.getenv("OWNER_PHONE", "your_phone_number")

    url = f"https://graph.facebook.com/v17.0/{PHONE_NUMBER_ID}/messages"

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    data = {
        "messaging_product": "whatsapp",
        "to": RECEIVER_PHONE,
        "type": "text",
        "text": {
            "body": f"⚠️ Low Stock Alert: '{product}' will run out in {days_left} days. Please reorder ASAP."
        }
    }

    response = requests.post(url, headers=headers, json=data)
    print("WhatsApp Response:", response.status_code, response.text)
