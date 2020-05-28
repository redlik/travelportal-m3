# Milestone 3 Project - Travelbuddy portal
For my third, Python based project, I’ve decided to expand the idea of a travel portal from my first milestone project. This time the site allows users to register themselves as tour providers and list their tours on a website.

Live version of the app: [travelbuddy-app.herokuapp.com][1]
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
- The site presents the data - tours - using Bootstrap’s card component. This allows for clean and universal presentation of data and make the layout behave correctly on different devices
- The site allows to create user accounts and add tours by registered users
- The site presents registered users with list of their tours and allows them to add, edit or delete operations
- The site prevents the data to be altered or deleted by non-authorised users by checking the login status and login credentials
## Technology used
- HTML, CSS for data presentation 
- Bootstrap CSS framework 
- Google Fonts
- Font Awesome font icons library
- Python used for back-end logic
- Flask web framework used to create web pages and communicate with database
- MongoDB - NoSQL database system used to store users and tours data
## Testing
The site was tested in 2 ways. First, I’ve test the presentation layer. Site was previewed on selection of different devices - desktop, laptop, iPad, couple of smartphones - to make sure there’s no issues with responsive layout. I’ve also checked the site with HTML and CSS validators to fix some small issues.
Next, I’ve tested the app logic. I’ve started with some manual testing - creating new account, re-using the same email to see if the app will reject it. I’ve tested the navigation menu whether it re-directs to correct routes and correct templates are displayed.

After that, I’ve  logged in and added a new tour.  All the fields were correctly saved in the database. Each tour provider has the access to the Dashboard page which lists their own tours. I’ve tested couple of sample logins to make sure they only see their own data. I’ve also protected the page from un-authorised access. If no user is logged in - the page re-directs to login page automatically. Dashboard page allows to edit or delete owner’s tours. I’ve tested whether both buttons function properly and display or delete only one and correct item. I’ve used tour’s `_id` field because of its uniqueness. No other tour can share the same id number.  Item selected for editing display its data inside HTML form. I’ve tested if the data is correctly loaded and after some changes saved back into the database as expected.

After that I’ve tested if the data can be altered or deleted without the proper access credentials, meaning only by the user associated with the tour. By using Flask’s `session` module I was able to detect if and which user is logged in so I could protect both edit and delete operations to be only performed on data a user has the rights to. If no user is logged in or different user is trying to delete other people’s items the function prevents this and displays appropriate message.
## Deployment
The site was originally created on a local machine and pushed to remote repository at GitHub. During the development the application was run locally using Python’s virtual environment and a local copy of MongoDB database via Compass app. 

Most of the development was done on a `master` branch, but for user login/registration and tour editing functionality I’ve decided to create separate branches using `git branch` to create and `git checkout` to switch to another branch. Branching allow a developer to work on new features or bug fixing safely leaving the master branch at the stage before separating the code into separate branch. In my case after the login/registration functionality was working as expected I’ve merged my `users` branch back into `master` using `git checkout master` and `git merge users`. For the second branch I’ve used GitHub online functionality. I’ve created a new branch on the website and because my editor - VS Code - was logged in to Github using my credentials I could see and switch to the new branch right away. Once I was happy with the code in the new branch I’ve used GitHub Pull Request and merged the branch back into master.

When the application was completed and working as expected I’ve transferred it to Heroku service. I’ve used direct link to my GitHub repository so I could still push my commits to “remote” and have the app re-built automatically. Flask app needs special instructions to be hosted at Heroku. 

First, it needs a `requirements.txt` file which list all necessary packages required to run the app.  The file is created using `pip` manager, using `pip freeze > requirements.txt` command.

Second, there needs to be a `Procfile`which points to the file the app is started from - `app.py` in my case and platform being used, `python` in my case. 

The last element were the configuration variables, which store sensitive information such as login to database, a secret key used to encrypt session data. These variables are created inside Heroku account panel and called in code using `os.getenv` command.

The local database has been transferred to a cloud account at MongoDB Atlas via `JSON` files. I’ve kept the same names of collections so I only had to change the link to the database from localhost to remote server at MongoDB Atlas.
Once all elements were in place I could check if the app was working correctly or not. I’ve used Heroku command line tools to check the logs for any messages using  `heroku logs --tail` command. Every couple of times I had to reboot my app using `heroku restart` command to get my app running again.

## Development Issues
The biggest issue I had working on this project was the Heroku deployment. My app was initially constructed with all files contained inside `application` folder with small `main.py`file calling the `app` object from inside that folder. While it did work no problem on a local computer, the app did crashed right away when deployed to Heroku. Unfortunately there was no particular error displayed in the log file, so there was no clear reason my app was crashing. I’ve followed tutors’ advice and merge all the Python files into one `app.py` file in the root folder and only then my app started to work as expected.

[1]:	https://travelbuddy-app.herokuapp.com/