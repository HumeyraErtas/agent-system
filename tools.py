users = {
    "ali@sirket.com": {"id": "u1", "status": "active"},
    "ayse@sirket.com": {"id": "u2", "status": "inactive"}
}

transactions = {
    "u1": [
        {"id": "t1", "amount": 100, "status": "failed"},
        {"id": "t2", "amount": 200, "status": "success"}
    ],
    "u2": [
        {"id": "t3", "amount": 300, "status": "failed"}
    ]
}

fraud_reasons = {
    "t1": "Kart limiti yetersiz",
    "t3": "Şüpheli işlem tespit edildi"
}


def get_user_details(email: str):
    if email not in users:
        raise ValueError("Kullanıcı bulunamadı")
    return users[email]


def get_recent_transactions(user_id: str, limit: int = 5):
    return transactions.get(user_id, [])[:limit]


def check_fraud_reason(transaction_id: str):
    return fraud_reasons.get(transaction_id, "Sebep bulunamadı")