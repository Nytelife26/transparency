def main():
    valid = False
    while not valid:
        try:
            days = int(input("How many days was the car hired for? ")
            miles = int(input("How many miles did the car travel during the hiring period? ")
            if miles <= 0 or days <= 0: # You don't want either of these numbers to be less than zero or negative.
                raise ValueError
            valid = True
        except ValueError:
            print("One or more of the values entered were not valid numerical representations. Please try again.")
            
    if days < 3:
        charge = (50 * days) + (0.2 * miles)
    else:
        charge = (35 * days) + (0.3 * miles)
    
    print(f"The client owes £{charge}.")

if __name__ == "__main__":
    while True:
        try:
            main()
        except KeyboardInterrupt:
            print("Exiting...")
            break