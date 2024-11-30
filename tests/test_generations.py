from pipeline import generate_answer

def test_generate_answer():
    query = "What is the capital of France?"
    answer = generate_answer(query)
    assert "Paris" in answer
