import random
from os.path import join
# ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
#     ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     digits = '0123456789'
#     hexdigits = '0123456789abcdefABCDEF'
#     octdigits = '01234567'
#     printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
#     punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
#     whitespace = ' \t\n\r\x0b\x0c'


digits = ('0','1','2', '3', '4', '5', '6', '7', '8', '9')
punctuation = ('!','"' ,'#', '$' ,'%','& ','(',')','*','+','-','.','/',':',';','<','=','>','?','@' ,'[',']','^','_','{','|','}' ,'~')
ascii_lowerUperCase = ('a','b', 'c' ,'d', 'e' ,'f', 'g', 'h', 'i', 'j' ,'k', 'l' ,'m' ,'n' ,'o' ,'p' ,'q' ,'r' ,'s' ,'t' ,'u' ,'v ','w ','x','y ','z','A ','B','C ','D ','E ','F', 'G ','H ','I ','J ','K ','L', 'M ','N ','O ','P', 'Q ','R ','S' ,'T' ,'U ','V ','W ','X ','Y ','Z')



print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

pasword_list = []

for char in range(1, nr_letters + 1):
    pasword_list += random.choice(ascii_lowerUperCase)

for char in range(1, nr_symbols + 1):
    pasword_list += random.choice(punctuation)

for char in range(1, nr_numbers + 1):
    pasword_list += random.choice(digits)

random.shuffle(pasword_list)
for i in pasword_list:
    password = ''.join(pasword_list)
    # password += i or use this one
print(f"Your password is: {password}")