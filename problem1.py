import numpy as np 
def create_matrix (N, M):
    
   A = np.zeros ([N,M])

   count = 1 
   for i in range (0, N):
      for j in range(0, M):
         A[i,j] = count 
         count +=1

   return A

def sort_odd_rows (A):

   N, M = A.shape[0], A.shape[1]

   for i in range (0, N):
      if i % 2 == 1:
         X = A[i,:]
         Y = sorted (X)
         Z = [ int(Y[M-j]) for j in range(1, M+1)]
         A[i,:] = Z 
   
   return A


def center_matrix (N, M):
   # At present does not work for matrix smaller than 3 x 3

   A =  np.zeros ([N, M])
   for i in range (0, int(N/2)):
      for j in range (i, int(M/2)):
         A[i,j] = int(N/2) -i      
   
      for j in range (0, i):
         A[i,j] = A[j,i]    

   m = int (M/2)
   n = int (N/2)

   for i in range (0, n):
      for j in range (0, m):
          A[i,m+j] =  A[i, m-j-1]

 
   for i in range (n, N):
      for j in range (0, M):
         A[i,j]  = A [N-i-1,j]
   return A  


if __name__ == "__main__":

   A = create_matrix (3, 3)

   print(A) 
  
   B = sort_odd_rows (A) 
   print(B)
   print("===")
   C = center_matrix (8,8)
   print(C)
   

