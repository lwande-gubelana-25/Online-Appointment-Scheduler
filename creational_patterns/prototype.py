import copy

class ServicePrototype:
    def __init__(self, id, name, description, duration, price):
        self.id = id
        self.name = name
        self.description = description
        self.duration = duration
        self.price = price

    def clone(self):
        return copy.deepcopy(self)

# Demo
if __name__ == "__main__":
    original = ServicePrototype("S001", "Consultation", "General health", 30, 150)
    clone = original.clone()
    print(f"Cloned service: {clone.name}, ID: {clone.id}")
