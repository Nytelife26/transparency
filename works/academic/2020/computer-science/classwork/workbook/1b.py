import datetime

def main():
    delta = datetime.timedelta(seconds=int(input("How many seconds? ")))
    print("That's {} days, {} hours, {} minutes and {} seconds.".format(delta.days, delta.seconds//3600, (delta.seconds//60)%60, delta.seconds%60))

if __name__ == "__main__":
    while True:
        try:
            main()
        except KeyboardInterrupt:
            print("Exiting...")
            break