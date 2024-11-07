import random 

#define the game function
def game(number_try):
#for loop to numbers of try
    for i in range(number_try):
#random number from 9 to 100 
        divisor = random.randint(9,100)
#random number from 1 to 9
        dividend = random.randint(1,9)
        print (f"{divisor} / {dividend}")
#calculate the quotient and remainder
        quotient = divisor/dividend
        remainder = divisor % dividend
#Compare the quotient and remainder with user inputs
        user_result_quotient = float(input("Enter the quotient: "))
        user_result_remainder = float(input("Enter the remainder: "))
        if (abs (user_result_quotient - quotient) <0.001) and user_result_remainder == remainder:
            print("Correct.")
        else: print("Incorrect.")
        

game(5)