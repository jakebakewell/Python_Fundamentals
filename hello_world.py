# x = "Hello Python"
# print(x)
# y = 42
# print(y)

#number = 15
#name = "Zen"
#print("My name is", number)
#print("My name is " + name)

#first_name = "Zen"
#last_name = "Coder"
#age = 25
#print(f"My name is {first_name} {last_name} and my age is {age} years old.")

#first_name = "Zen"
#last_name = "Coder"
#age = 25
#print("My name is {} {} and my age is {} years old.".format(first_name, last_name, age))
#print("My name is {} {} and my age is {} years old.".format(age, first_name, last_name))

#hw = "Hello %s" % "world"
#py = "I love Python %d" % 3
#print(hw, py)

#name ="Zen"
#age = 25
#print("My name is %s and my age is %d years old" % (name, age))

#string.upper(): returns a copy of the string with all the characters in uppercase.

#string.lower(): returns a copy of the string with all the characters in lowercase.

#string.count(substring): returns number of occurrences of substring in string.

#string.split(char): returns a list of values where string is split at the given character. Without a parameter the default split is at every space.

#string.find(substring): returns the index of the start of the first occurrence of substring within string.

#string.isalnum(): returns boolean depending on whether the string's length is > 0 and all characters are alphanumeric (letters and numbers only). Strings that include spaces and punctuation will return False for this method. Similar methods include .isalpha(), .isdigit(), .islower(), .isupper(), and so on. All return booleans.

#string.join(): returns a string that is all strings within our set (in this case a list) concatenated.

#string.endswith(substring): returns a boolean based upon whether the last characters of string match substring.

# 1. TASK: print "Hello World"
print("Hello World")
# 2. print "Hello Noelle!" with the name in a variable
name = "Jake"
print("Hello", name)	# with a comma
print("Hello " + name)	# with a +
# 3. print "Hello 42!" with the number in a variable
number = 15
numberString = "15"
print("Hello", number)	# with a comma
print("Hello " + numberString)	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "ramen"
fave_food2 = "fried chicken"
print("I love to eat {} and {}.".format(fave_food1, fave_food2)) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}.") # with an f string