# Milestone 3 Project - Travelbuddy portal
For my third, Python based project, I’ve decided to expand the idea of a travel portal from my first milestone project. This site allows users to register themselves as tour providers and list their tours on a website.
## UX
The website serves 2 types of users, regular visitors who are looking for an organised tour in the area they are planning their vacations and people who provide organised tour experiences using their expertise and knowledge of their local area.
### User stories
- I’d like the regular user to be welcomed with an eye-catchy hero image with short description of the website functionality
- I’d like the regular user to have a quick look at the small selection of tours on the homepage
- I’d like the regular user to view all the tours on the “Browse” page
- I’d like the regular users to filter this page by location and tour length
- Finally, I’d like the user to click on the card preview of the tour and see its details on a separate page with full description, selection of photos and a booking button
For the tour providers:
- I’d like them to create a new account
- I’d like them to add new tours using dedicated form
- I’d like them to see all of their tours on a Dashboard page, where they can edit or delete existing tours
### Features
- The site presents the data - tours - using Bootstrap’s card component. This allows for clean and universal presentation of data and secures the layout to correctly display on different devices
- The site prevents the data to be altered or deleted by non-authorised users by checking the login status and login credentials
## Technology used
- HTML, CSS for data presentation 
- Bootstrap CSS framework 
- Google Fonts
- Font Awesome font icons library
- Python used for back-end login
- Flask web framework used to create web pages and communicate with Database
- MongoDB - NoSQL database system used to store users’ and tours’ data
## Testing
The site was tested in 2 ways. First, I’ve test the presentation layer. Site was previewed on selection of different devices - desktop, laptop, iPad, couple of smartphones - to make sure there’s no issues with responsive layout. I’ve also checked the site with HTML and CSS validators to fix some small issues.
Next I’ve tested the app logic. I’ve started with some manual testing - creating new account, re-using the same email to see if the app will reject it. After that, I’ve  logged in and added a new tour.  All the fields were correctly saved in the database. Each tour provider has the access to the Dashboard page which lists their own tours. I’ve tested couple of sample logins to make sure they only see their own data. I’ve also protected the page from un-authorised access. If no user is logged in - the page re-directs to login page automatically. Dashboard page allows to edit or delete owner’s tours. I’ve tested whether both buttons function properly and display or delete only one and correct item. I’ve used tour’s `_id` field because of its uniqueness. No other tour can share the same id number.  Item selected for editing display its data inside HTML form. I’ve tested if the data is correctly loaded and after some changes saved back into the database as expected.
After that I’ve tested if the data can be altered or deleted without the proper access credentials, meaning only by the user associated with the tour. By using Flask’s `session` module I was able to detect if and which user is logged in so I could protect both edit and delete operations to be only performed on data a user has the rights to. If no user is logged in or different user is trying to delete other people’s items the function prevents this and displays appropriate message.
## Deployment
The site was originally created on a local machine and synchronised with remote repository at GitHub.  Python allows to create a virtual environment on a local machine. Thus my development folder was separated from the global Python interpreter and all the modules where only installed in this folder. This feature also helps to deploy the site to Heroku using `requirement.txt` consisting of all dependencies needed to run the app.