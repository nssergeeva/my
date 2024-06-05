first = 25
second = 68
third = 25

first = int(input('первое:'))
second = int(input('второе:'))
third = int(input('третье:'))
if first == second == third:
    print(3)
elif first == second and second == third and third == second:
    print(2)
else:
    print(0)