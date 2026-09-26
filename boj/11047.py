coins, money = map(int, input().split())
coin_list = list()

for i in range(coins):
    coin = int(input())
    coin_list.append(coin)

coin_list.sort(reverse=True)

coinCount = 0

for i in range(len(coin_list)):
    if money // coin_list[i] > 0:
        div = money // coin_list[i]
        # 4200원이라 하면 4200 // 1000 == 4잖아.
        coinCount += money // coin_list[i]
        money = money - (coin_list[i] * div)
        # 4200원이 있다 하고 4000원이라 하면

print(coinCount)