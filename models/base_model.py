#!/usr/bin/python3

"""Importing the modules we will use"""

from datetime import datetime
import uuid

"""Creating the BaseModel class"""
class BaseModel:
    """ Istantiating the new  model"""
    def __init__(self, *args, **kwargs):
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """returns a string version of the instance"""
        cls = str(type(self)).split('.')[-1].split('\'')[0]
        return f'[{cls}] ({self.id}) {self.__dict__}'
    
    def save(self):
        """Saves updated at with the current time"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()
        

    def to_dict(self):
        """ Returns a dictionary with all key values of __dict__"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':(str(type(self)).split('.')[-1].split('\'')[0])})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary