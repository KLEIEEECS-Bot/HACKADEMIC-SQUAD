from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import pandas as pd
from utils.forecast import predict_stockout_date
from utils.weather import get_weather_multiplier
from utils.whatsapp import send_whatsapp_alert
import uvicorn
import os

app = FastAPI()

@app.get("/")
def welcome():
    return {"message": "Inventory Restock Predictor API is live."}

@app.post("/upload-sales/")
async def upload_sales_data(file: UploadFile = File(...)):
    try:
        file_location = f"temp_{file.filename}"
        with open(file_location, "wb+") as f:
            f.write(await file.read())

        df = pd.read_excel(file_location)

        output = []
        for _, row in df.iterrows():
            product = row["Product"]
            current_stock = row["CurrentStock"]
            daily_sales = row["DailySales"]
            lead_time = row["LeadTime"]
            freshness = row.get("Freshness", 1.0)
            weather_multiplier = get_weather_multiplier(city="Dharwad")

            days_left, stockout_date = predict_stockout_date(
                current_stock,
                daily_sales,
                freshness,
                weather_multiplier
            )

            needs_restock = days_left < lead_time
            if needs_restock:
                send_whatsapp_alert(product, days_left)

            output.append({
                "Product": product,
                "CurrentStock": current_stock,
                "Average DailySales": daily_sales,
                "DaysLeft": days_left,
                "StockoutDate": stockout_date,
                "RestockNeeded": needs_restock
            })

        os.remove(file_location)
        return JSONResponse(content=output)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
