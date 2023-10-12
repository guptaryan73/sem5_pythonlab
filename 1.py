name = "john"
age = 20
message = "My name is " + name + " and I am " + str(age) + " years old."
print (message)

def is_Palindrome(input_str):
    clean_str = input_str.replace(" ", "").lower()
    return clean_str == clean_str[::-1]

text = "hi"
result = is_Palindrome(text)
print (result)