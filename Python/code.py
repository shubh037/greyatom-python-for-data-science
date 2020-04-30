# --------------
# Code starts here

# Create the lists 
class_1=["geoffrey hinton","andrew ng" ,"sebastian raschka","yoshua bengio"]
class_2=["hilary mason","carla gentry","corinna cortes"]
# Concatenate both the strings
new_class = class_1 + class_2
print(new_class)

# Append the list
new_class.append("peter warden")
# Print updated list
print(new_class)

# Remove the element from the list
new_class.remove("carla gentry")
# Print the list
print(new_class)


# Create the Dictionary
courses = {"maths":65,"english":70,"history":80,"french":70,"science":60}
print(courses)
total = 65+70+80+70+60
percentage_1=total/500
percentage = percentage_1*100
print(total)
# Insert percentage formula

# Print the percentage
print(percentage)



# Create the Dictionary
mathematics = {"geoffrey hinton":78,"andrew ng":95,"sebastian raschka":65,"yoshua":50,"hilary mason":70,"corninna":66,"peter":75}
print(mathematics)
topper = max(mathematics,key = mathematics.get)
print(topper)




# Given string
topper = "andrew ng"


# Create variable first_name 
first_name = (topper.split()[0])
print(first_name)
# Create variable Last_name and store last two element in the list
Last_name = (topper.split()[1])
print(Last_name)
# Concatenate the string
full_name = Last_name + " " + first_name
# print the full_name

# print the name in upper case
certificate_name = full_name.upper()
# Code ends here


