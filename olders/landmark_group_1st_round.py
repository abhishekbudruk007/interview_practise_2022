
#
# prices = [1000 , 2000 , 3000 , 4000.......1000]
#
# small_prices [-1]
# bigger_prices[0] = 6000


# def get_price_list(price_list_array):
    # n = len(price_list_array)
    # mid = len(price_list_array) // 2
    # print(mid)
    # lower_prices = price_list[0:mid]
    # price_list(price_list_array)

    # higher_prices = price_list[mid+1:n]
    # price_list(higher_prices)
    # # return lower_prices, higher_prices

price_list = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
print(price_list)
n = len(price_list)
mid = len(price_list) // 2
lower_prices = price_list[0:mid]
higher_prices = price_list[mid:n]
print(lower_prices)
print(higher_prices)


combinations = []
for i in range(len(lower_prices)):
    for j in range(i):
        tuple = (lower_prices[j], lower_prices[j+1])
        if tuple not in combinations:
            combinations.append(tuple)
print(combinations)




