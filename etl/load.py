import pandas as pd
from sqlalchemy import create_engine
from config import DB_URL

engine = create_engine(DB_URL)

def load_orders(df):

    with engine.begin() as conn:
        try:
            existing = pd.read_sql("SELECT id FROM fact_orders", conn)
            new_df = df[~df["id"].isin(existing["id"])]
        except:
            new_df = df

        new_df.to_sql("fact_orders", conn, if_exists="append", index=False)

    return len(new_df)
