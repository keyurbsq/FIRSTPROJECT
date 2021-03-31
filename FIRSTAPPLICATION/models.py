from django.db import models


# # Create your models here.
# #
# class NameInfo(models.Model):
#     name = models.CharField(max_length=30)
#
#
# class IDInfo(models.Model):
#     idNum = models.CharField(max_length=30)
#
#
# class ContactInfo(models.Model):
#     contact = models.CharField(max_length=30)
#
#
# class AddressInfo(models.Model):
#     address = models.CharField(max_length=30)
#
#
class NameInfo1(models.Model):
    name = models.CharField(max_length=30)


class IDInfo1(models.Model):
    idNum = models.CharField(max_length=30)


class ContactInfo1(models.Model):
    contact = models.CharField(max_length=30)


class AddressInfo1(models.Model):
    address = models.CharField(max_length=30)