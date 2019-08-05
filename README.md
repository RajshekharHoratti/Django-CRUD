# Django-CRUD TO-DO task manager

This is a simple TO-DO task manager.

Tech Stack : Python3, Django, MongoDB, Javascript, Jquery, CSS, Bootstrap

It consist of 2 saperate admin pannel for Superadmin and User

Clone the repo as it is and install all the dependencies from the requirement.txt

  pip install -r requirement.txt

change the database creds accordingly in the .env file in bacis_CRUD_app folder
I have used a localdatabase with
  Database Name: basicDB
  username:""
  password: ""
  URL: localhost


MongoDb Collections used

1: superAdmin
sample data used
{
    "_id" : ObjectId("5d449ff163feced859a65033"),
    "email" : "admin@admin.com",
    "password" : "password",
    "statusCode" : 1,
    "statusMsg" : "Active"
}

2: users
{
    "_id" : ObjectId("5d47dab80a04084bb89f25d3"),
    "email" : "user@user.com",
    "password" : "password",
    "statusCode" : 1,
    "statusMsg" : "Active"
}


3: tasks
{
    "userId" : ObjectId("5d449ff163feced859a65033"),
    "title" : "complete assignment",
    "description" : "dummy project",
    "timing" : "2019-08-05 12:00",
    "statusCode" : 1,
    "statusMsg" : "in progress",
    "createdAt" : 1564783405,
    "modifiedAt" : ,
    "isDeleted" : false
}



the superadmin or the user can add a task but the user will be able to see his respective tasks and update the status and delete it if needed.
and the superadmin can see all the user's data and even update and delete them if needed. 


