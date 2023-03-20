# Create calculate_insurance_cost() function below: 
def calculate_insurance_cost(name,age,sex,bmi,num_of_children,smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print("The estimated insurance cost for " + name + " is $" + str(estimated_cost) + ".")
  return estimated_cost

# Calculate difference between insurance cost of any two individuals
def insurance_cost_difference(name1,cost1,name2,cost2):
  difference = abs(cost1 - cost2)
  print("The difference in insurance cost between " + name1 + " and " + name2 + "is $" + str(difference))
  return difference

# Estimate Maria's insurance cost
maria_insurance_cost = calculate_insurance_cost("Maria",28,0,26.2,3,0)

# Estimate Omar's insurance cost 
omar_insurance_cost = calculate_insurance_cost("Omar",35,1,22.2,0,1)
omar_maria_cost_difference = insurance_cost_difference("Omar",omar_insurance_cost,"Maria",maria_insurance_cost)

