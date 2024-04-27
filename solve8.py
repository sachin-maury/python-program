import numpy as np
import matplotlib.pyplot as plt

def k_means(data, k, max_iterations=100):
    centroids = data[np.random.choice(range(len(data)), k, replace=False)]
    
    for _ in range(max_iterations):
        labels = np.argmin(np.linalg.norm(data - centroids[:, np.newaxis], axis=2), axis=0)
        new_centroids = np.array([data[labels == i].mean(axis=0) for i in range(k)])
        
        if np.all(centroids == new_centroids):
            break
        
        centroids = new_centroids

    return centroids, labels

if __name__ == "__main__":
    # Generate synthetic data with three clusters
    np.random.seed(42)
    data1 = np.random.normal(loc=[2, 2], scale=[0.5, 0.5], size=(100, 2))
    data2 = np.random.normal(loc=[7, 7], scale=[0.5, 0.5], size=(100, 2))
    data3 = np.random.normal(loc=[12, 2], scale=[0.5, 0.5], size=(100, 2))
    data = np.concatenate([data1, data2, data3])

    # Number of clusters
    k = 3

    # Apply K-means clustering
    centroids, labels = k_means(data, k)

    # Plot the results
    plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis', alpha=0.7)
    plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='x', s=100, label='Centroids')
    plt.title('K-means Clustering')
    plt.legend()
    plt.show()
