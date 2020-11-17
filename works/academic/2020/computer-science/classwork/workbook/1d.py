def main():
    print("You would end up with {}.".format(int(input("How much money are you investing? ")) * (((float(input("What percentage (%) is the interest rate?"))/100)+1)*float(input("How many years are you investing for?"))))
    
if __name__ == "__main__":
    while True:
        try:
            main()
        except KeyboardInterrupt:
            print("Exiting...")
            break