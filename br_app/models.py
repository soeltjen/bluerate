from django.db import models

# Create your models here.
class Officer(models.Model):
    badgenumber = models.IntegerField(db_column='badgeNumber', blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=45)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=45)  # Field name made lowercase.
    city = models.CharField(max_length=45, blank=True, null=True)
    numberstars = models.IntegerField(db_column='numberStars', blank=True, null=True)  # Field name made lowercase.
    profile_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'officer'


class Review(models.Model):
    subject = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    user = models.OneToOneField('User', models.DO_NOTHING, primary_key=True)
    officer = models.OneToOneField('Officer', models.DO_NOTHING)
    stars = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'review'
        unique_together = (('user', 'officer'),)


class User(models.Model):
    u_profile_id = models.AutoField(primary_key=True, default=1)
    firstname = models.CharField(db_column='firstName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'user'
