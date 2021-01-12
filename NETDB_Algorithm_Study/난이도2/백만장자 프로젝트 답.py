"""
def search_max_index(start, end, price_list):
    return price_list[start: end].index(max(price_list[start: end])) + start
 
def sell(start, end, price_list):
    return price_list[end]*(end-start) - sum(price_list[start:end])
 
def stockpile(day, price_list):
    profit = 0
    pivot = 0
    max_i = search_max_index(0, day, price_list)
    for i in range(day):
        if i == max_i:
            profit += sell(pivot, max_i, price_list)
            if i == day-1:
                break
            pivot = i+1
            max_i = search_max_index(max_i+1, day, price_list)
    return profit
 
case_len = int(input())
for i in range(case_len):
    day = int(input())
    price_list = list(map(int, input().split(' ')))
    profit = stockpile(day, price_list)
    print("#{} {}".format(i+1, profit))
"""
case_len = int(input())
for i in range(case_len):
    day = int(input())
    price_list = list(map(int, input().split(' ')))
     
    max_price = 0
    profit = 0
    for d in range(day)[::-1]:
        price = price_list[d]
        if price > max_price:
            max_price = price
            continue
        profit += (max_price - price)
     
    print("#{} {}".format(i+1, profit))