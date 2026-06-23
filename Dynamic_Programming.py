def knapsack_recursive(weights , values , knapsack_weight , n): # n is the items here
    if(n == 0 or knapsack_weight == 0):
        return 0
    