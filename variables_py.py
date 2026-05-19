# Demonstrate how varaiables are 



#   store a string
#   store different types of numbers
#   Assign the value of varaiables to ano
#   

# store a string
greeting = "Hello World"
print(greeting)
random_variables = "7"
print(random_variables)

# Store different types of numbers
#
num_1 =7
print(f"the varibles called num_1 which contains {num_1} is a {type(num_1)}")

#stores a float numbers (a nr with a decimal)
num_2 = 9.5
print(type(num_2))
print(f"the varibles called num_2 which contains {num_2} is a {type(num_2)}")

# Assign the value of one variable to another
num_2 = greeting
print(f"num_2 has the value of {greeting}.")
print(f"num_2 has now becomea {type(num_2)}")

# Do calculations with variables and store the results
# Create a new/reas
num_1 = 5
num_2 = 18

# Add up number
sum = 5+18 #not good practice
print(sum)

sum = num_1 + num_2
print(sum)
#t

# Add up string
Sum_string1 = "18"
Sum_string2 = "5" 

Sum_string_total = Sum_string1 + Sum_string2
print(Sum_string_total)
# Total prints as 185.
#It is text

#Print formatting
#f standsfor 'format'.
#Insert the value of 
#
print(f"My calclation for adding {num_1} and {num_2} together is {sum}.")


print("My calculation for concatenating {} and {} is {}".format(Sum_string1,Sum_string2,Sum_string_total))

# Greet someone
name = "Levi"
print("Kia ore, my name is ",name)
print("Kia ora my name is {}.".format(name))
print("Kia ora, my name is {name}.")