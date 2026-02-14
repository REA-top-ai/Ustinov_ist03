print((6 * 6) - 1 == 8 + 1 )
print(13 - 7 != (3 * 2) + 1 )
print(3 * (2 - 1) == 4 - 1 )

print((6 * 6) - 1 >= 8 + 1 )
print(3 - 7 <= (3 * 2) + 1 )
print(3 * (2 - 1) > 4 - 1 )

bool_variable_2 = True
print(bool_variable_2)

user_name = input()
Dmitriy_check = 'Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!'
hi = '«Добро пожаловать»'
if user_name == 'Дмитрий':
    print(Dmitriy_check)
else:
    print(hi)

statement_1 = (2+2+2>=6) and (-1*-1<0)
statement_2 = (4*2<=8) and (7 - 1 == 6)

Dmima_Check = "Дмитрий"
Angel_check = 'Ангелина'
Vasea_check = 'Василий'
Katea_chek = 'Екатерина'
APM1 = "1234"
APM2 = "2345"
APM3 = "3456"
APM4 = "5678"

DA = Dmima_Check + APM1
AA = Angel_check + APM2
VA = Vasea_check + APM3
KA = Katea_chek + APM4

usr_name = input("Введите свое имя: ")
pasw = input('Ведите свой APM: ')

if usr_name + pasw == DA:
    print('Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!')
elif usr_name + pasw != AA and usr_name + pasw != VA and usr_name + pasw != KA and usr_name + pasw != DA:
    print('Логин или пароль не верный')
else:
    print("Добро пожаловать!")


print((2-1>3) or (-5*2==-10))
print((9+5 <= 15) or (7 != 4+3))