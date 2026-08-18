def main():

    p = float(input("What do you have left in pesos?"))
    s = float(input("What do you have left in soles?"))
    r = float(input("What do you have left in reais?"))

    usd = ((p * 0.00032) + (s * 0.30) + (r * 0.19))
    print("USD:", usd)

    mxn = ((p * 0.0054) + (s * 5.07) + (r * 3.27))
    print("MXN:", mxn)

if __name__ == "__main__":
    main()
