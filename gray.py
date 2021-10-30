
def main():
    mode = input("Press 1 to convert from binary to Gray\nPress 2 to convert from Gray to binary\n")
    if mode == "1":
        number = input("Enter binary to convert to Gray code: ")
        if check_input(number):
            gray = convert_to_gray(number)
            print(gray)
    elif mode == "2":
        number = input("Enter Gray code to convert to binary: ")
        if check_input(number):
            binary = convert_to_binary(number)
            print(binary)
    else:
        print(f"{mode} is not a valid input.")

def check_input(number):
    for bit in number:
        if bit != "0" and bit != "1":
            print(f"{number} is not a valid input.")
            return False
    return True

def convert_to_gray(number):
    gray = []
    gray.append(number[0])
    i = 1

    while i < len(number):
        new_bit = ''
        if (number[i] == '0' and number[i-1] == '0') or (number[i] == '1' and number[i-1] == '1'):
            new_bit = '0'
        else:
            new_bit = '1'
        gray.append(new_bit)
        i += 1

    gray = ''.join(gray)
    return gray

def convert_to_binary(number):
    binary = []
    binary.append(number[0])
    i = 1

    while i < len(number):
        new_bit = ''
        if number[i] == '0':
            new_bit = binary[i-1]
        else:
            if binary[-1] == '1':
                new_bit = '0'
            else:
                new_bit = '1'
        binary.append(new_bit)
        i += 1

    binary = ''.join(binary)
    return binary

main()
