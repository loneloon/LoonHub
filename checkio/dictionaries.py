crumbs = [
    {"name": "bread", "price": 100},
    {"name": "wine", "price": 138},
    {"name": "meat", "price": 15},
    {"name": "water", "price": 1}
    ]
crumbs_prices = []
max_prices = []

for goods in crumbs:
    crumbs_prices.append(goods["price"])

print(crumbs_prices)

while len(crumbs_prices) >= 2 and len(max_prices) < 2:
    max_prices.append(max(crumbs_prices))
    crumbs_prices.pop(crumbs_prices.index(max(crumbs_prices)))

print(crumbs_prices)
print(max_prices)

result = []

for goods in crumbs:
        for idx in max_prices:
            if idx in goods.values():
                result.append(goods)
            else:
                continue
print(result)

#print(crumbs_prices)






