from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base
import connexion
from connexion.resolver import RestyResolver
from subprocess import run


engine = create_engine('sqlite:///db.sqlite')
Session = sessionmaker(bind= engine)
session = Session()


def migrate():
    with session:
        Base.metadata.create_all(engine)

def runserver(debug=False):
    app = connexion.App(__name__, specification_dir = './', debug = debug, options={"swagger_ui": True})
    app.add_api('openapi.yaml', resolver = RestyResolver('app.api'))
    app.run(port=8080)



def help():
    print(
        'These are the valid commands \n' 
        'migrate: To migrate the created models to database. \n'
        'runserver: To runserver. \n'
        'runserver --debug : To run server in debug mode. \n'
        'runtests: To run all the tests at once \n'
        'testpost: Tests post method with the default data \n'
        'testlist: Tests the list method \n'
        'testretrieve: Test the retrieve method \n'
        'testdelete: Tests the delete method \n'
        'testput: Tests the update method.'
    )

if __name__ == "__main__":
    import sys
    if sys.argv[1] == 'runserver':
        try:
            if sys.argv[2] == '--debug':
                runserver(debug = True)
        except:
            runserver()


    if sys.argv[1] == 'migrate':
        migrate()

    if sys.argv[1] == 'help':
        help()

    if sys.argv[1] == 'runtests':
        run('pytest -q -s --id 0 ./app/test_api.py::test_all') #Here id will mean nothing because we will override it in the test_all() func.

    if sys.argv[1] == 'testpost':
        run('pytest -q -s --id 0 ./app/test_api.py::test_postProfile') #In post id means nothing but to avoid parameter errors it is being passed here.

    if sys.argv[1] == 'testlist':
        run('pytest -q -s --id 0 ./app/test_api.py::test_listProfile') #id is being passed to avoid parameter errors because of conftest.py file.

    if sys.argv[1] == 'testretrieve':
        print('Please enter the id')
        id = input()
        run(f'pytest -q -s --id {id} ./app/test_api.py::test_retrieveProfile')


    if sys.argv[1] == 'testput':
        print('Please enter the id')
        id = input()
        run(f'pytest -q -s --id {id} ./app/test_api.py::test_updateProfile')


    if sys.argv[1] == 'testdelete':
        print('Please enter the id')
        id = input()
        run(f'pytest -q -s --id {id} ./app/test_api.py::test_deleteProfile')
        
