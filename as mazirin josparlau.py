food = "палау"
food_cal = 150.0
food_weight = 200.0

user_food = input("Сіздің сүйікті тағамыңыз: ")
user_cal = float(input("Ол тағамның 100 г үшін калориясы: "))
user_weight = float(input("Сіз жейтін мөлшер (г): "))

total_cal = (user_cal * user_weight) / 100
avg_cal = (food_cal + user_cal) / 2

print("\n--- Ас мәзірі ---")
print(f"Негізгі тағам: {food}")
print(f"Сіздің таңдауыңыз: {user_food}")
print(f"100 г калория: {user_cal}")
print(f"Жеген мөлшеріңіз: {user_weight} г")
print(f"Барлығы: {total_cal:.1f} ккал")
print(f"Орташа калория: {avg_cal:.1f} ккал")


foods = ["бешбармақ", "палау", "суши", "торт", "кофе", "бауырсақ", "стейк", "омлет", "шай", "бургер"]
print("\nТағамдар тізімі:", foods)

unique_foods = set(foods)
print("Бірегей тағамдар:", unique_foods)

meal_types = ("таңғы ас", "түскі ас", "кешкі ас")
print("\nҚай асқа мәзір құрамыз?")
for i, meal in enumerate(meal_types, 1):
    print(f"{i}. {meal}")

choice = int(input("Нөмірін таңдаңыз: "))

if choice == 1:
    print("Сіз таңғы ас мәзірін таңдадыңыз.")
elif choice == 2:
    print("Сіз түскі ас мәзірін таңдадыңыз.")
elif choice == 3:
    print("Сіз кешкі ас мәзірін таңдадыңыз.")
else:
    print("Қате таңдау!")


food_search = input("\nҚай тағамды іздейсіз? ").lower()
if food_search in unique_foods:
    print("Иә, мұндай тағам мәзірде бар!")
else:
    print("Ондай тағам мәзірде жоқ.")

desc = ("Бүгінгі мәзірде дәмді палау, жұмсақ бауырсақ және қою кофе бар.")
print("\nСипаттама:", desc)

words = desc.split()
print("Сөздер саны:", len(words))

new_desc = desc.replace("кофе", "шай")
print("Жаңартылған сипаттама:", new_desc)

foods_dict = {
    "бешбармақ": 320,
    "палау": 290,
    "суши": 150,
    "торт": 340,
    "кофе": 40,
    "бауырсақ": 270,
    "стейк": 310,
    "омлет": 154,
    "шай": 10,
    "бургер": 330
}

while True:
    print("\n--- Мәзір ---")
    print("1 - Тағамдар тізімі")
    print("2 - Тағам қосу")
    print("3 - Калория көру")
    print("4 - Жалпы калория")
    print("5 - Шығу")

    t = input("Таңдауыңыз: ")

    if t == "1":
        print("\nБарлық тағамдар:")
        for a, b in foods_dict.items():
            print(f"{a}: {b} ккал (100 г)")
    elif t == "2":
        name = input("Тағам атауы: ")
        cal = float(input("100 г үшін калория: "))
        foods_dict[name] = cal
        print(f"{name} мәзірге қосылды!")
    elif t == "3":
        name = input("Қай тағамның калориясын білгіңіз келеді? ")
        if name in foods_dict:
            print(f"{name} тағамы: {foods_dict[name]} ккал (100 г)")
        else:
            print("Ондай тағам жоқ.")
    elif t == "4":
        total = sum(foods_dict.values())
        avg = total / len(foods_dict)
        print(f"Барлық тағамдардың жалпы калориясы: {total:.1f} ккал")
        print(f"Орташа калория: {avg:.1f} ккал")
    elif t == "5":
        print("Бағдарлама аяқталды. Рақмет!")
        break
    else:
        print("Қате таңдау! Дұрыс нөмір енгізіңіз.")
