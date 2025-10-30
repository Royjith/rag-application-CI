from app.rag_pipeline import generate_answer

def test_generate_answer():
    response = generate_answer("What is AI?")
    assert "AI" in response

