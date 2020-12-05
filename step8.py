def apply_discound(price, discount):
    return price * (100 - discount) / 100


# def discound_product(price):
#     pass
basket = [5768.32, 4213.23, 12356, 12456]
basket_sum = sum(basket)
print(basket_sum)

basket_sum_discounted = 0
discount_1 = 7

for product in basket:
    basket_sum_discounted += apply_discound(product, discount_1)
# print(product, apply_discound(product, 15))
print(basket_sum_discounted)
