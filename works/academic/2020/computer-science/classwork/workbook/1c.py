import datetime

def main():
    print("That's {} seconds.".format(datetime.timedelta(days=int(input("How many days? ")), hours=int(input("How many hours? ")), int(input("How many minutes? "))).seconds)

if __name__ == "__main__":
    while True:
        try:
            main()
        except KeyboardInterrupt:
            print("Exiting...")
            break