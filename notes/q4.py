def generate_square_list(n):
    square_list = [i**2 for i in range(1, n+1)]
    return square_list

def print_square_list(square_list):
    for value in square_list:
        print(value, end=' ')

n = int(input("Enter a value for n: "))
squares = generate_square_list(n)

print("List of squares:")
print_square_list(squares)
