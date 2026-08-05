import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("Приветствую, я Ваш персональный фитнес-бот FitLife!")
print("=" * 62)
user_name = input("Пожалуйста, введите Ваше имя: ")
print(f"Привет, {user_name}!")

while True:  #  зациклил, чтобы пользователь использовал только цифры. Можно использовать и цикл for, но тогда нужно будет использовать доп переменные и if else.
    try:
        user_age = int(input("Подскажите, сколько Вам лет? "))
        break
    except ValueError:
        print("Пожалуйста, введите возраст, используя только цифры. Возраст должен быть целым числом.")

while True:  #  зациклил, по тому же принипу, что и с возрастом.
    try:
        user_weight = float(input("Введите Ваш вес в килограммах: "))
        break
    except ValueError:
        print("Пожалуйста, введите вес, используя только цифры и знак точки как десятичный разделитель.")

while True:  
    try:
        user_height = float(input("Введите Ваш рост в метрах: "))
        break
    except ValueError:
        print("Пожалуйста, введите рост, используя только цифры.")  #  я бы хотел добавитть возможность заменять запятую на точку, но пока не знаю как. 

bmi = user_weight / (user_height ** 2) 

user_bmi = round(bmi, 1) 

WATER_PER_KG_ADULT = 30
ML_PER_LITER = 1000

water_ml = user_weight * WATER_PER_KG_ADULT

water_l = round(water_ml / ML_PER_LITER, 2)

print("=" * 62)
print(f"""Отчет для пользователя: {user_name},{user_age} лет: 
Ваш индекс массы тела (BMI) составляет: {user_bmi} кг/м².
Рекомендуемая норма воды в сутки: {water_l} литра.""")
print("=" * 62)
print("Спасибо, что воспользовались FitLife! Берегите себя!")