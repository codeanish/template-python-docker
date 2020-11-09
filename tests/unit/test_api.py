from app import api

def test_hello_world():
    assert api.hello_world() == "Hello World"


def test_answer_to_the_meaning_of_life():
    assert api.answer_to_the_ultimate_question_of_life() == "42"