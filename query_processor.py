from data_retriever import DataRetriever

class QueryProcessor:
    def __init__(self):
        pass

    def process_query(self, query):
        # Gelen sorguyu işle ve daha düzgün bir formatla API'ye ilet.
        processed_query = query.strip().replace(" ", "_").lower()
        return processed_query
