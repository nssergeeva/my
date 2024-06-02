#мы можем поменять элемент числа кортежа, но заданное значение кортежа неизменно
immutable_var = ([5], 'cat')
print(immutable_var)
immutable_var[0][0] = 'wolf'
print(immutable_var)
#Кортеж неизменяемое имеет (...) исключением можно встретить сложение и умножение
#Список изменяемое имеет [...]
mutable_list = ["ручей", "река", "озеро", "море"]
mutable_list[0] = 1
mutable_list.remove("море")
mutable_list.append('капля')
print(mutable_list)
