from django.db import models
from datetime import date, time

# Create your models here.\

class Student(models.Model):
    candidate_id=models.IntegerField("Id of user", primary_key=True)
    username=models.CharField("Name of user", max_length=50)
    email=models.EmailField("Email")
    phone=models.IntegerField("Phone number")
    password = models.CharField("Password", max_length=25)
     
class Judge(models.Model):
    j_id=models.IntegerField("Id of user", primary_key=True)
    username=models.CharField("Name of user", max_length=50)
    email=models.EmailField("Email")
    phone=models.IntegerField("Phone number") 
    password = models.CharField("Password", max_length=25)
    qualification = models.CharField("Usertype", max_length=25)

class Venue(models.Model):
    venue_id=models.IntegerField("Id of stage", primary_key=True)
    name = models.CharField("name", max_length=30)
    block = models.IntegerField("block")

class Event(models.Model):
    event_id=models.IntegerField("Id of user", primary_key=True)
    pgm_name = models.CharField("prog_name", max_length=30)
    venue_id=models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


class Accomodation(models.Model):
    acc_id=models.IntegerField("id")
    place_name=models.CharField("acco place", max_length=50)
    candidate_id=models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateTimeField()
    
class Result(models.Model):
    event_id=models.ForeignKey(Event, on_delete=models.CASCADE)
    candidate_id=models.ForeignKey(Student, on_delete=models.CASCADE)
    position=models.IntegerField("position of candidate")
    grade=models.IntegerField("grade of candidate")
    j_id=models.ForeignKey(Judge, on_delete=models.CASCADE)

