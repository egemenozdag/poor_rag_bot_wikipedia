from retrieval import fetch_wikipedia_data

def test_fetch_wikipedia_data():
    query = "Artificial Intelligence"
    data = fetch_wikipedia_data(query)
    assert "Artificial Intelligence" in data["title"]
    assert len(data["content"]) > 100  # İçerik minimum bir uzunluğa sahip olmalı
