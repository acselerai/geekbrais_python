GOOD_DETAILS_INDEX = 1


def fetch_good_details(goods):
    good_details = []

    for good in goods:
        good_details.append(good[GOOD_DETAILS_INDEX])

    return good_details


def fetch_good_details_keys(good_details):
    good_details_keys = []

    for good_detail in good_details:
        good_details_keys.extend(good_detail.keys())

    return set(good_details_keys)


def compose_analytics(analytics_keys, good_details):
    combined_analytics = {}

    for analytic_key in analytics_keys:
        combined_analytics[analytic_key] = set(
            [good_detail[analytic_key] for good_detail in good_details]
        )

    return combined_analytics


goods = [
    (1, {'name': 'PC', 'price': 20000, 'amount': 5, 'unit': 'item'}),
    (2, {'name': 'printer', 'price': 6000, 'amount': 2, 'unit': 'item'}),
    (3, {'name': 'scanner', 'price': 2000, 'amount': 7, 'unit': 'item'})
]

good_details = fetch_good_details(goods)
analytics_keys = fetch_good_details_keys(good_details)
analytics = compose_analytics(analytics_keys, good_details)

print(analytics)
