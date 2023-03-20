#Types of Arguments
#In python, there are three types of arguments
#   1. Positional Arguments: arguments that can be called by their position in the function definition.
#   2. Keyword Arguments: arguments that can be called by their name.
#   3. Default Arguments: arguments that are given default values.
#
#Note: Python calculates from top to bottom

# Example: 
# Here, we are calculating the taxi price using these parameters: miles_to_travel, rate, discount.

# Positional Argument
def calculate_taxi_price(miles_to_travel,rate,discount):
    print(miles_to_travel * rate - discount)

calculate_taxi_price(100,10,5)

# Keyword Argument
def calculate_taxi_price(miles_to_travel,rate,discount):
    print(miles_to_travel * rate - discount)

calculate_taxi_price(rate = 10, discount=5, miles_to_travel=100)

# Default Arguments
def calculate_taxi_price(miles_to_travel, rate, discount = 10):
  print(miles_to_travel * rate - discount )
  
calculate_taxi_price(10,0.5)
    # Even if we do not include discount in the argument, it is default to 10. 
    # Therefore, in theory, it works as calculate_taxi_price(10,0.5,10)