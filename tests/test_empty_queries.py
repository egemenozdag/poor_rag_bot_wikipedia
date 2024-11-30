from pipeline import generate_answer

def test_empty_query():
    query = ""
    answer = generate_answer(query)
    assert answer == "Query cannot be empty."
