otvet ="да"
while otvet == "да":
    speed = float(input("Введите скорость автомобиля: "))
    if speed > 60:
        print("Вы превысили скорость")
    elif speed >= 40:
        print("Счастливого пути")
    else:
        print("Прибавьте скорость")

    otvet = input("Проверять скорость дальше =да=: ")

print("Конец")
print("Ура")
