def main():

    def calculate(a, b):
        answer = a + b
        print(f"{a} + {b} = {answer}")

    num1 = 10
    num2 = 15

    calculate(num1, num2)

    def avarge_value(a, b, c):
        answer = (a + b + c) / 3
        print(f"The avarage value is {answer}")

    num3 = float(input("enter first number: "))
    num4 = float(input("enter the second number: "))
    num5 = float(input("enter the third number: "))

    avarge_value(num3, num4, num5)

if __name__=="__main__":
    main()
