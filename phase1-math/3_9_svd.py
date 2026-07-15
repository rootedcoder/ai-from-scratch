import numpy as np

def svd_computation(M):
  Numpy_M = np.array(M)
  
  U, S, Vt = np.linalg.svd(Numpy_M)
  print("Singular Values: ", S)
  print("U:\n", U)
  print("Vt:\n", Vt)

  # Reconstruct M from U, S, Vt to confirm they multiply back to the original
  reconstructed = U @ np.diag(S) @ Vt
  print("Reconstructed:\n", reconstructed)

  return U, S, Vt, reconstructed 

M = [[3, 0], [0, 1]]
svd_computation(M)

M2 = [[4, 0], [3, -5]]
U, S, Vt, reconstructed = svd_computation(M2)

S_reduced = S.copy()
S_reduced[-1] = 0
approx = U @ np.diag(S_reduced) @ Vt
print("Approximation using only the largest singular value:\n", approx)