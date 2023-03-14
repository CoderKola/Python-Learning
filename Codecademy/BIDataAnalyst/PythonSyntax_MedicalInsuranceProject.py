# Person's Health Factors
age = 28                # age: age of the peron in years
sex = 0                 # sex: 0 for female, 1 for male 
bmi = 26.2              # bmi: individual's body mass index
num_of_children = 3     # num_of_children: the number of childern the individual has 
smoker = 0              # smoker: 0 for non-smoker, 1 for a smoker

# Insurance Cost
insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500     #Formula was given
print("This person's insurance cost is", str(insurance_cost), "dollars.")

# Age Factor 
age += 4
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
print("This person, who is four years older, has an insurance insurance cost of", new_insurance_cost, "dollars.")

# Change in Insurance Cost
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("Display 1: People who are four years older have estimated insurance costs that are", str(change_in_insurance_cost), "dollars different.")
print("Display 2: The change in cost of insurance after increasing the age by 4 years is " + str(change_in_insurance_cost) + " dollars.")

# bmi Factor
age = 28
bmi += 3.1

new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in estimated insurance cost after increasing bmi by 3.1 is", change_in_insurance_cost, "dollars.")

# Male vs. Female Factor
bmi = 26.2
sex = 1

new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in estimated cost for being male instead of female is "+ str(change_in_insurance_cost) + " dollars.")
print("This means that men tend to have lower medical costs on average than women.")

# Smoking Factor
sex = 0
smoker = 1 

new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in estimated insurance cost for being a smoker is " + str(change_in_insurance_cost) + " dollars.")

# bmi Factor
smoker = 0
num_of_children = 0

new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in insurance cost when you go from three to no-children is ", change_in_insurance_cost, "dollars.")