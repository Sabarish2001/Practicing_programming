def calculate_sum_n_numbers(number):
  
  if n == 1:
    return 1
  else:
    return number + calculate_sum_n_numbers(number - 1)
  
res = calculate_sum_n_numbers(10)
print(res)
