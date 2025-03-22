import time
import math
def x(number, milliseconds):
    time.sleep(milliseconds / 1000) 
    return math.sqrt(number)

number = int(input("Enter a number: "))
milliseconds = int(input("Enter delay in milliseconds: "))
delayed_result = x(number, milliseconds)
print(f"Square root of {number} after {milliseconds} milliseconds is {delayed_result}")
