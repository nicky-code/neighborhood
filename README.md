# Neighborhood
## Neighborhood-App, 4th of November 2019
### By Aline Nicole UWAMARIYA
## Description
If you are like me, You really don’t know what is happening in your neighborhood most of the time. What if an important meeting happens, theft or even death wouldn’t you like to know about it.

Our Job is to create a web application that allows you to be in the loop about everything happening in your neighborhood. From contact information of different handyman to meeting announcements or even alerts.
## Code scaffolding
Run python3.6 manage.py runserver when you want to implement the features of the landing pages and other pages.

## BDD
### Behaviour
We want our application to:

 a user should be able to his posts and posts of other users
* Click on a single photo to expand it and also view the details of the photo. The photo details will    appear on a modal within the same route as the main page.
* a user can Search for another user
* a user can like and comment on a post
* a user can view and rate other user's project

## Input Examples
1.search users by location of Neighborhood
2.Create a profile,registering,sign in,log in,create a post for business.

## Output Examples
any User will be able to see the businesses from the neighborhood  he/she has searched for and other business the user has posted.

## TDD
I have not test my project but normally i use Python3.6 manage.py test insta(my app-name).

## Setup/Installation Requirements

1.You should have a neighborhood class with the following properties:

Neighbourhood Name
Neighborhood location
Occupants Count
Admin Foreign key

2.Some of the methods you will need to implement are:

create_neigborhood()
delete_neigborhood()
find_neigborhood(neigborhood_id)
update_neighborhood()
update_occupants()

3.You will create a user class with the following properties;

name.
id.
neighborhood id foreign key
email address.

4.You will create a business class with the following properties;

Business name
User foreign key
neighborhood id foreign key
Business email address.
The Methods we will create are:

create_business()
delete_business()
find_business(business_id)
update_business()


5.Your application must have a business search functionality where users can search for businesses in their area.

6.Your project should have a dashboard that you will use to manage the different users.

7.our application should have a solid authentication system that allows users to sign in or register into the application before using it. When a user registers with your application they should receive a confirmation email.

8.Your project should be deployed to Heroku when you have finished with the set features. You should provide the link to your project in the description part of your project repository.

## Technology used
Python3.6
Django
Heroku
Bootstrap4

## My link repository on above

## Contact me on aline.nicole7@gmail.com
## Title Licence
Copyright(c)2019 Aline Nicole UWAMARIYA.
