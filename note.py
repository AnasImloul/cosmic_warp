from datetime import datetime

daily_price = 0.5

interest_rate = 0.01

cost = 0

date = datetime.now()

date = date.replace(year=2016, month=11, day=21)

today = datetime.now()

difference = (today - date).total_seconds()

seconds_in_day = 7 * 24 * 3600


for day in range(int(difference / seconds_in_day)):
    cost += daily_price * 7
    daily_price *= (1 + interest_rate)


print(daily_price)

cost = str(int(cost))

print("_".join([cost[i:i+3] for i in range(0, len(cost), 3)]))