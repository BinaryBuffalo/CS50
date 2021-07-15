class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    def open_seats(self):
        return self.capacity - len(self.passengers)

f = Flight(3)
people = ["dan", "pam", "jon", "epstein"]
for person in people:
    success = f.add_passenger(person)
    if success:
        print(f"Added {person}")
    else:
        print(f"Deny")