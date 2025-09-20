hackademic squad - 15 inventary restock predictor


# 📦 Inventory Restock Predictor

A FastAPI-based backend service that predicts when stock will run out based on historical sales data. The system supports weather-based demand adjustment and can send WhatsApp alerts for low stock or approaching expiry.

---

## 🚀 Features

- ✅ Predicts stock-out dates using Excel sales data
- 🌦️ Adjusts predictions based on weather conditions
- 📊 Reads `.xlsx` files for inventory and sales input
- 📩 Sends automated WhatsApp alerts
- 🔐 Environment-configured (e.g., API keys, Twilio credentials)
- 🔌 Modular utilities for forecasting, weather, and messaging

---

## 🧠 How It Works

1. **Upload Excel file** containing columns like `Date`, `Product`, `Sales`, `CurrentStock`, `ExpiryDate`
2. **Forecast** daily average usage per product
3. **Adjust** with weather multiplier (e.g., more ice cream sales on hot days)
4. **Predict** the date when stock will hit zero
5. **Trigger WhatsApp alerts** if a product is near stock-out or expiry

---

## 📁 Project Structure

inventory_predictor/
├── main.py               # FastAPI server
├── app.py                # Extra endpoints (if any)
├── utils/
│   ├── forecast.py       # Predict stock-out date
│   ├── weather.py        # Weather-based adjustments
│   └── whatsapp.py       # Send WhatsApp alerts via Twilio
├── temp_sales_data.xlsx  # Sample Excel data
├── requirements.txt
└── .env                  # Secret keys and config

---

## ⚙️ Setup Instructions

### 🔨 1. Install Dependencies

```bash
pip install -r requirements.txt

🌍 2. Create .env file

TWILIO_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_PHONE_NUMBER=+1415xxxxxxx
RECEIVER_PHONE_NUMBER=+91xxxxxxxxxx

▶️ 3. Run the Server

uvicorn main:app --reload

Visit: http://127.0.0.1:8000

⸻

🧪 Sample API Test

GET /
Response: {"message": "Inventory Restock Predictor API is live."}


⸻

✅ TODO / Future Improvements
	•	Add Streamlit frontend for drag-and-drop file uploads
	•	Add database support (MongoDB/PostgreSQL)
	•	Schedule automatic alerts (e.g., daily at 9 AM)
	•	Add user login/authentication

⸻

🧠 Credits

Built with ❤️ by Hackademic Squad
(Team: Sameer, Kausar, Amin, Suraj)

