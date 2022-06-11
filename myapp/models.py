# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    name = models.CharField(max_length=50)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class DjangoContentType(models.Model):
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Photo(models.Model):
    photoid = models.AutoField(primary_key=True)
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    filename = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'photo'


class Plant(models.Model):
    cntntsno = models.IntegerField(db_column='cntntsNo', primary_key=True)  # Field name made lowercase.
    plntbnenm = models.CharField(db_column='plntbneNm', max_length=45, blank=True, null=True)  # Field name made lowercase.
    lighttdemanddocode = models.CharField(db_column='lighttdemanddoCode', max_length=45, blank=True, null=True)  # Field name made lowercase.
    managelevelcode = models.CharField(db_column='managelevelCode', max_length=45, blank=True, null=True)  # Field name made lowercase.
    adviseinfo = models.CharField(db_column='adviseInfo', max_length=300, blank=True, null=True)  # Field name made lowercase.
    lowtp = models.IntegerField(db_column='lowTp', blank=True, null=True)  # Field name made lowercase.
    toptp = models.IntegerField(db_column='topTp', blank=True, null=True)  # Field name made lowercase.
    midtp = models.IntegerField(db_column='midTp', blank=True, null=True)  # Field name made lowercase.
    lowhd = models.IntegerField(db_column='lowHd', blank=True, null=True)  # Field name made lowercase.
    tophd = models.IntegerField(db_column='topHd', blank=True, null=True)  # Field name made lowercase.
    midhd = models.IntegerField(db_column='midHd', blank=True, null=True)  # Field name made lowercase.
    fmlnm = models.CharField(db_column='fmlNm', max_length=45, blank=True, null=True)  # Field name made lowercase.
    soilhd = models.IntegerField(blank=True, null=True)
    minlight = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plant'


class Plantmanage(models.Model):
    num = models.AutoField(primary_key=True)
    userid = models.CharField(db_column='userID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    luxdate = models.DateTimeField(db_column='luxDate', blank=True, null=True)  # Field name made lowercase.
    waterdate = models.DateTimeField(db_column='waterDate',auto_now= True) # 바뀐점!!!
    plant = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plantmanage'


class Rasdata(models.Model):
    temp = models.FloatField(blank=True, null=True)
    humid = models.FloatField(blank=True, null=True)
    light = models.FloatField(blank=True, null=True)
    soil_hum = models.FloatField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        managed = False
        db_table = 'rasData'


class Test(models.Model):
   # rasnum = models.TextField(blank=True, null=True)
   # num = models.IntegerField(db_column='NUM', blank=True, null=True)  # Field name made lowercase.
    temp = models.IntegerField(blank=True, null=True)
    humid = models.IntegerField(blank=True, null=True)
    light = models.IntegerField(blank=True, null=True)
    soil_hum = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(db_column='date', auto_now = True)

    class Meta:
        managed = False
        db_table = 'test'


class User(models.Model):
    userid = models.CharField(db_column='userID',primary_key=True, max_length=50)  # Field name made lowercase.
    userpassword = models.CharField(db_column='userPassword', max_length=50)  # Field name made lowercase.
    username = models.CharField(db_column='userName', max_length=50)  # Field name made lowercase.
    userbirth = models.CharField(db_column='userBirth', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'



class UserImage(models.Model):
    user = models.CharField(primary_key=True,max_length=50)
    userimage = models.ImageField(db_column='userImage', upload_to='')  # Field name made lowercase.
    plantname = models.CharField(db_column="plantName", max_length=50)

    class Meta:
        managed = False
        db_table = 'userImage'
