def knapsack_recursive(weights , values , knapsack_weight , items): # n is the items here
    if(items == 0 or knapsack_weight == 0):
        return 0
    
    if weights[items-1] > knapsack_weight :
        return knapsack_recursive(weights , values , knapsack_weight , items - 1)
    
    else:
        include = values[items - 1] + knapsack_recursive(weights , values , knapsack_weight - weights[items-1] , items - 1)

    exclude = knapsack_recursive(weights , values , knapsack_weight , items - 1)

    return max(include , exclude)
