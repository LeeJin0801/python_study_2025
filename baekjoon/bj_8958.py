num = int(input())
case_lists = []
for i in range(num):
  case_lists.append(input())

for j in range(len(case_lists)):
  input_str = case_lists[j]
  processed_list = []

  for k in range(len(input_str)):
    processed_list.append(input_str[k])

  #print(processed_list)
  #print(input_str.split('X'))
  no_x_list = input_str.split('X')
  #print(no_x_list)


  sum = 0
  for i in range(len(no_x_list)):
    if(no_x_list[i] != ''):
      #print(len(no_x_list[i]), end = ', ')
      sum += (1 + len(no_x_list[i])) * (len(no_x_list[i])/2)
    
  print(int(sum))
  