#!/usr/bin/env python3

# Created by: Jackson Naufal
# Created on: May 2022
# This is a address post code 



def post_function(fullname, 
    streetnum, 
    streetname,
    city,
    province, 
    postalcode, 
    apartment = None):

    # output
    
    if apartment is not None:
        post_code = "{0} \n{1}-{2} {3} \n{4} {5} {6}".format(
        fullname, 
        apartment, 
        streetnum, 
        streetname, 
        city, 
        province, 
        postalcode)
    
    else:
        post_code = "{0} \n{1} {2} \n{3} {4} {5}".format(fullname, 
        streetnum, 
        streetname, 
        city, 
        province, 
        postalcode)
    
    return post_code.upper()
    


def main():

    apartment = None
    
    # input
    fullname = input("Enter your fullname! (first, middle, last): ")
    question = input("Do you live in an apartment(y/n)?): ")
    if question.upper() == "Y" or question.upper() == "YES":
        apartment = input("Enter your apartment number!: ")
    streetnum = input("Enter your street number!: ")
    streetname = input("Enter street name AND type!: ")
    city = input("Enter your city!: ")
    province = input("Enter your province!: ")
    postalcode = input("Enter your postal code (LNL NLN): ")
                        

    # process
    try:
        street_number_int = int(streetnum)
        
        if street_number_int < 0:
            print("\nInvalid Street Number")
        elif apartment is not None:
            apartment_number_int = int(apartment)
            if apartment_number_int < 0:
              print("\nInvalid Street Number")
            else: 
                information = post_function(
                    fullname, 
                    apartment, 
                    streetnum, 
                    streetname, 
                    city, 
                    province, 
                    postalcode, 
                    )
                print (information)
        else:
            information = post_function(
                fullname, 
                streetnum, 
                streetname, 
                city, 
                province, 
                postalcode, 
                )
            print (information)

    except Exception:
        print("Not An Integer")

    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
