score = int(input())

if score < 0:
    print("Неправильный ввод")
elif score >= 0 and score < 50:
    print("Не сдано")
elif score >= 50 and score < 70:
    print("Удовлетворительно")
elif score >= 70 and score < 90:
    print("Хорошо")
elif score >= 90 and score <= 100:
    print("Отлично")
elif score > 100:
    print("Слишком умный")

