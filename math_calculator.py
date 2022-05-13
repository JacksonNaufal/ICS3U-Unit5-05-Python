#!/usr/bin/env python3

# Created by: Jackson Naufal
# Created on: March 2022
# This is whats your grade level

import math 

def grade_function(radius, height):
    
    # output
    
    volume = math.pi * (radius ** 2) * height
    
    return volume

def main():
    
    # input
    user_radius = input("Enter Your radius (mm): ")
    user_height = input("Enter Your height (mm): ")   
    
    # process
    try:
        user_radius_int = float(user_radius)
        user_height_int = float(user_height)
        function_grade = grade_function(radius = user_radius_int, height = user_height_int)
        
        print("The volume is {0} cm³".format(function_grade))
    
    except Exception:
        print("Not An Integer")
        
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
