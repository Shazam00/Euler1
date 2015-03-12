from math import factorial
def problem24(n):
  """ 
  Determine the nth lexicographic 
  permutation of 0123456789 
  """
  answer = ""
  digits = [0,1,2,3,4,5,6,7,8,9]
  for i in range(9,-1,-1):
    ifact = factorial(i)
    digit = (n-1) / ifact
    answer += str(digits.pop(digit))
    n = n - (digit * ifact)
  return answer
problem24(1000000)
