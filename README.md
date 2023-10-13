# Django-Backend-Packages

- User Registration
- User login
- Package table in admin panel only
- All users could add to subscribe to more than one package
- Subscription by making an order with one or more package



## Endpoints

- http://127.0.0.1:8000/users/subscriptions   [View the subscriptions of the users by email] 
- http://127.0.0.1:8000/users/subscribe [Subscribe to one or more package by providing array name: package_ids]
- http://127.0.0.1:8000/packages/ [See all packages]
- http://127.0.0.1:8000/users/login [Login by email and password]
- http://127.0.0.1:8000/users/signup [Signup by email and password]


## Instructions to run the code

- Clone the code to your machine 
- Open the folder 
- Make sure to have python installed
- Install the required dependencies: pip install -r requirements.txt
- Create your .env file and add its credentials as an example: 
  DB_NAME=mydatabase
  DB_USER=myuser
  DB_PASSWORD=mypassword
  DB_HOST=localhost
  DB_PORT=5432
- Run the server: python manage.py runserver
