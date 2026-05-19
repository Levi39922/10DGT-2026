# Demonstrate how to use an IF statement
#Author: lEVI
# 1 May 2026
# Version 1

# !TODO: Create a program that will ask the user whether
# they like coffee or not. If they do not like coffee
#I will try to persude 

#checking whether you like coffee and stores the answer in
# a variable.
like_coffee = input("Do you like coffee? ")
#print(like_coffee)
keep_going = ""
while keep_going == "":

if like_coffee == " yes":
    print("that is great! I like coffee too!")

if like_coffee == " no":
    print("You are missing out. why give it a try?")

elif like_coffee == "no":
    print("You are missing out. why give it a try?")

else:
    print("try againg.")

keep_going = ""
while keep_going == "":
    print("Looping")
    print("still looping")
    keep_going = input("Again?")

print("All done.")
