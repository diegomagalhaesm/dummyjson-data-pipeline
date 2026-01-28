from etl.extract import get_orders
from etl.transform import transform_orders
from etl.load import load_orders

def run_pipeline():
    print("Starting pipeline...")

    data = get_orders()
    print(f"Fetched {len(data)} records")

    df = transform_orders(data)
    print(df.head())

    inserted = load_orders(df)
    print(f"Inserted {inserted} rows")

if __name__ == "__main__":
    run_pipeline()
