CREATE TABLE IF NOT EXISTS fact_orders (
    id INT PRIMARY KEY,
    user_id INT,
    total NUMERIC,
    discounted_total NUMERIC,
    total_products INT,
    total_quantity INT,
    ingestion_date TIMESTAMP
);