#!/usr/bin/python3
import json

""" A class that serializes instances to a JSON file and deserializes JSON file to instances"""
class FileStorage:
    """This class stores models in json format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns a dictionary of models in storage"""
        return self.__objects
    
    def new(self, obj):
        """Adds a new object to storage"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to a file"""
        with open(FileStorage.__file_path, 'w') as writefile:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, writefile)    

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        """Deserialises the json files"""
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as writefile:
                temp = json.load(writefile)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass