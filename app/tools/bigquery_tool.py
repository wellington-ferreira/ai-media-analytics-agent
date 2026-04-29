from google.cloud import bigquery

client = bigquery.Client()

def get_media_data():
    query = """
        WITH users_base AS (
        SELECT
            id AS user_id,
            traffic_source
        FROM `bigquery-public-data.thelook_ecommerce.users`
        ),

        orders_base AS (
            SELECT
                user_id,
                order_id,
                created_at
            FROM `bigquery-public-data.thelook_ecommerce.orders`
            WHERE DATE(created_at) >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
        ),

        revenue_base AS (
            SELECT
                order_id,
                SUM(sale_price) AS order_revenue
            FROM `bigquery-public-data.thelook_ecommerce.order_items`
            GROUP BY order_id
        ),

        joined AS (
            SELECT
                u.traffic_source,
                u.user_id,
                o.order_id,
                r.order_revenue
            FROM users_base u
            LEFT JOIN orders_base o
                ON u.user_id = o.user_id
            LEFT JOIN revenue_base r
                ON o.order_id = r.order_id
        )

        SELECT
            traffic_source,

            COUNT(DISTINCT user_id) AS users,

            COUNT(DISTINCT order_id) AS orders,

            SUM(order_revenue) AS revenue,

            SAFE_DIVIDE(
                COUNT(DISTINCT CASE WHEN order_id IS NOT NULL THEN user_id END),
                COUNT(DISTINCT user_id)
            ) AS conversion_rate,

            SAFE_DIVIDE(
                SUM(order_revenue),
                COUNT(DISTINCT user_id)
            ) AS revenue_per_user

        FROM joined
        GROUP BY traffic_source
        ORDER BY revenue DESC
        """

    query_job = client.query(query)
    results = query_job.result()

    data = []
    for row in results:
        users = row.users or 0
        orders = row.orders or 0
        revenue = float(row.revenue or 0)

        conversion_rate = (orders / users) if users else 0
        rpu = (revenue / users) if users else 0

        data.append({
            "traffic_source": row.traffic_source,
            "users": users,
            "orders": orders,
            "revenue": revenue,
            "conversion_rate": round(conversion_rate, 4),
            "revenue_per_user": round(rpu, 2)
        })

    return data