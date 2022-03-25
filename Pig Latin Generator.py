user_input = input("Enter word to be translated:\n")
#change_1
vowels = ['a','e','i','o','u']
def translate(user_input): 
    first = user_input[0]
#change_2
    if first in vowels: 
         user_input = user_input.lower()
         user_input += "way" 
         return user_input
    else: 
        user_input = user_input.lower()
#change_3
        for letter in user_input:
            if letter in vowels:
                index_value = user_input.index(letter)
                break
#change_4
        user_input = user_input[index_value:] +user_input[:index_value]+ "ay" 
        return user_input 

print(translate(user_input))
