class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats(): #or if not self.open_seats()
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

Flight = Flight(3)

people = ["Harry","Ron", "Aime", "Ginny"]

for person in people:
    success = Flight.add_passenger(person)

    if success:
        print(f"Added {person} to flight succefully.")
    else: 
        print(f"No available setas for {person}")
        
    
    
