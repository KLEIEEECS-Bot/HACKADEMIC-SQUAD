from datetime import datetime, timedelta

def predict_stockout_date(current_stock, daily_sales, freshness=1.0, weather_multiplier=1.0):
    adjusted_sales = daily_sales * freshness * weather_multiplier
    if adjusted_sales == 0:
        days_left = 999
    else:
        days_left = int(current_stock // adjusted_sales)

    stockout_date = datetime.today() + timedelta(days=days_left)
    return days_left, stockout_date.strftime("%Y-%m-%d")
