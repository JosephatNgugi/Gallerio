# Gallerio
## Author  
  
>[Josephat Ngugi]
  
# Description  
This is a Django application that displays user images.
##  Live Link  
Click : https://serene-sierra-10808.herokuapp.com/ to visit the webite
## Screenshots 
###### Home page

## User Story  
  
* View different photos that interest them  
* Click a single image to expand it and view the details of that photo  
* Search for different categories   
* Copy a link to the photo to share with my friends.  
* View photos based on the location they were taken.  
  

  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
https://github.com/Josephat-Ngugi/Gallerio.git
```
##### Navigate into the folder and install requirements  
 ```bash 
cd Album pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations 
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your local host server `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python3](https://www.python.org/)  
* [Django 1.11](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* Navbar location dropdown currently not working.  
  
## License 

* Copyright (c) 2022 **Josephat Ngugi**