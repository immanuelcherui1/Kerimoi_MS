# lib/helpers.py

from profile import Profile
from milk_profile import MilkProfile
import datetime


    
def exit_program():
    print("See You Again!")
    exit()
       
# FOR PROFILES:
def list_profiles():
    profile_records = Profile.get_all()
    for profile in profile_records:
        print(profile) 
        
def find_person_profile_by_national_id():
    national_id_ = input("Enter the national id: ")
    person_profiles = Profile.find_by_national_id(national_id_)
    if person_profiles:
        print(f"Name: {person_profiles.national_id}")
        print(f"National ID: {person_profiles.age}")
        print(f"Age: {person_profiles.gender}")
        print(f"Gender: {person_profiles.id}")
    else:
        print(f'Profile with {national_id_} not found')

    
        
def update_profile():
    profile_id = input("Enter the Profile Id OR National Id: ")
    profile = Profile.find_by_id(profile_id) or Profile.find_by_national_id(profile_id)  
    if profile:
        try:
            new_name = input("Enter the profile's New Name: ")
            new_national_id = input("Enter the profile's New National Id: ")
            new_age = input("Enter Profile's New Age: ")
            new_gender = input("Enter Profile's New Gender: ")
            
            Profile.update(profile_id, new_name, new_national_id, new_age, new_gender)  
            print(f'Successfully updated')
        except Exception as exc:
            print("Error updating profile: ", exc)
    else:
        print(f'Profile {profile_id} not found')


        
        
def create_profile():
        name = input("Enter the profile's name: ")
        national_id = input("Enter the profile's national id: ")
        age = input("Enter the profile's age: ")
        gender = input("Enter the profile's gender: ")
        try:
            profile = Profile.create(name, national_id, age, gender)
            print('Successfully Created')
            
        except Exception as exc:
            print("Error creating profile: ", exc)
        
def delete_profile():
    national_id = input("Enter the profile's National Id: ")
    yes_responses = {"Yes", "yes", "YES", "y", "Y"}
    profile = Profile.find_by_national_id(national_id)
    if profile: 
        print(f"Are you sure you want to delete {profile.national_id}?")
        confirmation = input("Enter Yes or No: ")
        if confirmation in yes_responses:
            Profile.delete(national_id)
            print(f"{profile.national_id} Deleted Successfully")
        else:
            print("Deletion Unsuccessful")
    else:
        print(f'Profile {national_id} not found')



#FOR DAIRY FARMERS
def list_milk_records():
    milk_records = MilkProfile.get_all()
    for milk_profile in milk_records:
        print(milk_profile)
        
def list_specific_dairy_farmers_records():
    dairy_farmer_national_id = input("Enter the national id: ")
    dairy_farmer_profile = Profile.find_by_national_id(dairy_farmer_national_id)
    if dairy_farmer_profile:
        print("Dairy Farmer's Name:", dairy_farmer_profile.national_id)
        milk_records = MilkProfile.find_by_national_id(dairy_farmer_national_id)
        if milk_records:
            print("Milk Records:")
            for record in milk_records:
                print(f"  Date: {record.date}, Litres: {record.litres}")
        else:
            print(f'No milk records found for profile with {dairy_farmer_national_id}')
    else:
        print(f'Profile with national ID {dairy_farmer_national_id} not found')
        



def delivered_milk_recording():  
    profile_id = input("Enter the profile ID: ")
    dairy_farmer_national_id = Profile.get_profiles_national_id(profile_id)
    yes_responses = {"Yes", "yes", "YES", "y", "Y"}
    farmers_profile = Profile.find_by_national_id(dairy_farmer_national_id)
    
    if dairy_farmer_national_id:
        print(f"Delivered by {farmers_profile.national_id}?")
        confirmation = input("Yes or No: ")
        if confirmation in yes_responses:
            current_date = datetime.date.today()
        
            litres = input("Enter the litres of milk delivered: ")

            try:
                # Create the MilkProfile instance using the provided data
                MilkProfile.create(current_date, dairy_farmer_national_id, litres)
                print("Milk delivered added successfully.")
            except Exception as e:
                print(f"Error adding milk delivered: {e}")
        else:
            print("Kindly be sure next time")
    else:
        print("Enter a Valid Profile Id")
        
        
def update_farmers_litres():
    profile_id = input("Enter the Profile Id OR National Id: ")
    yes_responses = {"Yes", "yes", "YES", "y", "Y"}
    dairy_farmer_profile = Profile.find_by_id(profile_id) or Profile.find_by_national_id(profile_id)
    dairy_farmer_national_id = Profile.get_profiles_national_id(profile_id)
     
    if dairy_farmer_profile:
        print(f"Change {dairy_farmer_profile.national_id}'s Milk Records?")
        confirmation = input("Yes or No: ")
        if confirmation in yes_responses:
            new_date = input("Enter the date (YYYY-MM-DD) when the litres were recorded: ")
            new_litres = input("Enter new litres: ")
            MilkProfile.update_litres(dairy_farmer_national_id, new_litres, new_date)
            print("Successfully Changed!")
        
        else:
            print("Kindly be Careful Next Time")
        
    else:
        print("Dairy farmer profile not found")


