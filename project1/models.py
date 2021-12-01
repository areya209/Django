from django.db import models


from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categories(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

class Projects(models.Model):
    Project_id = models.AutoField(primary_key=True)
    Project_name = models.CharField(max_length=50)
    Project_details = models.CharField(max_length=500)
    category = models.ForeignKey(
        'Categories', null=True, on_delete=models.CASCADE)
    Total_target = models.IntegerField()  # 5000
    Total_donations = models.IntegerField()  # 2000
    Avg_rate = models.FloatField()
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Projectcomments(models.Model):
    comment_id = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=1000)
    cproject_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    cuser_id = models.ForeignKey(User, on_delete=models.CASCADE, default=0)


class Commentsreport(models.Model):
    creport_id = models.ForeignKey(Projectcomments, on_delete=models.CASCADE)
    report_comment = models.CharField(max_length=1000)
    reportcommentuser_id = models.ForeignKey(User, on_delete=models.CASCADE, default=0)


class projectreport(models.Model):
    preport_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    report_project = models.CharField(max_length=1000)
    reportprojectuser_id = models.ForeignKey(User, on_delete=models.CASCADE, default=0)


class Projectpictures(models.Model):
    Iproject_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='pics/')



# Create your models here.
