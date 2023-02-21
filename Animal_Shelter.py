# Anthony Vigil
# CS-340 Client/Server Development

from pymongo import MongoClient
from bson.objectid import ObjectId
from pprint import pprint
#import unittest

print('Welcome to the Animal Application')
#globally needed variables
userCreateData = {}   #input data 
userSearchTarget = {}  #target data
userUpdateFromTarget = {}  #update data 
userUpdateToTarget = {}  #update data 
userDeleteTarget = {}  #delete data 

#class
class AnimalShelter(object):
    """CRUD Operations for Animal collection in MongoDB"""
    def __init__(self, user, password):
            # Initializing the MongoClient. This helps to
            # access the MongoDB databases and collections.
            self.client = MongoClient('mongodb://%s:%s@localhost:52117/AAC' % (user, password))
            self.database = self.client['AAC']

    #obtain create data from user
    def obtainCreateData(self):
        #table to ensure data dict conforms to the expected format
        values = ['1', 'age_upon_outcome', 'animal_id', 'animal_type', 'breed', 'color', 'date_of_birth', 'datetime', 
          'monthyear', 'name', 'outcome_subtype', 'outcome_type', 'sex_upon_outcome', 'location_lat', 
          'location_long', 'age_upon_outcome_in_weeks']
        #loop to obtain input values from the user
        for i in range (len(values)):
            key = values[i]
            value = input("Enter " + values[i] + ": ")
            userCreateData.update({key: value})          #creates dict item with user input data
        #pprint(userCreateData)   <- FOR TESTING
        #print(type(userCreateData))  <- FOR TESTING
        
    #C operation for C in CRUD        
    def create(self, data):
        
        #use try/except block for boolean processing
        try:
            if data is not None:
                #print(type(data))  Confirm data
                insert_result = self.database.animals.insert_one(data)     # data should be dictionary
                pprint(insert_result)
                #print("True")  
                return True    #return value 
            else:
                # error message
                raise Exception("Nothing to save, because the data parameter is empty")
        except:
            #print("False")  
            return False     #return value
            
    #obtain target data for R in CRUD
    def obtainReadData(self):
        
        #loop to obtain a key/value pair
        for i in range(1):
            key = input("Enter search key: ")
            value = input("Enter search value: ")
            userSearchTarget.update({key: value})    #creates dict object to hold search terms
        #pprint(userSearchTarget) Testing
        #print(type(userSearchTarget)) Testing

    #R operation for R in CRUD
    def read(self, target):
        # try/except block for testing in the unit tests
        try:
            if target is not None:
                #print(type(target))       # dictionary
                read_result = list(self.database.animals.find(target, {"_id": False}))
                #pprint(read_result)   # displays results
                return read_result
            else:
                #lets the user know there was a problem
                raise Exception("Nothing to search, because the target parameter is empty")
                return False
        except Exception as e:
            print("An exception occurred: ", e)
    
    #obtain target data for U in CRUD
    def obtainUpdateData(self):
        #loop to obtain a key/value pair
        for i in range(1):
            key = input("Enter update key: ")
            value = input("Enter update value: ")
        userUpdateFromTarget.update({key: value})
        #obtain new data to change the target to
        for i in range(1):
            key = input("Enter update key: ")
            value = input("Enter new update value: ")
        userUpdateToTarget.update({'$set': {key: value}})
        print(userUpdateToTarget)

    #U operation for U in CRUD
    def update(self, fromTarget, toTarget, count):
        if fromTarget is not None:
            if count == 1:
                update_result = self.database.animals.update_one(fromTarget, toTarget)
                pprint("Matched Count: " + str(update_result.matched_count) + ", Modified Count: " + str(update_result.modified_count))
                if update_result.modified_count == 1:
                    print("Success!")
                    print(update_result)
                    return True
                else:
                    print("Something went wrong")
                    return False
            elif count == 2:
                update_result = self.database.animals.update_many(fromTarget, toTarget)
                pprint("Matched Count: " + str(update_result.matched_count) + ", Modified Count: " + str(update_result.modified_count))
                if update_result.modified_count == update_result.matched_count:
                    print("Success!")
                    print(update_result)
                    return True
                else:
                    print("Something went wrong, all items matching the target may not have been updated. Run a search to verify")
                    print(update_result)
                    return True
            else:
                print("Count not recognized - try again.")
                return False
        else:
            #lets the user know there was a problem
            raise Exception("Nothing to update, because at least one of the target parameters is empty")
            return False
    #obtain target data for D in CRUD
    def obtainDeleteData(self):
        #loop to obtain key/value pair
        for i in range(1):
            key = input("Enter delete key: ")
            value = input("Enter delete value: ")
            userDeleteTarget.update({key: value})
    #delete function for either single or many
    def deleteData(self, target, count):
        if target is not None:
            if count == 1:
                try:
                    delete_result = self.database.animals.delete_one(target)
                    pprint("Deleted Count: " + str(delete_result.deleted_count))
                    if delete_result.deleted_count == 0:
                        print("Nothing to be deleted using the target data.")
                        print(delete_result)
                        return True
                    else:
                        print("Success!")
                        print(delete_result)
                        return True
                except Exception as e:
                    print("An exception has occurred: ", e)
            elif count == 2:
                try:
                    delete_result = self.database.animals.delete_many(target)
                    pprint("Deleted Count: " + str(delete_result.deleted_count))
                    if delete_result.deleted_count == 0:
                        print("Nothing to be deleted using the target data.")
                        print(delete_result)
                        return True
                    else:
                        print("Success!")
                        print(delete_result)
                        return True
                except Exception as e:
                    print("An exception has occurred: ", e)
                    return False
            else:
                print("Count not recognized - try again.")
                return False
        else:
            #lets the user know there was a problem
            raise Exception("Nothing to delete, because the target parameter is empty")
            return False
            

#Shelter1 = AnimalShelter() Testing
#Shelter1.obtainCreateData() Testing
#Shelter1.obtainReadData() Testing
        

# a sample data set for the create method that does work
sampleData = {
        '1': 3,
        'age_upon_outcome': '35 years',
        'animal_id': 'AAAA',
        'animal_type': 'Dogecoin',
        'breed': 'crypto',
        'color': 'green',
        'date_of_birth': 'wonder-years',
        'datetime': '2020-05-10 10:49:00',
        'monthyear': '2020-05-10T10:49:00',
        'name': 'monkeyboy',
        'outcome_subtype': 'SCRP',
        'outcome_type': 'super-transfer',
        'sex_upon_outcome': 'non-spayed',
        'location_lat': 30.6525984,
        'location_long': -97.74199,
        'age_upon_outcome_in_weeks': '450.454'
}
#a sample search
sampleTarget = {
    'animal_type': 'Dogecoin'
}
#a sample update element with 1 element
sampleUpdate = {'$set': {'name': '42'}}

#a sample update with multiple elements
sampleUpdateTwoField= { '$set': {
    'name': '42',
    'animal_type': 'Jaguar'}
}
#sample delete element
sampleDelete = {
    'name': 'Zz'
}