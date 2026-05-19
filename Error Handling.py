# Crate an error handlig function
# Author: Levi
#
# Version 3

'''# Cod
done = False #
#
while not done
    num = int(input("please enter your number: "))
    done = True

print(f"The number you entered is {num}.")'''

# Code that tests that a number is is entered (V2)
# Create a fumcion to call every time I ask the user
# for a number. A function is a chunk of code that dos
#
# I 'call' it by wr
'''def test_int_num(): # test_int _num ()
    done = False
    while not done:
        try: # This tries for a
            num = int(input("Please enter yoer number: "))
            doue = True

        except ValueError:
            print("That is not a valid integer.")

    return(num)

# Main routine
num_1 = test_int_num()
print(f"You entered {num_1} as your first number.")

num_2 = test_int_num()
print(f"You two entered {num_2} as your secoud number.")
print() # one way of
sum = num_1 + num_2
print(f"Your two numbers added together are {sum}")

multiply = num_1 + num_2
print(f"The numbers multiply with each other results in {multiply}")

#divisision
divide = num_1 / num_2
print(f"{num_1} divide by {num_2} is equal to {divide}.")'''

 # Version 3 Refing my code. it more pythonic.
# this will result in being able to ch
def test_int_num(question, low, high): # Qustion' is a placehol
    done = False
    error = f"Whoops, that is not an int"
    while not done:
        # print(question)
        try: # tries
            num = int(input(question))
            if num >= low and num <= high:
                done = True

            else:
                print(error)
                print()

        except ValueError:
            print(error)
    
    return(num)

# M
num_1 = test_int_num("Please enter a number between 1 and 10: ", 1, 10)
print(f"You entered {num_1}.\n")

num_2 = test_int_num("Please enter a number between 15 and 25: ", 15, 25)
print(f"You entered {num_2}.\n")

num_3 = test_int_num("Please enter a number between 30 and 40: ", 30, 40)
print(f"You entered {num_3}.\n")

sum = num_1 + num_2 + num_3
print(f"Your two numbers added together are {sum}")

multiply = num_1 * num_2 * num_3
print(f"The numbers multiply with each other results in {multiply}")

#divisision
divide = num_1 / num_2
print(f"{num_1} divide by {num_2} is equal to {divide}.")
