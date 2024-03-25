import sqlite3
from __init__ import CURSOR,CONN
from profile import Profile

class MilkProfile:
    def __init__(self,id, date, dairy_farmer_national_id, litres):
        self.id = id
        self.date = date
        self.dairy_farmer_national_id = dairy_farmer_national_id
        self.litres = litres

    
        
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of MilkProfile instances """
        CURSOR.execute('''
            CREATE TABLE IF NOT EXISTS milk_profiles (
                id INTEGER PRIMARY KEY,
                date TEXT,
                dairy_farmer_national_id INTEGER,
                litres REAL,
                FOREIGN KEY (dairy_farmer_national_id) REFERENCES profile(national_id)
            )
        ''')
        CONN.commit()
        
    def save(self):
        CURSOR.execute("INSERT INTO milk_profiles (date, dairy_farmer_national_id, litres) VALUES (?, ?, ?)",
                       (self.date, self.dairy_farmer_national_id, self.litres))
        CONN.commit()
    
    @classmethod
    def create(cls, date, dairy_farmer_national_id, litres):
        """ Initialize a new MilkProfile instance and save the object to the database """
        milk_profile = cls(None, date, dairy_farmer_national_id, litres)
        milk_profile.save()
        return milk_profile

    
    
    @classmethod
    def drop_table(cls):
        """ Drop the table that persists MilkProfile instances """
        CURSOR.execute("""
            DROP TABLE IF EXISTS milk_profiles;
        """)
        CONN.commit()
        
    @classmethod
    def get_all(cls):
        """ Retrieve all milk profiles from the database """
        CURSOR.execute("""
            SELECT profiles.name AS DAIRY_FARMER_NAME, milk_profiles.date AS MILK_DELIVERY_DATE, milk_profiles.litres AS LITRES
            FROM milk_profiles 
            JOIN profiles ON milk_profiles.dairy_farmer_national_id = profiles.national_id
        """)
        return CURSOR.fetchall()
    
    
    @classmethod
    def find_by_national_id(cls, dairy_farmer_national_id):
        """ Retrieve a profile from the database by its national_id """
        CURSOR.execute("SELECT * FROM milk_profiles WHERE dairy_farmer_national_id=?", (dairy_farmer_national_id,))
        rows = CURSOR.fetchall()
        if rows:
            return [cls(*row) for row in rows]
        else:
            return None
           
    
    @classmethod
    def update_litres(cls, dairy_farmer_national_id, new_litres, new_date):
        """ Update the attributes of the milk in the database """
        CURSOR.execute("UPDATE milk_profiles SET litres=?, date=? WHERE dairy_farmer_national_id=?", 
                    (new_litres, new_date, dairy_farmer_national_id))
        CONN.commit()



