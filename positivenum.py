
def print_positive_numbers(lst):
  
    positive_lst = []
    
    for num in lst:
        if num > 0:
            positive_lst.append(num)
   
    print(positive_lst)


user_input = input("Enter a list of numbers separated by commas: ")

num_list = [int(num) for num in user_input.split(",")]

print("Output:", end=" ")
print_positive_numbers(num_list)
