from __future__ import unicode_literals

from django.db import models

import re

# Create your models here.
class UserManager(models.Manager):
    #Update this code with validation functions for input fields,
    #Among other things...
    def validator(self, username, interest):

        LETTERS_ONLY_REGEX = re.compile(r'^[a-zA-Z]+$')
        errorlist = []
        errordict = {
        "entername": "Please insert a first name.",
        "lettersname": "Please ensure that your name field only contains letters.",
        "enterinterest": "Please insert an interest."
        }

        if len(username) < 2:
            errorlist.append("entername")
        elif not LETTERS_ONLY_REGEX.match(username):
            errorlist.append("lettersname")

        if len(interest) < 2:
            errorlist.append("enterinterest")

        if len(errorlist) > 0:
            return False, errorlist, errordict

        currentuser = User.objects.filter(name = username)
        currentinterest = Interest.objects.filter(name = interest)
        #If there is no user with the username currently in the database, create one and put it inside a list
        #so that the data base matches the result of the filter command
        if len(currentuser) == 0:
            currentuser = [self.create(name = username)]
        if len(currentinterest) == 0:
            currentinterest = [Interest.objects.create(name = interest)]

        currentinterest[0].users.add(currentuser[0])

        return True, currentuser, currentinterest




    def login(self, email, password):
        errorlist = []
        errordict = {"enteremail": "Please enter an email address.",
        "emismatch": "Your email address does not appear in our database.  If you do not have an account, please register below.",
        "pmismatch": "Your password does not match our records.  Please try again or create a new account below."}
        if len(email) == 0:
            errorlist.append("enteremail")
        else:
            try:
                selection = registration.objects.get(email = email)
                if bcrypt.hashpw(password.encode(), selection.password.encode()) == selection.password:
                    choice_id = selection.id
                    return True, choice_id
                else:
                    errorlist.append("pmismatch")
            except:
                errorlist.append("emismatch")

        return False, errorlist,errordict

class User(models.Model):
    name = models.CharField(max_length = 45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #May want to make separate userManagers, depending...
    objects = UserManager()

class Interest(models.Model):
    name = models.CharField(max_length = 45)
    users = models.ManyToManyField(User, related_name="interests")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
