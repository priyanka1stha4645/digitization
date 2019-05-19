from django.db import models

# Create your models here.
class daily(models.Model):
	std_id = models.CharField(max_length=20)
	roll_no= models.IntegerField()
	std_name = models.CharField(max_length=100)
	date= models.DateField()
	period = models.CharField(max_length=20)
	attendance = models.BinaryField()
	faculty = models.CharField(max_length=20)
	batch = models.IntegerField()


class monthly(models.Model):
	std_id = models.CharField(max_length=20)
	roll_no= models.IntegerField()
	std_name = models.CharField(max_length=100)
	month =  models.CharField(max_length=3)
	year = models.CharField(max_length=8)
	present_days = models.IntegerField(default=30)
	absent_days = models.IntegerField()
	working_days = models.IntegerField()
	faculty = models.CharField(max_length=20)
	batch = models.IntegerField()

class Meta:
		db_table = "daily"
# class Meta:
# 		db_table = "monthly"