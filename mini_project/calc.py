while True:
    a = float(input('Выберите первое число = '))
    b = float(input('Выберите второе число = '))
    s = input("Выберите операцию из следующих(+,-,*,/): ")
    if s == '0':
        break
    if s not in ('+','-','*','/'):
        continue
    
    if s == '+':
        print((f'Ответик:'), a+b)
    elif s == '-':
        print((f'Ответик:'), a-b)
    elif s == '*':
        print((f'Ответик:'), a*b)
    elif s == '/':
        if b !=0:
            print((f'Ответик:'), a/b)
        else:
            print(f'Данной операции нет в системе!!!')
