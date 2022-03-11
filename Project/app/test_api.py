import requests
import json



def main_url():
    return "http://192.168.43.46:8080/"


def test_listProfile(): # Test for the get request which returns all the profiles
    url = main_url() + "profile"
    response = requests.get(url)
    assert response.status_code == 200, "Status Code do not match."
    response_data = json.loads(response.text) 
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
    response_data.pop('id') #removing id from the data so that we can match with the request data.
    assert response_data == {
        "name": "Steve Rogers",
        "checked": False,
        "age": 25,
        "description": "Developer",
        "type": "Python",
        "date": "2022-03-11T08:50:10.860100"
    }, "Response data does not match."


def test_retrieveProfile(): #Test get request with id.
    id = 2 #Change id to perform test for different IDs.
    url = main_url() + f"profile/{id}"
    response = requests.get(url)
    assert response.status_code == 200, "Status code does not match."
    response_data = json.loads(response.text)
    assert response_data['age'] >= 0, "Invalid age found."



def test_updateProfile(): # Test Put request with id.
    id = 2 #Change id to perform test for different IDs.
    url = main_url() + f"profile/{id}"
    request_data = {
        "name": "Ram",
        "age": 20
    }
    response = requests.put(url, json=request_data)
    assert response.status_code == 200, "Status do not match."
    response_data = json.loads(response.text)
    reqeusted_fields = list(request_data.keys())
    for field in reqeusted_fields: #Checking whether each field of requested data has been updated or not.
        assert response_data[field] == request_data[field], f"{field} data does not match."


def test_deleteProfile(): #Test delete request with id.
    id = 2 #Change id to perform test for another id.
    url = main_url() + f"profile/{id}"
    response = requests.delete(url)
    assert response.status_code == 200, "Status code does not match."
    response_data = json.loads(response.text)
    assert response_data == f"Profile with id {id} has been deleted.", "No deleted response."

