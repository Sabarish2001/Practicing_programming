def calculate_fibonacci(number):
  
  if number == 0:
    return 0
  elif number == 1 or number == 2:
    return 1
  else:
    return calculate_fibonacci(number - 1) + calculate_fibonacci(number - 2)
  

n = int(input("Please enter the number till you want to calculate fibonacci series for :"))
for i in range(0,n):
  print(calculate_fibonacci(i))
