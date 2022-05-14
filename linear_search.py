def linear_search(my_list, num_to_search):
  
  list_len = len(my_list)
  indices = []
  for each_index in range(list_len):
    if my_list[each_index] == num_to_search:
      indices.append(each_index)
      
  return indices

res = linear_search([1,2,3,4,5,6], 5)
print(res)
