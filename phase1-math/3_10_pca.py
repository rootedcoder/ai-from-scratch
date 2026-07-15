import numpy as np

def pca(data, n_components):
  data = np.array(data, dtype=float)
  
  mean = data.mean(axis=0)
  print("Mean: ", mean)

  centered = data - mean # broadcasting from 1.3.8
  print("Centered:\n", centered)

  cov_matrix = (centered.T @ centered) / (len(data) - 1) 
  print("Covariance Matrix:\n", cov_matrix)

  eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
  print("Eigen values: ", eigenvalues)
  print("Eigen Vectors:\n", eigenvectors)

  order = np.argsort(eigenvalues)[::-1] # sort largest to smallest
  print("Order: ", order)

  top_components = eigenvectors[:, order[:n_components]]
  print("Top Components:\n", top_components)

  reduced = centered @ top_components
  print("Reduced:\n", reduced)

  return reduced, eigenvalues[order]

data = [
  [2, 3],
  [3, 4],
  [4, 5],
  [5, 6]
]
print(pca(data, n_components=1))