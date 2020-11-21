from django.db import models

# Create your models here.


class Course_Description_Manager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        if len(postData['name']) < 6:
            errors['name'] = "The name shoud be more than 5 characters"
        if len(postData['desc']) < 16:
            errors['desc'] = "The description shoud be more than 15 characters"

        return errors

class Course(models.Model):
    name = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = Course_Description_Manager()


class Description(models.Model):
    desc = models.TextField()
    course = models.OneToOneField(Course, on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
