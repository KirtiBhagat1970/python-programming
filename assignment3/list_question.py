
orders = [
    {
        'id': 101,
        'customer': 'Asha',
        'status': 'DELIVERED',
        'items': [('keyboard', 2, 1499.0), ('mouse', 1, 599.0)]
    },
    {
        'id': 102,
        'customer': 'Ravi',
        'status': 'CANCELLED',
        'items': [('monitor', 1, 10999.0)]
    },
    {
        'id': 103,
        'customer': 'Asha',
        'status': 'DELIVERED',
        'items': [('cable', 5, 199.0)]
    },
    {
        'id': 104,
        'customer': 'Meera',
        'status': 'SHIPPED',
        'items': [('keyboard', 1, 1499.0), ('monitor', 1, 10999.0)]
    },
    {
        'id': 105,
        'customer': 'Ravi',
        'status': 'DELIVERED',
        'items': [('mouse', 3, 599.0)]
    }
]


# A. Calculate revenue customer-wise
def analyse_revenue(orders):
    result = {}
    revenue = {}

    for i in orders:
        if i['status'] != 'CANCELLED':
            customer = i['customer']

            order_value = sum(
                quantity * unit_price
                for product, quantity, unit_price in i['items']
            )

            revenue[customer] = revenue.get(customer, 0) + order_value

    result['revenue'] = revenue
    return result


print(analyse_revenue(orders))


# B. Find top 2 products by quantity
def top(orders):
    top_products = {}
    result = {}

    for i in orders:
        if i['status'] != 'CANCELLED':
            for product, quantity, price in i['items']:
                top_products[product] = (
                    top_products.get(product, 0) + quantity
                )

    top_products = sorted(
        top_products.items(),
        key=lambda x: (-x[1], x[0])
    )[:2]

    result['top_products'] = top_products
    return result


print(top(orders))


# C. Find fully delivered customers
def analyse_delivery(orders):
    result = {}

    customers = {order['customer'] for order in orders}

    fully_delivered = sorted([
        customer
        for customer in customers
        if all(
            order['status'] == 'DELIVERED'
            for order in orders
            if order['customer'] == customer
        )
    ])

    result['fully_delivered'] = fully_delivered
    return result


print(analyse_delivery(orders))
