# This is the correct solution to the problem:

def spooky_word(n):
    return "sp" + "o" * n + "ky"

# Input
n = int(input())

# Output
print(spooky_word(n))



#The below code is what I originally tried to answer the question with:



# We are creating a function that will replace S with an integer that is at least equal to 2 but not more than 20.

def replace_s(S):

    # Ask user for input, we are accepting an integer
    S = input('Please input a number between 2 and 20: ').int()
    # It has to be equal to greater than 2
    # If it is less than 2, we will ask the user to input a number that is equal or greater than 2
    if S < 2:
        input('Please input a number that is equal to or greater than 2: ')
    # If is greater than 20, we will ask the user to input a number that is equal to or less than 20
    elif S > 20:
        input('Please input a number that is equal to or less than 20: ')
    else:
        for value in S:
            print('sp' + value + 'ky')
    # Output is the word spooky with the number of Os as input by the user
