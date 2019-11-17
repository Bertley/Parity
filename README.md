# Parity Go 

Data models for a home automation system. 

# Requirements 

- Python 3.6
- Requirements.txt

# Usage

- Clone repo <repo-link>
- I have included my virtual environment to this project for simplicity 
- To activate run ``source env/bin/activate`` from the project root 
- The cd into the Django project ``cd paritygo``
- Then run the Django project ``python manage.py runserver``
- The Username and password for /admin is ``username: ehisidialu password: paritygo``
 
In this project i am tracking changes to the House thermostats, Room lights & Room Sensors table, 
To find automatic entries of these changes check the Field History table 

The fields tracked are 

1. House Thermostate Mode (on, cool, etc)
2. Room Light status (off, on)
3. Value of the Room Sensor. (value of temperature)

Go ahead and makes changes to fields and entries of these changes will automatically be added to the Field History Table. 

