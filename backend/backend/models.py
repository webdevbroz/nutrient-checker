# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Food(models.Model):
    fdc_id = models.AutoField(primary_key=True)
    data_type = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    food_category_id = models.AutoField()
    publication_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'food'


class FoodNutrient(models.Model):
    fdc_id = models.IntegerField(blank=True, null=True)
    nutrient_id = models.IntegerField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    data_points = models.IntegerField(blank=True, null=True)
    derivation_id = models.IntegerField(blank=True, null=True)
    min = models.FloatField(blank=True, null=True)
    max = models.FloatField(blank=True, null=True)
    median = models.FloatField(blank=True, null=True)
    footnote = models.CharField(max_length=300, blank=True, null=True)
    min_year_acquired = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'food_nutrient'


class Nutrient(models.Model):
    name = models.TextField(blank=True, null=True)
    unit_name = models.CharField(max_length=100, blank=True, null=True)
    rank = models.FloatField(blank=True, null=True)
    nutrient_nbr = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nutrient'


class Test(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test'
