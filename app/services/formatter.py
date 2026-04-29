def format_data(data):
    text = ""

    for row in data:
        text += f"""
Canal: {row['traffic_source']}
- Usuários: {row['users']}
- Pedidos: {row['orders']}
- Receita: R$ {round(row['revenue'], 2)}
- Conversão: {round(row['conversion_rate']*100, 2)}%
- RPU: R$ {row['revenue_per_user']}
"""

    return text