# import random

# def practice(word_list):
#   word = word_list[random.randint(0, len(word_list)-1)]
#   word_guessed = ['_' for x in range(len(word))]
#   num_letters = len(set(word))

#   print(word_guessed, word, num_letters)

# practice(['brain', 'trainwaa', 'sla'])

# string = 'trainwaaa'
# result = string.index('a')
# print(result)

# word_guessed = ['_', '_', '_', '_', '_']
# def stuff(letter, word):
#   index_position = 0

#   while index_position >= 0:
#     index_position = word.index(letter, index_position)
#     word_guessed[index_position] = letter
#     index_position += 1

# stuff('a', 'aadva')
# print(word_guessed)

index_position = 'hello'.index('e', 2)

print(index_position)


  

