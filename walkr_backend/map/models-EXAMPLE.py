# Dustin Dannenhauer (dtdannen)
# Models class for MySQL database
# Contains set up for the following tables:
# -Problems
# -ContestProblems
# -Contests
# -ContestDates
# -Submissions

# Notes:
# All file name entries have a max_length of 200 characters

from django.db import models
from datetime import datetime

# We are using the built-in user table
from django.contrib.auth.models import User

########## TO-DO: get logging working ########## 
import logging
LOG_FILENAME = 'logs/testing.log'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)
################################################                   

# A User is anyone that would be using the website, competitor or admin
#class Users(models.Model):
#    user_name = models.CharField(primary_key=True,max_length=30)
#    is_admin = models.BooleanField()

    # Every class in models has this function so that this 'object'
    # displays a nice string when looked at, aka just like toString()
#    def __unicode__(self):
#        return self.user_name

# A Problem in this table has:
# -name (plaintext)
# -description (plaintext)
# -solution (html)
# -release time
# -close time
class Problems(models.Model):
    name = models.CharField(primary_key=True,max_length=50)
    description = models.TextField()
    solution = models.TextField()
    start_time = models.DateTimeField()
    close_time = models.DateTimeField()
    points = models.IntegerField() # Max number of points this problem is worth
    author = models.CharField(max_length=50)

    # As soon as this object is created, auto_now_add=True sets
    # this to the datetime
    creation_date = models.DateTimeField(auto_now_add=True) 

    # This function takes the current time and returns
    # the status (as a string) of the problem which is 
    # one of four possibilities
    # 1. Waiting - Problem has not become available yet
    # 2. Open - Problem is currently available and awaiting submissions
    # 3. Closed - Problem has closed
    # TO-DO:
    # 4. Overtime - Problme has closed but there have been no correct submissions yet
    def status(self):
        curr_time = datetime.now()
        if curr_time < self.start_time:
            return "waiting"
        elif curr_time < self.close_time:
            return "open"
        elif self.any_correct_non_admin_submissions():
            return "closed"
        else:
            return "overtime"
        
        
    # Returns True iff there exists a correct submission
    # for this problem that is not from an admin
    def any_correct_non_admin_submissions(self):
        submissions_for_this_problem = Submissions.objects.filter(problem_name=self.name)
        #logging.debug('There are ' + submissions_for_this_problems.length + ' submissions for ' + self.name)
        
        # For all the correct submissions, if there exists one by a user who is not an admin
        # return True, otherwise return false
        for s in submissions_for_this_problem:
            if s.is_correct and not s.user.is_staff:
                return True

        return False
                

    def __unicode__(self):
        return self.name

# Connects each contest with the problems that were used for that contest
class ContestProblems(models.Model):
    # Contest's have a name to allow them to be re-used (aka have multiple dates)
    name = models.ForeignKey('Contests')
    name = models.ForeignKey('Problems')

    def __unicode__(self):
        return str(self.problem_name) + " in " + str(self.contest_name)

# A Contest has a unique name, author, and creation date
class Contests(models.Model):
    name = models.CharField(primary_key=True,max_length=50)
    author = models.CharField(max_length=50)
    creation_date = models.DateField(auto_now_add=True)
    #is_finished = models.BooleanField()  #Possible addition

    def __unicode__(self):
        return self.name

# Connects a contest to all the dates it was used (to keep track of what days contests were used)
class ContestDates(models.Model):
    name = models.ForeignKey('Contests')
    date = models.DateField()
    
    def __unicode__(self):
        return str(self.contest_name) + " on " + str(self.contest_date)

# Keeps track of every file submitted by each user for each contest for each problem
# Note: Might be good to break this table up in the future, it could get very big...
class Submissions(models.Model):
    user = models.ForeignKey(User)
    problem_name = models.ForeignKey('Problems')
    contest_name = models.ForeignKey('Contests')
    is_correct = models.BooleanField()
    score = models.IntegerField() # This value should always be <= than the Problems.points field
    file_name = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True) # grab the timestamp at the time of submission
    
    def __unicode__(self):
        return str(self.user.username) + " submitted for " + str(self.problem_name) + " on " + str(self.timestamp)
    


