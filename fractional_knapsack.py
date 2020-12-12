import functools
def pick_items(knapsack_items, prices, waights, capacity_of_knapsack):
    def compare(item1, item2):
        choise_factor1 = prices[item1] / waights[item1]
        choise_factor2 = prices[item2] / waights[item2]
        if choise_factor1 >= choise_factor2:
            return -1
        else:
            return 1

    final_price = 0
    knapsack_items = sorted(knapsack_items, key=functools.cmp_to_key(compare))
    print(knapsack_items)
    input("\n----press enter to pick items----")
    for i in knapsack_items:
        if capacity_of_knapsack == 0: break
        if capacity_of_knapsack - waights[i] > 0:
            final_price += prices[i]
            print(f"{i} : 100%")
            capacity_of_knapsack-=waights[i]
        else:
            portion_size = (capacity_of_knapsack * 100) / waights[i]
            print(f"{i} : {portion_size}%")
            final_price += (capacity_of_knapsack/waights[i]) * prices[i]
            capacity_of_knapsack-=(capacity_of_knapsack/waights[i])
    print("\nTotal max cost : ", final_price)
    return final_price


if __name__ == "__main__":
    knapsack_items = []
    prices = {}
    waights = {}
    n = int(input("Enter number of items : "))
    for i in range(n):
        name = input("Enter item name : ")
        knapsack_items.append(name)
        prices[name], waights[name] = int(input("Enter item price : ")), int(
            input("Enter waight : "))
    capacity = int(input("Enter capacity of Knapsack : "))
    pick_items(knapsack_items, prices, waights, capacity)
