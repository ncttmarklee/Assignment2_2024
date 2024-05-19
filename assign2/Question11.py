def fact(x):
      result = 1
      for i in range(2, x+ 1):
            result *= i
      return result

def perm(n,r):
     result = 1
     for i in range(n,n-r,-1):
           result *= i
     return result
