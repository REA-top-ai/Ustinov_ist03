orders = ['маргаритки', 'васильки']
orders.append('тульпаны')
orders.append('розы')
print(orders)

orders = ['маргаритка', 'лютик', 'львиный зев', 'гардения', 'лилия']
new_orders = orders + ['сирень','ирис']
broken_prices = [5, 3, 4, 5, 4] + [4]
print(broken_prices)

list1=range(9)
print(list(list1))
list2=range(8)
print(list(list2))
lll = range(5,16,3)
print(list(lll))
lll2=range(0,40,5)
print(list(lll2))

first_names = ['Эйнсли', 'Бен', 'Чани', 'Депак']
age = []
age.append('42')
all_ages=['32','41','29'] + age
name_and_age = zip(first_names,all_ages)
ids = range(4)