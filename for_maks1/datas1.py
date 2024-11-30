import json
import random
# Функция для создания улучшенных корреляций в данных
def generate_client_data_with_correlations(client_id):
    segments = ["Малый бизнес", "Средний бизнес", "Крупный бизнес"]
    roles = ["ЕИО", "Сотрудник"]
    methods = ["SMS", "PayControl", "КЭП на токене", "КЭП в приложении"]

    # Корреляции: сегмент бизнеса влияет на выбор текущего метода
    segment = random.choice(segments)
    role = random.choice(roles)
    organizations = random.randint(1, 300)

    # Вероятность выбора метода в зависимости от сегмента
    method_weights = {
        "Малый бизнес": [0.5, 0.3, 0.1, 0.1],
        "Средний бизнес": [0.3, 0.4, 0.2, 0.1],
        "Крупный бизнес": [0.1, 0.3, 0.3, 0.3]
    }
    current_method = random.choices(methods, weights=method_weights[segment])[0]

    # Вероятность наличия мобильного приложения выше для PayControl и КЭП в приложении
    mobile_app = random.random() < (0.9 if current_method in ["PayControl", "КЭП в приложении"] else 0.5)

    # Корреляции: больше организаций - больше подписей, особенно для крупных компаний и роли ЕИО
    factor = {"Малый бизнес": 1, "Средний бизнес": 1.5, "Крупный бизнес": 2}
    role_factor = 2 if role == "ЕИО" else 1
    org_factor = organizations / 100

    signatures_common_mobile = int(random.randint(0, 20) * factor[segment] * role_factor * org_factor)
    signatures_common_web = int(random.randint(0, 50) * factor[segment] * role_factor * org_factor)
    signatures_special_mobile = int(random.randint(0, 10) * factor[segment] * role_factor * org_factor)
    signatures_special_web = int(random.randint(0, 20) * factor[segment] * role_factor * org_factor)

    # Подключённые методы зависят от текущего метода
    available_methods = random.sample(methods, random.randint(1, len(methods)))
    if current_method not in available_methods:
        available_methods.append(current_method)

    # Претензии чаще встречаются у пользователей с SMS и меньше у PayControl/КЭП
    claims_prob = {"SMS": 0.5, "PayControl": 0.1, "КЭП на токене": 0.2, "КЭП в приложении": 0.1}
    claims = 1 if random.random() < claims_prob[current_method] else 0

    return {
        "clientId": f"client_{client_id}",
        "organizationId": f"organization_{client_id}",
        "segment": segment,
        "role": role,
        "organizations": organizations,
        "currentMethod": current_method,
        "mobileApp": mobile_app,
        "signatures": {
            "common": {"mobile": signatures_common_mobile, "web": signatures_common_web},
            "special": {"mobile": signatures_special_mobile, "web": signatures_special_web}
        },
        "availableMethods": available_methods,
        "claims": claims
    }


# Генерация 300 примеров с улучшенными корреляциями
data_with_correlations = [generate_client_data_with_correlations(i) for i in range(1, 2000)]

# Сохранение в файл
output_file_correlated = "synthetic_clients_correlated1.json"
with open(output_file_correlated, "w", encoding="utf-8") as f:
    json.dump(data_with_correlations, f, ensure_ascii=False, indent=4)

output_file_correlated
