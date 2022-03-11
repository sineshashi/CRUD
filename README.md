This project is the solution to the following problem:

        You have to create a simple RESTful API using the following frameworks and packages in python.
        Connexion - https://github.com/zalando/connexion
        Open API Specification - https://swagger.io/specification/
        SQLAlchemy - https://www.sqlalchemy.org/
        Marshmallow - https://marshmallow.readthedocs.io/en/stable/
        Marshmallow-sqlalchemy - https://marshmallow-sqlalchemy.readthedocs.io/en/latest/
        Pytest - https://docs.pytest.org/en/6.2.x/

        By using these tools, create a RESTful API for the CRUD(Create, Read, Update, Delete) operations for a single model. Also you need to write basic unit tests to test the API. Model fields are listed below.

        Model Fields
            Id: Integer
            Checked: Boolean
            Name: String
            Type : String
            Age: Number
            Description: String
            Date: Datetime


Guide for using repository (windows):

    After cloning the repository.
    Create virtual environment using following command:
        python -m venv env
       
    Activate environment using:
        ./env/Scripts/activate
    
    Install all the required packages and dependencies using command:
        pip install requirements.txt

    Now go to Project directory using cd ./Project and migrate using the command:
        python migrate.py 
            This command will create table in the database. Here sqlite is set default. 

    Now start the server using following command:
        python startserver.py

    base_url/ui more specifically for default connexion server http://192.168.43.46:8080/ui/ will show swagger specification where all the info about APIs can be obtained.

Usage of different modules and packages:

    1) OpenAPI Specification:
        This is a way of creating Open API documentation by creating a .json or .yaml file.
        In this project, a file named openapi.yaml has been created which consists of the details and specifications of APIs created in the project.

    2) Connexion: 
        This is a webframework which gaurantees the mapping of urls mentioned in the open api specification with the corresponding python functions or classes.
        In this prject, a file named startserver.py has been created which maps the APIs with the functions of api.py file created in app folder, and starts a default flask server for us too.
    
    3) SQLAlchemy:
        This is a package which provides a Object Relational Mapper to interact with the database. Using this orm, we can create tables and manipulate data of the table.
        In this project, models.py file in app folder, has the required model created by using sqlalchemy. The file migrate.py when executed creates the table of this model in the database. Since SQLAlchemy works on the sessions so a file db.py in app folder, has been created which has all the code to connect with the data base.
        Whenever we need to connect with database we import session from db.py file and start the session.
        This package has been used as ORM so api.py file which handles requests, also uses this to fetch, insert or maniulate data of database.

    4) Marshmallow and marshmallow-sqlalchemy:
        Marshmallow is a packages which is used for serialization and deserialization while marshmallow-sqlalchemy is package built on the top of Marshmallow with sqlalchemy. Marshmallow-sqlalchemy automatically creates the schema of a sqlalchemy model.
        Here schema.py file in app folder, has been created which has schema for the model, using marshmallow and marshmallow-sqlalchemy. The schema in this file has been used to serialize and deserialze the data in api.py file.

    5) Pytest has been used to test the APIs. The test_api.py file in app folder has tests for each route and each operation on that route. Using command:
        pytest
    all the tests can be tested in a simulatneously. Or we can test them one by one too.

