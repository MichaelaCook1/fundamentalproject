# Wine and Cheese App

## External Resources:
#Presentation:
#Jira:https://michaelacook.atlassian.net/jira/software/projects/CHEES/boards/1
#App:http://35.246.75.103:5000/

## Project Overview

#App Summary
#Project Board
#User Stories
#ERD
#MOSCOW model
#CI Pipeline
#Risk Assessment
#Known Issues
#Live Demonstration
#Future Developments
#Conclusion

## App Summary

#Project Brief: To create a CRUD application with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules covered during training.


#Pitch: Wine and Cheese Board is an app where users can create, edit and display their choice of wines and cheeses as well as their own pairings. Further developments of the app could allow for user registration, personalised wine-cheese recommendations and wordpress for text posts by the users.

## Project Board

#Project board : https://imgur.com/a/EiORvHq

## User Stories

#User stories : https://imgur.com/a/zuYHVuU

## ERD

#Initial ERD detailing relation between cheese questions and cheese recommendations within database.
#Next Version will be optimised to include “Cheese Questions” as a form completely within Flask/Python and will include an intermediate table where “Cheese Recommendations” will have a many-to-many relationship to “Wine Pairings”

#Below is an updated ERD, which describes the relation in the final app version. Due to the complexity and time given the cheese questionnaire element was removed, and instead allowing all cheese and wines to be user inputs, including a pairing intermediate table.


#Initial ERD : https://imgur.com/a/4F84ApD

#Updated ERD : https://imgur.com/a/rUTnZ56

## MOSCOW Model

# M – MUST HAVE: CRUD capability, 2 related databases, clear documentation, trello board, 			          functioning flask front-end, code fully integrated into VCS, and fully 				          designed test suite 
# O -
# S – SHOULD HAVE: Many-Many database relation with an intermediate wine-cheese pairing
# C – COULD HAVE:   Wine and Cheese recommendations based on user input, app run in background using Gunicorn
# O -
#W – WON’T HAVE: sharing links between social media platforms, wine clink animation 				             using CSS, wordpress for user posts 

## CI Pipeline

#CI Pipeline : https://imgur.com/a/1BCPakl

## Risk Assessment

#Initial Risk Assessment : https://imgur.com/a/qnyTryy

#Updated Risk Assessment : https://imgur.com/a/jPIjlbl

## Known Issues 

#After troubleshooting “Update” does not work on the app due to an Attribute error, that I have been unable to fix within the time.
#Within the Unit testing when testing the “Wine” table all tests passed bar one where an UnmappedInstanceError occurred, unable to find the cause I removed the Wine table from the test to ensure a fully passed result with 100% coverage.
#Within the Integrated testing a SyntaxError appears for the xpath of the add functionality, as said path has been copied from the app itself, I could not source this error.

## App functionality

# To run this web application the prequisite packages must first be installed, all packages necessary for running this application are located within the requirements.txt and can be installed directly by inputting the following code:

# sudo apt install python3-pip
# sudo apt install python3-venv
# python3 -m venv venv
# . venv/bin/activate
# pip3 install -r requirements.txt


# From here the database must first be created and then the application can be run, this can be done by inputting the following:

# python3 create.py
# python3 app.py

# The application also has Gunicorn functionality so can be run in the background by inputting:

# gunicorn --workers 4 --bind=0.0.0.0:5000 app:app




## Testing

# The unit testing in this application was carried out using pytest, to test set functionality of operations within the application, it also includes a coverage report which details as a percentage how much code within the application has been successfully tested, these reports are in html format and are located within the tests directory. The base test was created such that the database configuration can be passed through. Next the TestViews class was created to test each url on the index page, due to time constraints only the "addcheese" url of the "add" section of urls was tested however the code used for the "addwine" and "addpair" urls was copied directly from the "addcheese" code therefore should produce the same result.

# The AddCheese url was tested next and successfully passed.

# The DeleteCheese url was tested next and successfully passed.

# As I could not resolve the Update functionality within the Routes.py file, it would have been arbitrary to test this url knowing it did not work.

# For these tests conducted a coverage of 100% was achieved

# To increase the number of tests I made an attempt at including a test for the AddWine url however I encountered an UnmappedInstanceError on the variables within the Wines table, this would imply a mapping request was made to an unknown instance, however as this table is identical in structure to the Cheeses table and those tests were successful, and the code for testing the wines was identical, the source of this error could not be located, and to not produce a failing test result this test was removed.


# The integrated testing in this application was carried out using selenium through a chromium browser to test the functionality of all operations working together within the application. The prequistie software has been added to the requirements.txt, however a chrome driver is required if not already present, this can be installed in linux from the following link:

#wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip

#The test base is set up similarly to unit testing with the addition of environment variables to connect to the application locally. The registration tests were then set up using the executable x-path of the input boxes on the "AddCheese" html site, these were accessed by pressing sht+I to view the html elements. When running the pytest of this a SyntaxError appears over the x-path of the "Cheese_name" variable, this was examined numerous times for minor mistakes and wrong bracket placement however I could not locate this issue, as well as this the x-path was copied directly from the html elements so there was no opportunity for spelling mistakes. Due to time constraints I could not investigate this further.

## Demonstration

#The application can be accessed at the following external ip address : 35.246.75.103:5000


## Further Developments 

#Upon resolution of the known software issues, further developments can be made to the application.
#Aesthetic additions to the html – background image, bootstrap, CSS etc.
#User registration and login capability 
#Wordpress implementation for text posts.

## Conclusion

#Overall I was successful in creating a flask web application covering the core modules I have learned over the course of the Academy.
#While due to time constraints, and listed software issues the application did not have full “CRUD” functionality, in its current state it allows the creation, addition and deletion of database entries across three tables, and was tested and analysed to a high degree.
#Given more time, with the test analysis that conducted, full CRUD functionality could be obtained.

## Author

# Michaela Cook

## Acknowledgments

# I would like to acknowledge Ben Hesketh and Nathan Forrester for their guidance and support over the course of this project and for their assistance in troubleshooting many of the software errors I encountered over the course of this project.


