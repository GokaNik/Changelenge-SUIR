import random
import json


def generate_realistic_data(num_records=200):
    segments = ["Малый бизнес", "Средний бизнес", "Крупный бизнес"]
    roles = ["ЕИО", "Сотрудник"]
    methods = ["SMS", "PayControl", "КЭП на токене", "КЭП в приложении"]
    data = []

    for _ in range(num_records):
        # 1. Сегмент бизнеса
        segment = random.choices(segments, weights=[0.5, 0.3, 0.2])[0]

        # 2. Количество организаций
        organizations = random.randint(1, 50) if segment == "Малый бизнес" else (
            random.randint(51, 150) if segment == "Средний бизнес" else random.randint(151, 300))

        # 3. Роль уполномоченного лица
        role = random.choice(roles)

        # 4. Мобильное приложение
        mobile_app = random.choice([True, False]) if segment != "Малый бизнес" else True

        # 5. Доступные методы подписания
        if organizations < 50:
            available_methods = ["SMS", "КЭП на токене"]
        elif organizations < 150:
            available_methods = random.sample(methods, k=random.randint(2, 3))
        else:
            available_methods = methods

        # 6. Текущий метод подписания
        current_method = random.choice(available_methods) if mobile_app else "SMS"

        # 7. Жалобы
        if current_method == "SMS":
            claims = random.randint(0, 5)
        elif current_method in ["PayControl", "КЭП на токене"]:
            claims = random.randint(0, 2)
        else:  # "КЭП в приложении"
            claims = random.randint(0, 1)

        # 8. Подписи документов
        signatures_common_mobile = random.randint(1, 20) if mobile_app else random.randint(0, 5)
        signatures_common_web = random.randint(1, 20) if not mobile_app else random.randint(0, 10)
        signatures_special_mobile = random.randint(5, 15) if role == "ЕИО" and mobile_app else random.randint(0, 5)
        signatures_special_web = random.randint(5, 15) if role == "ЕИО" else random.randint(0, 5)

        signatures = {
            "common": {
                "mobile": signatures_common_mobile,
                "web": signatures_common_web,
            },
            "special": {
                "mobile": signatures_special_mobile,
                "web": signatures_special_web,
            },
        }

        # Собираем запись
        record = {
            "clientId": f"client_{random.randint(1000, 9999)}",
            "organizationId": f"org_{random.randint(100, 999)}",
            "segment": segment,
            "role": role,
            "organizations": organizations,
            "currentMethod": current_method,
            "mobileApp": mobile_app,
            "signatures": signatures,
            "availableMethods": available_methods,
            "claims": claims,
        }
        data.append(record)

    return data


# Генерация данных
realistic_data = generate_realistic_data(500)

# Сохранение данных в JSON-файл
output_path = "realistic_synthetic_data.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(realistic_data, f, ensure_ascii=False, indent=4)

print(f"Данные сохранены в файл: {output_path}")
