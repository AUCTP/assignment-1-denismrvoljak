import random


# Defining user choice to make the app interactive
def get_user_choice():
    print("======Cafeterie Simulation======")
    print("Choose an option:")
    print("1. Use random weapon")
    print("2. Pick a weapon on your own")
    print("3. End the game")
    choice = int(input())
    return choice


def simulate_customers(inventories, sales):
    customer_arrivals = random.randint(1, 250)

    i = 1

    while i < customer_arrivals:
        is_purchase = random.choice([1, 0])

        if is_purchase:
            item_index = random.choice([0, 1, 2])
            if inventories[item_index] >= 1:
                # item_purchased = items[item_index]
                item_price = prices[item_index]
                inventories[item_index] = inventories[item_index] - 1
                sales.append(item_price)

        i += 1


def process_sales(sales):
    total_sales = sum(sales)
    return total_sales


def generate_report(sales, items, inventories):
    print(f"Total sales for the day are: {process_sales(sales)}")

    for i in range(0, len(items)):
        print(f"End of day inventory for {items[i]} is {inventories[i]}")


# simulation
# Some example items - feel free tho change them
items = ["Sandwich", "Salad", "Cake"]
prices = [65, 45, 50]
inventories = [100, 50, 100]

sales = []


print(inventories)
print(sales)
simulate_customers(inventories, sales)
generate_report(sales, items, inventories)

print(inventories)
print(sales)
