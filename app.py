import datetime
from twilio.rest import Client
import streamlit as st
import pandas as pd
import requests
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="Inventory Restock Predictor", layout="wide")
st.title(" Inventory Restock Predictor")

st.markdown("Upload your sales Excel file (`.xlsx`) with these columns: **Product, CurrentStock, DailySales, LeadTime, [Freshness]**")

# Twilio WhatsApp configuration (update with your actual credentials)
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_FROM = os.getenv("TWILIO_WHATSAPP_FROM")
WHATSAPP_TO = os.getenv("WHATSAPP_TO")

uploaded_file = st.file_uploader("Choose Excel file", type="xlsx")

if uploaded_file:
    with st.spinner("Processing..."):
        files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
        try:
            response = requests.post("http://127.0.0.1:8000/upload-sales/", files=files)
            if response.status_code == 200:
                result = pd.DataFrame(response.json())

                # Send WhatsApp notification if any product expires in 2 days
                today = datetime.date.today()
                expiring_soon = result[result['DaysLeft'] == 2]
                if not expiring_soon.empty:
                    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
                    for _, row in expiring_soon.iterrows():
                        message_body = f"⚠️ ALERT: '{row['Product']}' has only 2 days left before stockout!"
                        client.messages.create(
                            body=message_body,
                            from_=TWILIO_WHATSAPP_FROM,
                            to=WHATSAPP_TO
                        )

                def highlight_restock(row):
                    styles = []
                    for _, val in row.items():
                        if row.get('DaysLeft', 1) <= 0:
                            styles.append('background-color: #000000')  # Light red for expired
                        elif row.get('RestockNeeded', False):
                            styles.append('background-color: #000000')  # Light pink for restock
                        else:
                            styles.append('')
                    return styles

                st.subheader(" Stock Prediction Results")
                styled = result.style.apply(highlight_restock, axis=1)
                st.dataframe(styled, use_container_width=True)
            else:
                st.error("Error from backend: " + str(response.json()))
        except Exception as e:
            st.error(f"Connection error: {e}")

st.markdown("---")
