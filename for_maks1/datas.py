import json
import random
# Функция для генерации синтетических данных
def generate_synthetic_data_with_correlations(num_records=200):
    segments = ["Малый бизнес", "Средний бизнес", "Крупный бизнес"]
    roles = ["ЕИО", "Сотрудник"]
    methods = ["SMS", "PayControl", "КЭП на токене", "КЭП в приложении"]
    data = []

    for _ in range(num_records):
        segment = random.choices(segments, weights=[0.5, 0.3, 0.2])[0]
        role = random.choice(roles)
        organizations = random.randint(1, 50) if segment == "Малый бизнес" else (
            random.randint(51, 150) if segment == "Средний бизнес" else random.randint(151, 300))
        mobile_app = random.choice([True, False]) if segment != "Малый бизнес" else True
        current_method = random.choice(methods) if mobile_app else random.choice(["SMS", "КЭП на токене"])
        claims = random.randint(0, 2) if current_method != "SMS" else random.randint(0, 5)
        signatures = {
            "common": {
                "mobile": random.randint(1, 20) if mobile_app else random.randint(0, 5),
                "web": random.randint(1, 20) if not mobile_app else random.randint(0, 10),
            },
            "special": {
                "mobile": random.randint(0, 10) if mobile_app else 0,
                "web": random.randint(0, 5),
            },
        }
        available_methods = random.sample(methods, k=random.randint(1, len(methods))) if segment != "Малый бизнес" else ["SMS", "КЭП на токене"]
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
new_data = generate_synthetic_data_with_correlations(200)

# Сохранение данных в файл
with open("synthetic_data_with_correlations.json", "w", encoding="utf-8") as f:
    json.dump(new_data, f, ensure_ascii=False, indent=4)

print("Данные сохранены в файл 'synthetic_data_with_correlations.json'")
