
# Personal assistant

With this project I want to create a personal assistant that makes my daily tasks easier.

I want to cover the following aspects:



## Features

These are desirable features, I will be adding this functionality by steps, by doing a top down prioritization.
But hopefully all features will be added in the end to conclude the proyect, at least, to conclude the first development phase.

- Works through telegram
- Configure different users with different permissions
- Create grocery list
- Set reminders
- Get some statistics (TBD)



## Documentation

On this early step I only want to set the basic premisses that I considered to build this:

- There will be a database (SQL because I already know how to handle easily)
- It will work using an ORM and database migrations (alembic) to create the tables based on the considered
- There will be initialized by using a script.

## Configuration file

The project works by consuming a config.ini file, the following structure is neccesary:

[DEFAULT] 
TOKEN = <TELEGRAM TOKEN>
DB_CONNECTION = <CONNECTION STRING>

if there were missing config, the project will throw an exception
