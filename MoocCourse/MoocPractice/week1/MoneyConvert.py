money = input()
if money[0:3] == 'RMB':
    new_money = eval(money[3:])/6.78
    print('USD{:.2f}'.format(new_money))
elif money[0:3] == 'USD':
    new_money = eval(money[3:]) * 6.78
    print('RMB{:.2f}'.format(new_money))