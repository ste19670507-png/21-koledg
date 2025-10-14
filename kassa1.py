otvet ="да"
while otvet == "да":
    n = int(input("Ведите колличество товара: "))
    sp_cena = []
    i = 0
    while i < n:
        cena = float(input(f"Введите цену товара {i + 1}:"))
        sp_cena.append(cena)
        i = i + 1
    s = sum(sp_cena)
    print(f"Сумма вашей покупки: {s:.2f} руб.")
    nal = float(input("Введите сумму наличных: "))
    while nal < s:
        d = s - nal
        print(f"Недостаточно средств! Требуется доплатить {d:.2f}")
        d = float(input("Введите сумму доплаты: "))
        nal = nal + d
    sd = nal - s
    i = 0
    print("========ЧЕК========")
    while i < n:
        print(f"Товар {i + 1}: {sp_cena[i]:.2f} руб.")
        i = i + 1
    print(f"Сумма покупки: {s:.2f} руб.")
    print(f"Внесено: {nal:.2f} руб.")
    print(f"Сдача: {sd:.2f} руб.")
    print("===================\n")

    otvet = input("Есть следующий покупатель? (да/нет): ")




