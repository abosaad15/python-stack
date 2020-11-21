from django.db import models
import datetime
# Create your models here.


class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name should be at least 2 characters"
        if len(postData['password']) < 8:
            errors["password"] = "Password should be at least 8 characters"
        return errors

class TripManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['dest']) < 3:
            errors["dest"] = "destination must be at least 3 characters"
        if len(postData['plan']) < 3:
            errors["plan"] = "plan must be at least 3 characters"

        if len(postData['start_date']) == 0:
            errors["start_date"] = "you must include a start date"
        if len(postData['end_date']) == 0:
            errors["end_date"] = "you must include an end date"

        if postData['start_date'] <= str(datetime.date.today()):
            errors["start_date"] = "Start Date must be in future"

        if postData['end_date'] <= postData['start_date']:
            errors["end_date"] = "End Date must be after the Start Date"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    # trips list
    # joined_trips list


class Trip(models.Model):
    dest = models.CharField(max_length = 255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    plan = models.TextField()
    user = models.ForeignKey(User, related_name = 'trips', on_delete = models.CASCADE)
    jointed_users = models.ManyToManyField(User, related_name = 'joined_trips')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = TripManager()
