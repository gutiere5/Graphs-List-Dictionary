
class State:
    def __init__(self, name, capital, area, population):
        self.name = name
        self.capital = capital
        self.area = area
        self.population = population

    def __str__(self):
        return (f"State: {self.name}\n"
                f"Capital: {self.capital}\n"
                f"Area: {self.area} sq km\n"
                f"Population: {self.population}")

state_info = {
    "California": State("California", "Sacramento", 423967, 39538223),
    "Texas": State("Texas", "Austin", 695662, 29145505),
    "Florida": State("Florida", "Tallahassee", 170312, 21538187),
    "New York": State("New York", "Albany", 141297, 20201249)
}

def main():
    state_name = input("Enter the state name: ")
    state = state_info.get(state_name)

    if state:
        print(state)
    else:
        print("State not found in the database.")

if __name__ == "__main__":
    main()