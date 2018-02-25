from __future__ import unicode_literals
from django.db import models

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models

class Assistants(models.Model):
    person_name = models.CharField(db_column='Person_Name', max_length=64) # Field name made lowercase.
    ccn = models.IntegerField(db_column='CCN', primary_key=True) # Field name made lowercase.
    officer = models.TextField(db_column='Officer', blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        managed = False
        db_table = 'Assistants'

class Buildings(models.Model):
    building_name = models.CharField(db_column='Building_Name', primary_key=True, max_length=12) # Field name made lowercase.
    history = models.CharField(db_column='History', max_length=512, blank=True) # Field name made lowercase.
    built = models.DateField(db_column='Built', blank=True, null=True) # Field name made lowercase.
    namesake = models.CharField(db_column='Namesake', max_length=64, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Buildings'

class Courses(models.Model):
    ccn = models.IntegerField(db_column='CCN', primary_key=True) # Field name made lowercase.
    course_title = models.CharField(db_column='Course_Title', max_length=64) # Field name made lowercase.
    course_code = models.CharField(db_column='Course_Code', max_length=12) # Field name made lowercase.
    section_no = models.IntegerField(db_column='Section_No') # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=512, blank=True) # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=32, blank=True) # Field name made lowercase.
    room_no = models.CharField(db_column='Room_No', max_length=8, blank=True) # Field name made lowercase.
    building_name = models.CharField(db_column='Building_Name', max_length=12, blank=True) # Field name made lowercase.
    course_type = models.CharField(db_column='Course_Type', max_length=3, blank=True) # Field name made lowercase.
    units = models.IntegerField(db_column='Units', blank=True, null=True) # Field name made lowercase.
    exam = models.IntegerField(db_column='Exam', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Courses'

class Professors(models.Model):
    professor_name = models.CharField(db_column='Professor_Name', primary_key=True, max_length=64) # Field name made lowercase.
    ccn = models.IntegerField(db_column='CCN', blank=True, null=True) # Field name made lowercase.
    rating = models.FloatField(db_column='Rating', blank=True, null=True) # Field name made lowercase.
    salary = models.FloatField(db_column='Salary', blank=True, null=True) # Field name made lowercase.
    position = models.CharField(db_column='Position', max_length=64, blank=True) # Field name made lowercase.
    homepage = models.CharField(db_column='Homepage', max_length=128, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Professors'

class Tutors(models.Model):
    person_name = models.CharField(db_column='Person_Name', primary_key=True, max_length=64) # Field name made lowercase.
    course_codes = models.CharField(db_column='Course_Codes', max_length=256, blank=True) # Field name made lowercase.
    day = models.CharField(db_column='Day', max_length=10, blank=True) # Field name made lowercase.    
    time = models.CharField(db_column='Time', max_length=12, blank=True) # Field name made lowercase.
    building_name = models.CharField(db_column='Building_Name', max_length=12, blank=True) # Field name made lowercase.
    room_no = models.CharField(db_column='Room_No', max_length=8, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Tutors'

