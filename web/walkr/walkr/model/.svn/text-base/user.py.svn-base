from walkr.lib.auth import encrypt
from sqlalchemy.ext.associationproxy import association_proxy

class User(object):
    """
    User object for ORM, is initializable
    """
    def __init__(self, username, password=None,
                 fullname=None, email=None):
        self.username = username
        self.password = encrypt(password)
        self.gullname = fullname
        self.email = email
    
    def __repr__(self):
        return "<User %(username)s>" % self.__dict__
    
    roles = association_proxy('_roles', 'name')

class Role(object):
    """
    User Role object for ORM, is initializable. Users may belong to any number of Roles
    """
    def __init__(self, name=None):
        self.name = name
    def __repr__(self):
        return "<Role %(name)s>" % self.__dict__
