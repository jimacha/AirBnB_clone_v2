#!/usr/bin/python3

import uuid
import datetime

class BaseModel:
    """
    Represents the BaseModel of the hbnb project.
    """
    def _init_(self, *args, **kwargs):
        """
        Initialize a new BaseModel.

        Args:
        *args (any): Unused.
        **kwargs (dict): Key/value pairs of attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items()
            if k == "created_at" or k == "updated_at":
                self._dict_[k] = datetime.datetime.strptime(v, tform
                        else:
                        self._dict_[k] = v
                        else:
                        # models.storage.new(self) -- not sure what this does, so it's commented out
                        pass

                        def save(self):
                        """
                        Update updated_at with the current datetime.
                        """
                        self.updated_at = datetime.datetime.today()
                        # models.storage.save() -- not sure what this does, so it's commented out
                        pass

                        def to_dict(self):
                        """
                        Return the dictionary of the BaseModel instance. 
                        Includes the key/value pair _class_ representing the class name of the object.
                        """
                        rdict = self._dict_.copy()
                        rdict["created_at"] = self.created_at.isoformat()
                        rdict["updated_at"] = self.updated_at.isoformat()
                        rdict["_class"] = self.__class.__name_
                        return rdict

                        def _str_(self):
                        """
                        Return the print/str representation of the BaseModel instance.
                        """
                        clname = self._class.__name_
                        return "[{}] ({}) {}".format(clname, self.id, self._dict_)
