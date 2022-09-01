#function generator

def function_generator(function_name):
  return lambda x : function_name(x) 

my_print = function_generator(print)
my_max = function_generator(max)
my_sorted = function_generator(sorted)
my_bool = function_generator(bool)

my_print("I love you")


my_max((23,56,89,45,12))

my_sorted((1,3,56,99,0))