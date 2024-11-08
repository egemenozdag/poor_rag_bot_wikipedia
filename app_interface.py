from rag_system import RAGSystem

class AppInterface:
    def __init__(self):
        self.rag_system = RAGSystem()

    def run(self):
        print("Welcome to the RAG system! Type 'exit' to quit.")
        while True:
            query = input("Ask a question: ")
            if query.lower() == "exit":
                print("Goodbye!")
                break
            answer = self.rag_system.ask(query)
            print(f"Answer: {answer}")

