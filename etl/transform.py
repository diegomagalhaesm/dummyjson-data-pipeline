import pandas as pd

def transform_orders(data):
    df = pd.json_normalize(data)

    df = df[[
        "id", "userId", "total", "discountedTotal",
        "totalProducts", "totalQuantity"
    ]]

    df.columns = [
        "id", "user_id", "total", "discounted_total",
        "total_products", "total_quantity"
    ]

    df["ingestion_date"] = pd.Timestamp.utcnow()

    return df

