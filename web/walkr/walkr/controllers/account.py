""" 
AccountController

Responsible for delegating requests regarding user signin, signout and register.
Delegated to by ``config.routing``'s mapper. Also contains validation for
Usernamesand the Registration form.
"""

import logging

from pylons import request, response, session, url, tmpl_context as c
from pylons.controllers.util import abort, redirect

# import decorators
from pylons.decorators import validate
from pylons.decorators.rest import restrict

from walkr.model import User
from walkr.lib.base import BaseController, render
import walkr.lib.helpers as h
from walkr.model.meta import Session

from sqlalchemy import and_, or_
from sqlalchemy.orm import aliased

log = logging.getLogger(__name__)

import formencode
from formencode import htmlfill, validators as v, FancyValidator
from math import sqrt
from turbomail import Message

class UsernameValidator(FancyValidator):
    """Validates that a username does not exist or contain spaces."""
    def _to_python(self, value, state):
        if ' ' in value:
            raise formencode.Invalid(
                'Usernames cannot contain space characters',
                value, state)
        if h.auth.user_exists(value):
            raise formencode.Invalid(
                'User %s already exists'%value,
                value, state)
        return value
    

class RegisterForm(formencode.Schema):
    """
    Validator for the registration form rendered by 
    ``AccountController.register()``and accepted by 
    ``AccountController.submit()``
    """
    allow_extra_fields = True
    filter_extra_fields = True
    fullname =v.UnicodeString()
    username = formencode.All(v.UnicodeString(not_empty=True), 
                              UsernameValidator())
    password =v.UnicodeString(not_empty=True)
    confirm_password =v.UnicodeString(not_empty=True)
    email =v.Email(not_empty=True)
    confirm_email =v.Email(not_empty=True)
    chained_validators = [v.FieldsMatch('email', 'confirm_email'),
                          v.FieldsMatch('password', 'confirm_password')]



class AccountController(BaseController):


    ''' Controller for handling user account activities. 
    
    Dispatches the registration page, signin/signout and should eventually
    have more functionality for administrative tasks, like listing and deleting
    users. Also will handle updating of user information, such as SEP subject
    areas.
    '''
    def signin(self):
        identity = request.environ.get('repoze.who.identity')
        if identity is not None:
            came_from = request.params.get('came_from', '')
            if request.environ.get('HTTP_REFERER', '').startswith(came_from)\
                or not came_from:
                redirect('/account/profile')
            if came_from:
                redirect(str(came_from))

        c.failed = request.url == request.environ.get('HTTP_REFERER','')

        return render('/account/signin.html')

    def test(self):
        identity = request.environ.get('repoze.who.identity')
        if identity is None:
            # Force skip the StatusCodeRedirect middleware; it was stripping
            #   the WWW-Authenticate header from the 401 response
            request.environ['pylons.status_code_redirect'] = True
            # Return a 401 (Unauthorized) response and signal the repoze.who
            #   basicauth plugin to set the WWW-Authenticate header.
            abort(401, 'You are not authenticated')
        
        return """
<body>
Hello %(name)s, you are logged in as %(username)s.
<a href="/account/signout">logout</a>
</body>
</html>
""" %identity['user']

    def signout(self):
        ''' 
        Action to sign the user out. The actual signout happens when the
        middleware captures the request, so this function just displays a
        confirmation pageFor ``cookie`` authentication this
        function's routing must be added to the ``authkit.cookie.signoutpath``
        directive.
        '''
        return render('account/signedout.html')

    def profile(self):
        if not request.environ.get('REMOTE_USER', False):
            abort(401)
        
        c.user = h.get_user(request.environ['REMOTE_USER'])        

        return render('account/profile.html')

    def register(self):
        '''Renders the registration form.'''
        return render('account/register.html')

    @validate(schema=RegisterForm(), form='register')
    def submit(self):
        ''' 
        This function validates the submitted registration form and creates a
        new user. Restricted to ``POST`` requests. If successful, redirects to 
        the result action to prevent resubmission.
        ''' 
        
        user = User(
            self.form_result['username'],
            self.form_result['password'],
            email=self.form_result['email'],
            fullname=self.form_result['fullname'],
        )


        Session.add(user) 
        Session.commit()
        '''
        msg = Message("syriac@ua.edu", self.form_result['email'], 
                      "Syriac Reference Portal registration")
        msg.plain = """%s, thank you for registering with the Syriac Reference
                       Portal. You can access your """ % self.form_result['username'] 
        msg.send()
        '''
        h.redirect(h.url(controller='account', action='result'))


    def result(self):
        ''' Target of redirect from submit. Simply returns a "Registration
        Successful!" page '''
        return render('account/success.html')


