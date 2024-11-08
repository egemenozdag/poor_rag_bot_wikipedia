from data_retriever import DataRetriever
from query_processor import QueryProcessor
from answer_generator import AnswerGenerator

class RAGSystem:
    def __init__(self):
        self.data_retriever = DataRetriever()
        self.query_processor = QueryProcessor()
        self.answer_generator = AnswerGenerator()

    def ask(self, query):
        # 1. Sorguyu işliyoruz
        processed_query = self.query_processor.process_query(query)
        # 2. API'den veri çekiyoruz
        context = self.data_retriever.fetch_data(processed_query)
        # 3. Eğer veri yoksa, hata mesajı döndürüyoruz
        if not context or "Error" in context:
            return context
        # 4. Veriyi kullanarak yanıt üretiyoruz
        answer = self.answer_generator.generate_answer(context)
        return answer
