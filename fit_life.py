#  Позволил себе немного вольности
print("Приветствую, я Ваш персональный фитнес-бот FitLife!")
print("=" * 62)
user_name = input("Пожалуйста, введите Ваше имя: ")
print(f"Привет, {user_name}!")
while True:  # зациклил, чтобы пользователь вводил нужный текст
    user_sex = input("Eкажите Ваш пол (мужской/женский): ").lower() # это пригодится далее
    if user_sex == "мужской": 
        user_sex = "male"
        break
    elif user_sex == "женский":
        user_sex = "female"
        break
    else:
        print("Пожалуйста, введите 'мужской' или 'женский'.")

while True:  # зациклил, чтобы пользователь использовал только цифры. Можно использовать и цикл for, но тогда нужно будет использовать доп переменные и if else.
    try:
        user_age = int(input("Подскажите, сколько Вам лет? "))
        break
    except ValueError:
        print("Пожалуйста, введите возраст, используя только цифры. Возраст должен быть целым числом.")

while True:  # зациклил, по тому же принипу, что и с возрастом.
    try:
        user_weight = float(input("Введите Ваш вес в килограммах: "))
        break
    except ValueError:
        print("Пожалуйста, введите вес, используя только цифры и знак точки как десятичный разделитель.")

while True:  
    try:
        user_height_sm = float(input("Введите Ваш рост в сантиметрах: "))
        user_height = user_height_sm / 100
        break
    except ValueError:
        print("Пожалуйста, введите рост, используя только цифры.")  # я бы хотел добавитть возможность заменять запятую на точку, но пока не знаю как. 
bmi = user_weight / (user_height ** 2) 
user_bmi = round(bmi, 1) 
if user_bmi < 18.5:
    user_bmi_category = "недостаточный вес, вам нужно питаться более калорийно."
elif 18.5 <= user_bmi < 24.9:
    user_bmi_category = "нормальный вес, продолжайте поддерживать здоровый образ жизни." 
elif 25 <= user_bmi < 29.9:
    user_bmi_category = "избыточный вес, рекомендуется обратиться к диетологу."
elif 30 <= user_bmi < 34.9:
    user_bmi_category = "ожирение I степени, Вам необходимо контролировать питание и физическую активность."
elif 35 <= user_bmi < 39.9:
    user_bmi_category = "ожирение II степени, Вам необходимо контролировать питание и физическую активность."
elif user_bmi >= 40:
    user_bmi_category = """ожирение III степени, 
Вам необходимо контролировать питание и физическую активность, если для Вас это проблема, 
то рекомендуется обратиться к врачу."""
def calc_ideal_weight(height, sex): # Формула Лоренца, используется для расчета идеального веса. 
    if sex == "male":  #все расчеты в медецине ведутся на идеальный вес, в том чисел потребность в жидкости.
        ideal_weight = height - 100 - ((height - 150) / 4) 
    elif sex == "female":  
        ideal_weight = height - 100 - ((height - 150) / 2)
    return ideal_weight
ideal_weight = calc_ideal_weight(user_height_sm, user_sex)
WATER_PER_KG_ADULT = 30
WATER_PER_KG_OLD = 25
WATER_PER_KG_VERY_OLD = 20
ML_PER_LITER = 1000
water_ml = ideal_weight * WATER_PER_KG_ADULT
if user_age >= 65 and user_age < 75:
    water_ml = ideal_weight * WATER_PER_KG_OLD
elif user_age >= 75:
    water_ml = ideal_weight * WATER_PER_KG_VERY_OLD  # если говорить о потребности жидкости, с медицинской точки зрения этьи расчеты более точные.
water_l = round(water_ml / ML_PER_LITER, 2)
print("=" * 62)
print(f"""Отчет для пользователя: {user_name}: 
Ваш индекс массы тела (BMI) составляет: {user_bmi} кг/м². У вас {user_bmi_category}
Рекомендуемая норма воды в сутки: {water_l} литра.""")
print("=" * 62)
print("Спасибо, что воспользовались FitLife! Берегите себя!")