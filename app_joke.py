def attention(text):
    for i in range(1, 5):
        print(">" * i)
    print(">" * 5, "ВНИМАНИЕ! ВАЖНАЯ ИНФОРМАЦИЯ!")
    for i in range(4, 0, -1):
        print(">" * i)
    print(text)
    x = input("1 - ДА, 2 - НЕТ: ")


attention("Вы знаете, что высыпаться очень важно?")
attention("Вы знаете, что чтение книг развивает воображение?")
attention("Вы знаете, что хорошо учиться хорошо, а плохо - плохо?")
attention("Вы тоже чувствуете, что программа бессмысленна?")
