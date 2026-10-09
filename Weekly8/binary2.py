def main():
    print("Welcome!")

    valid_bits = ["0", "1"]
    while True:
        u_binary_num = input("Enter a binary number: ")
        valid_chars = 0
        for user_bit in u_binary_num:
            if user_bit in valid_bits:
                valid_chars += 1
        if valid_chars == len(u_binary_num):
            break
        else:
            print("Invalid number.")
    binary_to_decimal(u_binary_num)

def binary_to_decimal(binary_num):
    decimal_num = 0
    for bit in binary_num:
        decimal_num = (decimal_num * 2) + int(bit)
    print(decimal_num)



if __name__=="__main__":
    main()
