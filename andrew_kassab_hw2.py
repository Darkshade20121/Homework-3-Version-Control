def main():
    if leap_year() == 0:
        print("Not a leap year")
    else:
        print("Is a leap year")

def leap_year():
    year = inp_validation()
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

def inp_validation():
    while True: 
        try:
            year = int(input("Enter a year: "))
        except ValueError:
            print("Sorry, this value was not accepted")
            continue
        else:
            print("Value was successful!")
            return year
            break


if __name__ == "__main__":
    main()

