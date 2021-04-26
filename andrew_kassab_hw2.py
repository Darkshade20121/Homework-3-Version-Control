def main():
    if leap_year() == 0:
        print("Not a leap year")
    else:
        print("Is a leap year")

def leap_year():
    year = input("Enter a year: ")
    year = int(year)
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return 1
            else:
                return 0
        else:
            return 1
    else:
        return 0

if __name__ == "__main__":
    main()

