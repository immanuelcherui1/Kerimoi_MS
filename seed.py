#!/usr/bin/env python3

from __init__ import CONN, CURSOR
from profile import Profile
from milk_profile import MilkProfile

def seed_database():
    
    Profile.drop_table()
    MilkProfile.drop_table()
    
    Profile.create_table()
    MilkProfile.create_table()


    # Seed Profiles
    Profile.create("George Okumu", 31875378, 34, "Male")
    Profile.create("Naomi Mogi", 37654341, 32, "Female")
    Profile.create("Immanuel Ronoh", 18795402, 23, "Male")
    Profile.create("Sarah Wanjiku", 42345878, 29, "Female")
    Profile.create("Ian Chesire", 37650321, 23, "Male")
    Profile.create("Adriano Suprine", 28769430, 25, "Female")
    Profile.create("Lamech Omwega", 22845878, 30, "Male")
    Profile.create("Samuel Omoding", 18654620, 18, "Male")
    Profile.create("Mary Watiri", 33765032, 25, "Female")
    Profile.create("Sydney Mukisira", 42305070, 21, "Male")
    Profile.create("Hillary Maina", 27600021, 24, "Female")
    Profile.create("Philiph Wekullo", 15876543, 33, "Male")


    
    # Seed Milk Profiles
    MilkProfile.create("2024-03-10", 18795402, 13.5)
    MilkProfile.create("2024-03-10", 31875378, 11.2)
    MilkProfile.create("2024-03-10", 28769430, 37.9)
    MilkProfile.create("2024-03-10", 37650321, 23.6)
    
    MilkProfile.create("2024-03-11", 28769430, 33.9)
    MilkProfile.create("2024-03-11", 42345878, 26.0)
    MilkProfile.create("2024-03-11", 31875378, 18.8)
    
    MilkProfile.create("2024-03-12", 31875378, 15.0)
    MilkProfile.create("2024-03-12", 42345878, 31.6)
    
    MilkProfile.create("2024-03-13", 18795402, 36.3)
    MilkProfile.create("2024-03-13", 31875378, 37.8)
    
    MilkProfile.create("2024-03-14", 42345878, 59.7)
    MilkProfile.create("2024-03-14", 28769430, 27.5)
    MilkProfile.create("2024-03-14", 37650321, 45.6)
    
    MilkProfile.create("2024-03-15", 18795402, 27.8)
    MilkProfile.create("2024-03-15", 28769430, 14.2)
    
    MilkProfile.create("2024-03-16", 18795402, 63.9)
    MilkProfile.create("2024-03-16", 27600021, 30.7)
    MilkProfile.create("2024-03-16", 31875378, 22.5)
    MilkProfile.create("2024-03-16", 37650321, 39.0)
    

if __name__ == "__main__":
    seed_database()
    print("Seeded database")
