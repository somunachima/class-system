class Experiences:
    def __init__(self, date, content):
        self.date = date
        self.content = content
        self.all_contacts = []

    def word_count(self):
        words = self.content.split()
        return len(words)
    
    def add_number(self, number):
        self.all_contacts.append(number)

    def list_numbers(self):
        contacts = []
        for contact in self.all_contacts:
            contacts.append(contact.name + ": " + contact.contact)
        return " ".join(contacts)