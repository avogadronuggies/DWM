import numpy as np
import pandas as pd

def calculate_pagerank(adj_matrix, num_iter, damping_factor, num_nodes):
    # Initialize PageRank values equally
    pagerank = np.ones(num_nodes) / num_nodes
    print(f"Iteration 0: {pagerank}")

    # DataFrame to track PageRank values over iterations
    history = pd.DataFrame(index=[f"Page {chr(65 + i)}" for i in range(num_nodes)],
                           columns=[f"Iteration {i}" for i in range(num_iter + 1)])
    history['Iteration 0'] = np.round(pagerank, 2)

    # Main PageRank iteration loop
    for iter in range(1, num_iter + 1):
        new_pagerank = np.zeros(num_nodes)

        # Calculate new PageRank for each page
        for i in range(num_nodes):
            incoming_links = np.where(adj_matrix[:, i] > 0)[0]
            incoming_sum = sum(pagerank[j] / np.sum(adj_matrix[j]) for j in incoming_links if np.sum(adj_matrix[j]) > 0)
            new_pagerank[i] = (1 - damping_factor) + damping_factor * incoming_sum

        pagerank = new_pagerank
        history[f'Iteration {iter}'] = np.round(pagerank, 2)
        print(f"Iteration {iter}: {pagerank}")

    # Display final PageRank and history table
    print("\nFinal PageRank:", pagerank)
    print("\nPageRank History:\n", history)

# User inputs
num_nodes = int(input("Enter number of pages: "))
print("Enter the adjacency matrix (one row per line):")
adj_matrix = np.array([list(map(int, input().split())) for _ in range(num_nodes)])
num_iter = int(input("Enter number of iterations: "))
damping_factor = float(input("Enter damping factor (0 to 1): "))

calculate_pagerank(adj_matrix, num_iter, damping_factor, num_nodes)
