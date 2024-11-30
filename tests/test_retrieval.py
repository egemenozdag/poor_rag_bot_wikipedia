from vectorizer import create_embeddings

def test_create_embeddings():
    sentences = ["What is AI?", "Explain RAG."]
    embeddings = create_embeddings(sentences)
    assert len(embeddings) == 2
    assert len(embeddings[0]) > 0  # Her embedding bir değer içermeli
