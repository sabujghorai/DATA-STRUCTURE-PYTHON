def fractional_knapsack(item_weight , price , knapsack_weight):
    n = len(item_weight)

    items = [(item_weight[i],price[i],price[i]/item_weight[i]) for i in range(n)] 
    # Creates a list of tuples containing (weight, price, price-to-weight ratio)
    #  for every item from index 0 to n-1