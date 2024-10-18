import random
import my_module
import random_float


pi = my_module.my_favourite_num

random_int = random.randint(0, 10)
print(f"{random_int} and the Value Pi which is imported from my_module is {pi} " )

#RANDOM FLOAT NUMBER

float_random = random_float.random_number_float * 10
print(f"{float_random}")