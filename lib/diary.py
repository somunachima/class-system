class Diary:
    def __init__(self):
        self.entries = []
        self.tasks_to_do = []

# As a user
# So that I can record my experiences
# I want to keep a regular diary

    def add(self, experiences):
        self.entries.append(experiences)

    
# As a user
# So that I can reflect on my experiences
# I want to read my past diary entries

    def list(self):
        read_all = []
        for entry in self.entries:
            read_all.append(entry.date + ": " + entry.content)
        return ", ".join(read_all)
    
# As a user
# So that I can reflect on my experiences in my busy day
# I want to select diary entries to read based on how much time I have and my reading speed
# reading speed = 1 word per mins
# time available = 2 mins
# words they have time to read = 2 words

    def quick_read(self, time_available, reading_speed):
        word_limit = time_available * reading_speed
        short_entries = {}
        for entry in self.entries:    
            if entry.word_count() <= word_limit:
                short_entries[entry] = entry.word_count()
        best_read = sorted(short_entries.items(), key=lambda item: item[1])[-1][0]
        return f"The quickest read is from {best_read.date}"
# As a user
# So that I can keep track of my tasks
# I want to keep a todo list along with my diary

    def must_do(self, task):
        self.tasks_to_do.append(task)

    def tasks_list(self):
        read_to_do = []
        for task in self.tasks_to_do:
            read_to_do.append(task.content)
        return ", ".join(read_to_do)

# As a user
# So that I can keep track of my contacts
# I want to see a list of all of the mobile phone numbers in all my diary entries

    def contacts_for_each_entry(self, entry):
        # return self.list_numbers()
        return entry.list_numbers()
