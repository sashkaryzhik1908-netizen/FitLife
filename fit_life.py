print("Приветствую, я Ваш персональный фитнес-бот FitLife!")
print("=" * 62)
user_name = input("Пожалуйста, введите Ваше имя: ")
print(f"Привет, {user_name}!")

while True:  # зациклил, чтобы пользователь использовал только цифры.
    try:
        user_age = int(input("Подскажите, сколько Вам лет? "))
        break
    except ValueError:
        print("""Пожалуйста, введите возраст, используя только цифры.
Возраст должен быть целым числом.""")

age_name = ""
if user_age % 100 in [11, 12, 13, 14]:
    age_name = "лет"
elif user_age % 10 == 1:
    age_name = "год"
elif user_age % 10 in [2, 3, 4]:
    age_name = "года"
else:
    age_name = "лет"

while True:  # зациклил, по тому же принипу, что и с возрастом.
    try:
        user_weight = float(input("Введите Ваш вес в килограммах: "))
        break
    except ValueError:
        print("""Пожалуйста, введите вес, используя только цифры"
        " и знак точки как десятичный разделитель.""")

while True:
    try:
        user_height = float(input("Введите Ваш рост в метрах: "))
        break
    except ValueError:
        print("Пожалуйста, введите рост, используя только цифры.")

user_bmi = round(user_weight / (user_height ** 2), 1)

WATER_PER_KG_ADULT = 30
ML_PER_LITER = 1000

water_l = round(user_weight * WATER_PER_KG_ADULT / ML_PER_LITER, 2)

print("=" * 62)
print(f"""Отчет для пользователя: {user_name}, {user_age} {age_name}:
Ваш индекс массы тела (BMI) составляет: {user_bmi} кг/м².
Рекомендуемая норма воды в сутки: {water_l} литра.""")
print("=" * 62)
print("Спасибо, что воспользовались FitLife! Берегите себя!")
