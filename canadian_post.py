#!/usr/bin/env python3

# Created by: Jackson Naufal
# Created on: May 2022
# This is a address post code


def post_function(
    full_name, street_num, street_name, city, province, postal_code, apartment=None
):

    # output
    if apartment != None:
        post_code = "\n{0} \n{1}-{2} {3} \n{4} {5} {6}".format(
            full_name, street_num, street_name, city, province, postal_code, apartment
        )

    else:
        post_code = "\n{0} \n{1} {2} \n{3} {4} {5}".format(
            full_name, street_num, street_name, city, province, postal_code
        )

    return post_code.upper()


def main():

    apartment = None

    # input
    full_name = input("Enter your full_name! (first, middle, last): ")
    question = input("Do you live in an apartment(y/n)?): ")
    if question.upper() == "Y" or question.upper() == "YES":
        apartment = input("Enter your apartment number!: ")
    street_num = input("Enter your street number!: ")
    street_name = input("Enter street name AND type!: ")
    city = input("Enter your city!: ")
    province = input("Enter your province!: ")
    postal_code = input("Enter your postal code (LNL NLN): ")

    # process
    try:
        street_number_int = int(street_num)

        if street_number_int < 0:
            print("\nInvalid Street Number")
        elif apartment is not None:
            apartment_number_int = int(apartment)
            if apartment_number_int < 0:
                print("\nInvalid Street Number")
            # call functions
            else:
                information = post_function(
                    full_name,
                    apartment,
                    street_num,
                    street_name,
                    city,
                    province,
                    postal_code,
                )
                print(information)
        else:
            information = post_function(
                full_name,
                street_num,
                street_name,
                city,
                province,
                postal_code,
            )
            print(information)

    except Exception:
        print("Not An Integer")

    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
