"""
This is week 1 of the Python Bootcamp for Data assignment. All of your questions 
for this week will come commented out. 
To pass, all automated testing of your inputs have to pass their tests. 
"""

# The following exception is breaking the function. You haven't seen
# functions yet, but concentrate in fixing the exception so that: 
# * the exception doesn't happen
# * The exception_message is correctly defined as a string
def create_message():
    try:
        exception_message = "This message is broken " + 1
    except RuntimeError:
        raise 
    return exception_message

# Make single_string use both the `name` and `greeting` variables to 
# create a single string. The single_string should be a string and not a `None`
name = "Monday"
greeting = "Hello students!"
single_string = None

# Use the following text to create a string and assign it to quoted_string:
# Sometimes you can use a ' character to denote minutes or " for seconds
quoted_string = None

# The current condition does not evaluate correctly. Python has truthy values
# and dictionaries is one of them. Update the code so that has_contacts will
# evaluate to True instead of False
contacts = {}
if contacts:
    has_contacts = True
else:
    has_contacts = False

# Use the `apples` and `cost` variables in the numbers_string variable
apples = 4
cost = 7.3
numbers_string = None

