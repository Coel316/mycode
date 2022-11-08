#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   print() - display data to std out"""

# below is a function containing our code
def main():

    # pause the program and wait for the user to provide input
    user_input_name = input("Please enter your name: ")
    # pause the program and wait for user to enter day of week
    user_input_dayOfWeek = input("Please enter day of week: ")

    # display the input back to the user.
    print("Hello, ",  user_input_name, "! Happy ", user_input_dayOfWeek, "!")
    
# this calls main
main()

