# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class WheelSpecificationSubmission(models.Model):
    form_number = models.CharField(unique=True, max_length=150)
    submitted_by = models.CharField(max_length=255)
    submitted_date = models.DateField()
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wheel_specification_submission'
        app_label = 'kpa_app'


class WheelSpecification(models.Model):
    submission = models.ForeignKey('WheelSpecificationSubmission', models.DO_NOTHING)
    axle_box_housing_bore_dia = models.CharField(max_length=50, blank=True, null=True)
    bearing_seat_diameter = models.CharField(max_length=50, blank=True, null=True)
    condemning_dia = models.CharField(max_length=50, blank=True, null=True)
    intermediate_wwp = models.CharField(max_length=50, blank=True, null=True)
    last_shop_issue_size = models.CharField(max_length=50, blank=True, null=True)
    roller_bearing_bore_dia = models.CharField(max_length=50, blank=True, null=True)
    roller_bearing_outer_dia = models.CharField(max_length=50, blank=True, null=True)
    roller_bearing_width = models.CharField(max_length=50, blank=True, null=True)
    tread_diameter_new = models.CharField(max_length=50, blank=True, null=True)
    variation_same_axle = models.CharField(max_length=20, blank=True, null=True)
    variation_same_bogie = models.CharField(max_length=20, blank=True, null=True)
    variation_same_coach = models.CharField(max_length=20, blank=True, null=True)
    wheel_disc_width = models.CharField(max_length=50, blank=True, null=True)
    wheel_gauge = models.CharField(max_length=50, blank=True, null=True)
    wheel_profile = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wheel_specification'
        app_label = 'kpa_app'