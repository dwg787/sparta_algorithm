shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]
# 정렬로 푸는 문제

def get_max_discounted_price(prices, coupons):
    prices.sort(reverse=True)
    coupons.sort(reverse=True)

    price_idx = 0
    coupon_idx = 0
    max_discounted_price = 0

    while price_idx < len(prices) and coupon_idx < len(coupons):
        max_discounted_price += prices[price_idx] * (100 - coupons[coupon_idx])/100
        price_idx+=1
        coupon_idx+=1

    while price_idx < len(prices):
        max_discounted_price += prices[price_idx]
        price_idx += 1

    return max_discounted_price


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.