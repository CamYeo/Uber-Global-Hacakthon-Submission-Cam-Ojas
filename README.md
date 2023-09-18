# Uber Global Hacakthon Submission Cam+Ojas
This is Ojas and Cameron's Uber Global Hackathon submission, a transport survey web application

# In each file
I will be skipping over the inherited files from django that I did not change. 
1. In models.py we have created a model to store the data of transport users.

2. In views.py there are several functions. login, logout and register are standard functions that redirect users to their respective templates and checks throguh the form data, creating / logging in a user if valid. home redirects the user to the homepage where the user is able to navigate the app. ammend is the function that updates the transport data and info fetches the data from the database to be used in the frontend of the application.

3. URLS.py contain all the relevant paths needed for the application.
4. HTML files:
⋅⋅*layout.html - standard html layout inherited by other html files. Contains navbar and some javascript files
⋅⋅*home.html - Page that collates data
⋅⋅*hackathon_2.html 2nd Redirect page with all the data


