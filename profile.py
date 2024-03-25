import sqlite3
from . import CURSOR,CONN

class Profile:
    def __init__(self, name, national_id ,age, gender,id=None):
        self.id = id
        self.name = name
        self.national_id = national_id
        self.age = age
        self.gender=gender


    
    def create_table():
        """ Create a new table to persist the attributes of Profile instances """
        CURSOR.execute('''
            CREATE TABLE IF NOT EXISTS profiles (
                id INTEGER PRIMARY KEY,
                name TEXT,
                national_id INTEGER UNIQUE,
                age INTEGER,
                gender TEXT,
                CONSTRAINT national_id_length CHECK (LENGTH(CAST(national_id AS TEXT)) = 8)

                
            )
        ''')
        CONN.commit()
    
    def save(self):
        CURSOR.execute("INSERT INTO profiles (name, national_id, age, gender) VALUES (?, ?, ?, ?)",
                       (self.name, self.national_id, self.age, self.gender))
        CONN.commit()
    
    @classmethod
    def create(cls, name, national_id, age, gender):
        """ Initialize a new Profile instance and save the object to the database """
        profile = cls(name, national_id, age, gender)
        profile.save()
        return profile
    
    
    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Profile instances """
        CURSOR.execute("""
            DROP TABLE IF EXISTS profiles;
        """)
        CONN.commit()
    
    @classmethod
    def get_all(cls):
        """ Retrieve all profiles from the database """
        CURSOR.execute("""
            SELECT profiles.name AS NAME, profiles.national_id AS NATIONAL_ID, profiles.age AS AGE, profiles.gender AS GENDER
            FROM profiles 
			ORDER BY NAME;
        """)
        return CURSOR.fetchall()
    
    @classmethod
    def update(cls, profile_id, new_name, new_national_id, new_age, new_gender):
        """ Update the attributes of the profile in the database """
        CURSOR.execute("UPDATE profiles SET name=?, national_id=?, age=?, gender=? WHERE id=? OR national_id=?", 
                    (new_name, new_national_id, new_age, new_gender, profile_id, profile_id))
        CONN.commit()


    @classmethod
    def find_by_national_id(cls, national_id):
        """ Retrieve a profile from the database by its national_id """
        CURSOR.execute("SELECT * FROM profiles WHERE national_id=?", (national_id,))
        row = CURSOR.fetchone()
        if row:
            return cls(*row)
        else:
            return None
       
       
    @classmethod 
    def find_by_id(cls, profile_id):
        """ Retrieve a profile from the database by its ID """
        CURSOR.execute("SELECT * FROM profiles WHERE id=?", (profile_id,))
        row = CURSOR.fetchone()
        if row:
            return cls(*row)
        else:
            return None
        
    @classmethod
    def delete(cls, national_id):
        """Delete the profile corresponding to the given national id"""
        try:
            CURSOR.execute("""
                DELETE FROM profiles
                WHERE national_id = ?
            """, (national_id,))
            CONN.commit()
            print("Profile deleted successfully")
        except sqlite3.Error as e:
            print(f"Error deleting profile: {e}")



    @classmethod
    def get_profiles_national_id(cls, profile_id):
        """Retrieve the dairy profile's national ID based on the profile ID."""
        try:
            # Execute SQL query to fetch the profile's national ID based on the provided profile ID
            CURSOR.execute("SELECT national_id FROM profiles WHERE id=?", (profile_id,))
            row = CURSOR.fetchone()
            if row:
                return row[0]  # Return profile's national ID
            else:
                print(f"No profile found with profile ID: {profile_id}")
                return None
        except Exception as e:
            print(f"Error fetching profile's national ID: {e}")
            return None


        
        
    
           
            