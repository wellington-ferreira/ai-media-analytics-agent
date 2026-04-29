from google.cloud import bigquery

client = bigquery.Client()

def run_query(question: str):
    query = """
    SELECT
        traffic_source,
        COUNT(DISTINCT user_id) as users,
        COUNT(DISTINCT order_id) as orders,
        SUM(sale_price) as revenue
    FROM `bigquery-public-data.thelook_ecommerce.order_items`
    GROUP BY traffic_source
    """

    results = client.query(query).result()

    return [dict(row) for row in results]