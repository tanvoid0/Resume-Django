from django.db import models

# Create your models here.

class Project_Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200, default=None, blank=True, null=True)
    category = models.ForeignKey(Project_Category, on_delete=models.CASCADE)
    image = models.CharField(max_length=200, default=None, blank=True, null=True)
    icon = models.CharField(max_length=100, default=None, blank=True, null=True)
    language_and_framework = models.CharField(max_length=200, default=None, blank=True, null=True)
    description = models.TextField(default=None, blank=True, null=True)

    def __str__(self):
        return self.name



class Project_Feature(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    feature = models.CharField(max_length=100)

    def __str__(self):
        return self.feature


class Project_Tag(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag

