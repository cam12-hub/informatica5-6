def main():
    transistors = 17800000000
    years = int(input("How many years into the future?"))
    transistors *= round(2** (years/2))
    print(f"{transistors:,}")

if __name__ == "__main__":
    main()
