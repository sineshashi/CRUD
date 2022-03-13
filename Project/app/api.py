from marshmallow import ValidationError
from .models import Profile
from .schema import ProfileSchema
from .db import session


def createProfile(body):
    '''
        post request for creating profile.
    '''
    if len(body.get('name')) == 0: #Checking whether user has passes empty string.
        return "Please provide name.", 406
    if len(body.get('type')) == 0: #Checking whether user has passes empty string.
        return "Please provide type.", 406
    profile_schema = ProfileSchema() 
    try:
        deserialized_data = profile_schema.load(body, session=session) #Deserializing the request data.
    except ValidationError as err: #For any invalid data, raise error.
        return err.messages, 406
    with session:
        profile = Profile(**deserialized_data) #Creating instance with the request data.
        session.add(profile)
        session.commit() #saving data in the data base.
        profile_data = profile_schema.dump(profile) #Getting serialized data of the created profile.
        return profile_data, 200


    
def listProfiles():
    with session:
        profiles_list = session.query(Profile).all() #Get all the profiles.
        profile_schema = ProfileSchema()
        serialized_profiles_list = profile_schema.dump(profiles_list, many=True) #Serialize the profiles.
        return serialized_profiles_list, 200 #Return the list of the profiles.
 


def retrieveProfile(id):
    with session:
        profile = session.get(Profile, id) 
        if profile: #Checking whether a profile of the id exists.
            profile_schema = ProfileSchema()
            data = profile_schema.dump(profile)
            return data, 200
        else: #If there is no profile with provided id raise error.
            return "No such profile found for this id.", 404
        
def updateProfile(id, body):
    with session:
        profile = session.get(Profile, id)
        if profile: #Checking whether a profile of the id exists.
            profile_schema = ProfileSchema(partial=True)
            try:
                deserialized_data = profile_schema.load(body)
            except ValidationError as err:
                return err.messages, 406     
            '''
            Now find get the data for individual fields from the body and the field with this new data.
            '''       
            if deserialized_data.get('name'):
                if len(body.get('name')) == 0: #Checking whether user has passes empty string.
                    return "Please provide name.", 406
                profile.name = deserialized_data['name']
            if deserialized_data.get('checked'):
                profile.checked = deserialized_data['checked']
            if deserialized_data.get('type'):
                if len(body.get('type')) == 0: #Checking whether user has passes empty string.
                    return "Please provide type.", 406
                profile.type = deserialized_data['type']
            if deserialized_data.get('age'):
                profile.age = deserialized_data['age']
            if deserialized_data.get('description'):
                profile.description = deserialized_data['description']
            if deserialized_data.get('date'):
                profile.date = deserialized_data['date']
            session.add(profile)
            session.commit() #Updating the profile with new data.
            response = profile_schema.dump(profile)
            return response, 200
        else: #If there is no profile with provided id raise error.
            return "No such profile found for this id.", 404

def deleteProfile(id):
    with session:
        profile = session.get(Profile, id)
        if profile: #Checking whether a profile of the id exists.
            session.delete(profile)
            session.commit()
            return f"Profile with id {id} has been deleted.", 200
        else: #If there is no profile with provided id raise error.
            return "No such profile found for this id.", 404

