# CourseCatalog
*beta version* 
[Link](https://coursecatalog-api.herokuapp.com/)
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [API](#api)

## General infoT
This is a course catalog that has a number of endpoints(API) for interacting with courses. 

## Technologies
Project is created with:
* Python 3.8
* Django 3.1
* Django-rest-framework
* Postman
* Git
* Heroku
	
## Setup
To run this project, do this:

1) Clone project in your PC
```
$ git clone https://github.com/Grayder0152/CourseCatalog.git
```
2) Go to the root directory of the project and install requirements:
```
$ pip install -r requirements.txt
```
3) You can use an existing database(`db.sqlite3`) in which there are several courses or delete it and Django will create a new empty one automatically.
4) Then you have to make migrations(if you deleted existing database)
```
$ python manage.py makemigrations
$ python manage.py migrate
```
5) Finally, run the server and use API.
```
$ python manage.py runserver
```
## API
The CRUD API interface is implemented on the site. You can see its documentation [here](https://documenter.getpostman.com/view/14942069/TzJx8bqZ)
