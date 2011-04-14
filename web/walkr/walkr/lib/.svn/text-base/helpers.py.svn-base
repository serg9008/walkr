"""Helper functions

Consists of functions to typically be used within templates, but also
available to Controllers. This module is available to templates as 'h'.
"""
# Import helpers as desired, or define your own, ie:
#from webhelpers.html.tags import checkbox, password
from pylons import url
from formbuild import Form
from webhelpers.html.tags import *
from pylons.controllers.util import abort, redirect

#from pylons.controllers.util import abort, redirect

from walkr.lib import auth

from walkr.model.user import User
from walkr.model.meta import Session
from sqlalchemy.orm.attributes import set_attribute, get_attribute 

def get_user(username):
    """
    Returns the User object from the model.

    :rtype: :class:`inphosite.model.User`
    """
    user = Session.query(User).filter_by(username=username.lower()).first()
    return user

def fetch_obj(type, id, error=404, new_id=False):
    """
    Fetches the object with the given id from the collection of type type. If
    the object does not exist, throw an HTTP error (default: 404 Not Found).

    :param type: object type
    :type type: class in :mod:`inphosite.model`
    :param id: object id
    :type id: integer or None
    :param error: HTTP error code.
    :rtype: *type*
    """
    if id is None:
        abort(error)
    obj_q = Session.query(type)
    obj = obj_q.get(int(id))
    #else:
    #    obj = obj_q.filter(type.ID==int(id)).first()

    if obj is None:
        abort(error)
    return obj

def update_obj(obj, attributes, params):
    """
    Updates any arbitrary object. Takes a list of attributes and a dictionary of update
    parameters. Checks if each key is in the list of approved attributes and then attempts
    to set it. If the object does not have that key, throw an HTTP 400 Bad Request

    :param obj: object to update
    :param attributes: list of approved attributes
    :param params: dictionary of update parameters 

    """
    for key in params.keys():
        if key in attributes:
            try:
                set_attribute(obj, key, params[key])
            except:
                abort(400)
    
    Session.flush()

def delete_obj(obj):
    """
    Deletes any arbitrary object from the SQLAlchemy Session and cascades deletes to evaluations.

    :param obj: object to delete

    """
    Session.delete(obj)
    Session.flush()
