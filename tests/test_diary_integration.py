from lib.diary import Diary
from lib.experiences import Experiences
from lib.todo import Todo
from lib.numbers import Numbers

def test_diary_has_no_entries():
    diary = Diary()
    assert diary.entries == []

def test_add_diary_entries():
    diary = Diary()
    entry_1 = Experiences("Monday", "Coding in java")
    diary.add(entry_1)
    entry_2 = Experiences("Tuesday", "Coding in ruby")
    diary.add(entry_2)
    assert diary.list() == "Monday: Coding in java, Tuesday: Coding in ruby"

def test_select_diary_entry_based_on_time():
    diary = Diary()
    entry_1 = Experiences("Monday", "Coding in java")
    entry_2 = Experiences("Thursday", "Less time")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.quick_read(2, 1) == "The quickest read is from Thursday"

def test_add_to_do_to_diary():
    diary = Diary()
    todo_1 = Todo("Clean bedroom")
    diary.must_do(todo_1)
    todo_2 = Todo("Exhibition")
    diary.must_do(todo_2)
    assert diary.tasks_list() == "Clean bedroom, Exhibition"
    
def test_share_contacts_for_each_entry():
    diary = Diary()
    entry = Experiences("Thursday", "Less time")
    number = Numbers("Nnemdi", "123456")
    entry.add_number(number)
    assert diary.contacts_for_each_entry(entry) == "Nnemdi: 123456"