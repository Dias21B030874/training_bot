import os
import requests
from dotenv import load_dotenv

load_dotenv()

class GeminiRecommender:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")  
        self.api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={self.api_key}"

    def get_recommendation_with_best(self, user_problem: str, user_name: str = "Не указано", user_phone: str = "Не указано"):
        directions = [
            "Pilates", "Reformer", "Фитнес", "Силовая", "Растяжка", "Пока не знаю"
        ]
        prompt = (
            f"Ты — консультант студии тренировок. Пользователь:\n"
            f"Имя: {user_name}\n"
            f"Телефон: {user_phone}\n"
            f"Жалоба: {user_problem}\n"
            f"Вот направления, которые мы предлагаем: {', '.join(directions)}.\n"
            "1. Проанализируй жалобу пользователя и выбери ОДНО направление из списка, которое лучше всего поможет ему.\n"
            "2. Объясни, почему именно это направление подходит.\n"
            "3. Ответь от лица компании, дружелюбно и кратко.\n"
            "4. В конце ответа напиши на отдельной строке только выбранное направление (без лишних слов)."
        )

        headers = {"Content-Type": "application/json"}
        params = {"key": self.api_key}
        data = {
            "contents": [
                {"parts": [{"text": prompt}]}
            ]
        }

        try:
            response = requests.post(
                self.api_url,
                headers=headers,
                params=params,
                json=data,
                timeout=10
            )
            response.raise_for_status()
            result = response.json()
            full_text = result["candidates"][0]["content"]["parts"][0]["text"]
            # Последняя строка — выбранное направление
            lines = full_text.strip().splitlines()
            best_direction = lines[-1].strip()
            recommendation = "\n".join(lines[:-1]).strip()
            return recommendation, best_direction
        except Exception as e:
            print(f"[Gemini Error] {e}")
            return "⚠️ Не удалось получить рекомендацию от AI. Попробуйте позже.", "Pilates"