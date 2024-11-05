import numpy as np
from itertools import combinations

# Calculate support for an itemset
def calculate_support(dataset, itemset):
    return sum(1 for transaction in dataset if itemset.issubset(transaction))

# Generate candidate itemsets of a specific length
def generate_candidates(prev_freq_itemsets, length):
    return {frozenset(i | j) for i in prev_freq_itemsets for j in prev_freq_itemsets if len(i | j) == length}

# Apriori Algorithm
def apriori(dataset, min_support):
    dataset = list(map(set, dataset))
    # Step 1: Find frequent 1-itemsets
    items = {frozenset([item]) for transaction in dataset for item in transaction}
    freq_itemsets = {item for item in items if calculate_support(dataset, item) >= min_support}
    all_freq_itemsets = [freq_itemsets]
    supports = {item: calculate_support(dataset, item) for item in freq_itemsets}
    
    # Step 2: Generate larger itemsets
    k = 2
    while freq_itemsets:
        candidates = generate_candidates(freq_itemsets, k)
        freq_itemsets = {item for item in candidates if calculate_support(dataset, item) >= min_support}
        supports.update({item: calculate_support(dataset, item) for item in freq_itemsets})
        
        if freq_itemsets:
            all_freq_itemsets.append(freq_itemsets)
        k += 1
    
    return all_freq_itemsets, supports

# Generate association rules from the last frequent itemset level
def generate_rules(freq_itemsets, supports, min_confidence):
    rules = []
    for itemset in freq_itemsets[-1]:
        for i in range(1, len(itemset)):
            for antecedent in map(frozenset, combinations(itemset, i)):
                consequent = itemset - antecedent
                confidence = supports[itemset] / supports[antecedent]
                if confidence >= min_confidence:
                    rules.append((antecedent, consequent, supports[itemset], confidence))
    return rules

# Example Usage
if __name__ == "__main__":
    # Dataset and user input
    dataset = [{1, 2, 4}, {2, 3, 5}, {1, 2, 3, 5}, {2, 5}]
    min_support_percent = float(input("Enter minimum support percentage: "))
    min_confidence_percent = float(input("Enter minimum confidence percentage: "))
    
    # Calculate minimum support and confidence
    min_support = (min_support_percent / 100) * len(dataset)
    min_confidence = min_confidence_percent / 100
    
    # Run Apriori algorithm
    freq_itemsets, supports = apriori(dataset, min_support)
    
    # Print frequent itemsets with their support
    print("Frequent Itemsets:")
    for level, itemsets in enumerate(freq_itemsets, 1):
        print(f"\nLevel {level}:")
        for itemset in itemsets:
            print(f"{set(itemset)}: Support = {supports[itemset]}")
    
    # Generate and print association rules from the last level
    rules = generate_rules(freq_itemsets, supports, min_confidence)
    if rules:
        print("\nAssociation Rules:")
        for antecedent, consequent, support, confidence in rules:
            print(f"{set(antecedent)} => {set(consequent)}: Support = {support}, Confidence = {confidence:.2%}")
    else:
        print("\nNo association rules generated.")
