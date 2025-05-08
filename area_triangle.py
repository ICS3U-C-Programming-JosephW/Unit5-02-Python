#!/usr/bin/env python3
# Created By: Joseph Wondimagnehu
# Date: May 8, 2025
# This program finds the area of a triangle
# using another function, given the base and
# height from the user.


# Define a function to calculate
# the area of a triangle.
def calc_area(base, height):
    # Set the area result to the triangle area formula.
    area_result = (1 / 2) * base * height

    # Display the area result to the user.
    print(f"\nThe area of the triangle is {area_result}cm^2.")


# Define the main function.
def main():
    # Get the user base in cm.
    user_base_str = input("\nEnter the base of the triangle (cm): ")

    # Try to validate the user base input.
    try:
        # Attempt to convert the user base string into a float.
        user_base_float = float(user_base_str)
        # Get the user height in cm.
        user_height_str = input("Enter the height of the triangle (cm): ")

        # Try to validate the user height input.
        try:
            # Attempt to convert the user height string to a float.
            user_height_float = float(user_height_str)

            # Check if the user entered a base
            # and height greater than zero.
            if (user_base_float > 0) and (user_height_float > 0):
                # Call the function to calculate
                # the area of the user's triangle.
                calc_area(user_base_float, user_height_float)
            # Otherwise, the user entered zero for the base, height, or both.
            else:
                # Display to the user that they must enter
                # a base and height greater than zero.
                print("\nBase and height must be greater than zero.")
        # Runs if float() could not convert the
        # user's height string input into a float.
        except ValueError:
            # Display to the user that they did not
            # enter a valid number for the height.
            print(f"\n{user_height_str} is not a valid number.")
    # Runs if float() could not convert the
    # user's base string input into a float.
    except ValueError:
        # Display to the user that they did not
        # enter a valid number for the base.
        print(f"\n{user_base_str} is not a valid number.")


# Check if the special name of the file is __main__.
if __name__ == "__main__":
    # Run the main function if so.
    main()
