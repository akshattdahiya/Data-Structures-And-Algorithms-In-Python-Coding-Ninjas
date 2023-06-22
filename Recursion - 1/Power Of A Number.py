li= input().split() 
x= int(li[0]) 
n= int(li[1]) 
def power(x,n):
  if n==1: 
    return x 
  if n==0: 
    return 1 
  return x*power(x,n-1); 
print(power(x,n))
