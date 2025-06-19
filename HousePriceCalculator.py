houses = []

def add_house():
    while True:
        price_input = input("Enter house price (or 'n' to finish): ")
        if price_input.lower() == 'n':
            break
        try:
            price = float(price_input)
            if price >= 0:
                houses.append(price)
            else:
                raise ValueError("Price cannot be negative.")
        except ValueError:
            print("Invalid input. Please enter a valid number or 'n' to finish.")

def calculate_average_price():
    if not houses:
        raise ValueError("No houses available to calculate average price.")
    average_price = sum(houses) / len(houses)
    return f"{average_price:.2f}"

def main():
    try:
        neighborhood = input("Enter the neighborhood name: ")

        add_house()

        count_houses = len(houses)
        sum_price = sum(houses)
        highest_price = max(houses)
        lowest_price = min(houses)

        print(f"You have entered {count_houses} houses, the sum is ${sum_price:.2f}, "
              f"the highest price is ${highest_price:.2f}, and the lowest price is ${lowest_price:.2f}.")

        print(f"The average house price in {neighborhood} is ${calculate_average_price()}")
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()