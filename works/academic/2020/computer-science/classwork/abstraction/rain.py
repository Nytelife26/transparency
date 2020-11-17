import matplotlib.pyplot as plt

def main():
    for x in ["length", "width", "depth"]: # fetching and setting the length, width and depth
        valid = False
        while not valid:
            try:
                exec(f"global {x}; {x} = float(input('Enter the {x} of the pond (in cm): '))") # set all variables to a float input
                valid = True # break cycle if this is reached (valid number entered)
            except ValueError: # handle if user doesn't enter a number
                print(f"You did not enter a valid numerical representation of the {x}. Please try again.")
                continue # repeat
                
    sur = length * width
    vol = sur * depth
    
    evap = sur * 0.6 # daily evaporation = surface area * 0.6cm
    rain = []
    while True:
        val = input("Enter rain volume (in ml), or leave blank to end: ")
        if not val:
            break
            
        try:
            rain.append(sur * float(val))
        except ValueError:
            print("That value was not a valid numerical representation of the rain and will be skipped. Please try again.")
            continue
    if rain:
        loss = [evap - x for x in rain] # calculates daily water loss based on evaporation output - rain input
    
        plt.plot(range(1, len(loss)+1), loss)
        plt.ylabel(f"Daily Water Loss in cm\N{SUPERSCRIPT THREE} (total: {sum(loss)})")
        plt.xlabel("Days")
        plt.show()
    else:
        print("No values entered, therefore there are no losses to plot. Restarting...")

if __name__ == "__main__":
    while True:
        try:
            main()
        except KeyboardInterrupt:
            print("Exiting...")
            break