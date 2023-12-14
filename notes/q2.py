def count_set_bits(num):

    binary_representation = bin(num)[2:]

    set_bits_count = binary_representation.count('1')

    return set_bits_count

number = int(input("take a positive number"))
result = count_set_bits(number)

print(f"{result}")
