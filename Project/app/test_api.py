import requests
import json
import datetime
    

def main_url():
    return "http://192.168.43.46:8080/"


def test_listProfile(): # Test for the get request which returns all the profiles
    url = main_url() + "profile"
    response = requests.get(url)
    assert response.status_code == 200, "Status Code do not match."
    response_data = json.loads(response.text) 
    print(response_data)
    for profile in response_data: #Verifying whether the age in every profile is greater or equal to zero or not.
        assert profile['age'] >= 0, f"{profile} has invalid age." #Validating age.


def test_postProfile(): #Test the post request for profile.
    url = main_url() + "profile"
    request_data = {
        "name": "Steve Rogers",
        "checked": False,
        "age": 25,
        "description": "Developer",
        "type": "Python",
        "date": "2022-03-11T08:50:10.8601Z"
    }
    response = requests.post(url, json = request_data)
    assert response.status_code == 200, "Sataus Code does not match"
    response_data = json.loads(response.text) #Converting response data to python.
    print(response_data)
    id = response_data.pop('id') #removing id from the data so that we can match with the request data.
    fields = request_data.keys() #All fields whose data has been passed
    for field in fields: #Checking whether each field of requested data has been updated or not.
        if field == "date":
            assert datetime.datetime.strptime(response_data[field], "%Y-%m-%dT%H:%M:%S.%f") == datetime.datetime.strptime(request_data[field], "%Y-%m-%dT%H:%M:%S.%fZ")
        else:
            assert response_data[field] == request_data[field], f"{field} data does not match."
    return id

def test_retrieveProfile(id): #Test get request with id.
    url = main_url() + f"profile/{id}"
    response = requests.get(url)
    assert response.status_code == 200, "Status code does not match."
    response_data = json.loads(response.text)
    print(response_data)
    assert response_data['age'] >= 0, "Invalid age found."



def test_updateProfile(id): # Test Put request with id.
    url = main_url() + f"profile/{id}"
    request_data = {
        "name": "Captain",
        "checked": True,
        "age": 30,
        "description": "Soldier",
        "type": "Commando",
        "date": "2022-03-11T08:50:10.86Z"
    }
    response = requests.put(url, json=request_data)
    assert response.status_code == 200, "Status code does not match."
    response_data = json.loads(response.text)
    print(response_data)
    reqeusted_fields = list(request_data.keys())
    for field in reqeusted_fields: #Checking whether each field of requested data has been updated or not.
        if field == "date":
            assert datetime.datetime.strptime(response_data[field], "%Y-%m-%dT%H:%M:%S.%f") == datetime.datetime.strptime(request_data[field], "%Y-%m-%dT%H:%M:%S.%fZ")
        else:
            assert response_data[field] == request_data[field], f"{field} data does not match."


def test_deleteProfile(id): #Test delete request with id.
    url = main_url() + f"profile/{id}"
    response = requests.delete(url)
    assert response.status_code == 200, "Status code does not match."
    response_data = json.loads(response.text)
    print(response_data)
    assert response_data == f"Profile with id {id} has been deleted.", "No deleted response."

def test_all():
    test_listProfile()
    print('Listing of profiles passed \n')
    id = test_postProfile()
    print('Posting a new profile passed \n')
    test_retrieveProfile(id)
    print('Retrieving of a profile passed \n')
    test_updateProfile(id)
    print('testing for update passed \n')
    test_deleteProfile(id)
    print('deletion passed')
    

