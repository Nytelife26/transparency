def main():
    width=int(input('Enter the width: '))
    length=int(input('Enter the length: '))
    print("The area of the floor would be {1}m\N{SUPERSCRIPT TWO}".format(x*y))

if __name__ == "__main__":
    while True:
        try:
            main()
        except KeyboardInterrupt:
            print("Exiting...")
            break