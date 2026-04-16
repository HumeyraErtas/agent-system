from tools import *
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

class AgentSystem:
    def __init__(self):
        self.client = genai.Client(
            api_key=os.getenv("GOOGLE_API_KEY")
        )

    def handle_query(self, user_input):
        try:
            # 🔹 email kontrol
            if "@" not in user_input:
                return "Lütfen email adresinizi belirtin."

            email = [word for word in user_input.split() if "@" in word][0]

            # 🔹 user
            user = get_user_details(email)
            user_id = user["id"]

            # 🔹 transactions
            txs = get_recent_transactions(user_id)

            failed_tx = next((t for t in txs if t["status"] == "failed"), None)

            if not failed_tx:
                return "Başarısız işlem bulunamadı."

            # 🔹 fraud reason
            reason = check_fraud_reason(failed_tx["id"])

            prompt = f"""
            Kullanıcı: {email}
            İşlem ID: {failed_tx['id']}
            Red nedeni: {reason}

            Kullanıcıya açıklayıcı şekilde anlat.
            """

            response = self.client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )

            return response.text

        except Exception as e:
            return f"Hata: {str(e)}"