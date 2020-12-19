# Assignment/usr/bin/env python3
# This program was created by Larry Nkengbeza
# This program was created on December 2020
# This program adds numbers up.

def main():
    loop_counter = 0
    # input
    user_input_str = input("Enter a number to be added:")
    print("")
    user_input_str = input("Enter another number to be added:")
    print("")

    # Process and Ouput
    try:
        user_input = int(user_input_str)

        while loop_counter < user_input:
            print("The answer is {0}.".format(5+3))
            loop_counter = loop_counter + 1
    except Exception:
        print("This is not an integer.")
    finally:
        print("Thanks for using the program.")


if __name__ == "__main__":
    main()
