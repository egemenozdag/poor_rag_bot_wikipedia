from transformers import pipeline
from query_processor import QueryProcessor

class AnswerGenerator:
    def __init__(self):
        # GPT-2 modelini daha doğru ve sorunsuz çalışması için konfigüre ediyoruz.
        self.generator = pipeline(
            "text-generation",
            model="gpt2",
            tokenizer="gpt2",
            max_length=150,
            pad_token_id=50256,  # GPT-2'nin eos_token_id'si pad_token_id olarak kullanılıyor
            truncation=True
        )

    def generate_answer(self, context):
        try:
            # Yine veriyi alıp daha uzun ve anlamlı cevaplar üretiyoruz
            response = self.generator(
                context,
                max_length=150,
                num_return_sequences=1,
                pad_token_id=50256,  # Bunu tekrar kontrol ediyoruz
                truncation=True
            )
            return response[0]['generated_text']
        except Exception as e:
            print(f"Error generating answer: {e}")
            return "Sorry, something went wrong."
