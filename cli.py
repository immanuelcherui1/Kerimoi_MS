# lib/cli.py

from helpers import (
    exit_program,
    list_profiles,
    list_milk_records,
    find_person_profile_by_national_id,
    update_profile,
    list_specific_dairy_farmers_records,
    create_profile,
    delete_profile,
    delivered_milk_recording,
    update_farmers_litres
)


def main():
    while True:
        main_menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            while choice:
                print("ALL PROFILES")
                all_profiles_menu()
                new_choice = input(">")
                if new_choice == "0":
                    choice = ""
                elif new_choice == "1":
                    list_profiles()
                elif new_choice == "2":
                    find_person_profile_by_national_id() 
                elif new_choice == "3":
                    update_profile()   
                elif new_choice == "4":
                    create_profile()
                elif new_choice == "5":
                    delete_profile()
        
        elif choice == "2":
            while choice:
                print("DAIRY FARMERS PROFILE")
                milk_profile_menu()
                new_choice = input(">")
                if new_choice == "0":
                    choice = ""
                elif new_choice == "1":
                    list_milk_records()
                elif new_choice == "2":
                    list_specific_dairy_farmers_records()
                elif new_choice == "3":
                    delivered_milk_recording()
                elif new_choice == "4":
                    update_farmers_litres()
                
        else:
            print("Invalid choice")

def main_menu():
    print("Select an option:")
    print("0. Exit")
    print("1. Profiles Menu")
    print("2. Dairy Farmers Profile Menu")
    
def all_profiles_menu():
    print("Select an option:")
    print("0. Back to main menu")
    print("1. List of Profiles")
    print("2. Find Person profile by National ID")
    print("3. Update Profile")
    print("4. Create Profile")
    print("5. Delete Profile")
       
def milk_profile_menu():
    print("Select an option:")
    print("0. Back to main menu")
    print("1. Dairy Farmers Records")
    print("2. List by Id - Dairy Farmer's Records")
    print("3. Record Delivered Milk")
    print("4. Change Milk Records Data")
    
    

if __name__ == "__main__":
    main()
