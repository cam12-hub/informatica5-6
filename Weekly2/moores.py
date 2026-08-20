def main():
    transitors = 17800000000
    years = int(input("How many years into the future?"))
    transitors *= round(2** (years/2))
    print(f"{transitors:,}")

if __name__ == "__main__":
    main()
