from lib.experiences import Experiences
from lib.numbers import Numbers

def test_word_count_for_content():
    entry = Experiences("Monday", "Coding in java")
    assert entry.word_count() == 3

def test_add_all_phone_numbers_to_each_entry():
    entry = Experiences("Monday", "Coding in java")
    number = Numbers("Nnemdi", "123456")
    entry.add_number(number)
    assert entry.list_numbers() == "Nnemdi: 123456"

