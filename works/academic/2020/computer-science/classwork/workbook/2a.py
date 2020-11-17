def main():
    thresholds = {0: "minor", 4: "moderate", 6: "strong", 7: "major", 8: "devastating"}
    magnitude  = float(input("What magnitude was the earthquake? "))
    idx        = list(thresholds.keys())[len(thresholds.keys()) - (list(reversed([magnitude > x for x in thresholds.keys()])).index(True) + 1)]
    print("There has been a {} earthquake in {}.".format(thresholds[idx], input("Where was the epicentre of the earthquake located? ").title()))

if __name__ == "__main__":
    while True:
        try:
            main()
        except KeyboardInterrupt:
            print("Exiting...")
            break