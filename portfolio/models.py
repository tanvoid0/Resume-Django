from django.db import models

# Create your models here.

class Project_Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Project_Feature(models.Model):
    feature = models.CharField(max_length=100)

    def __str__(self):
        return self.feature

class Project_Tag(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag

class Project(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200, default=None, blank=True, null=True)
    category = models.ForeignKey(Project_Category, on_delete=models.CASCADE, default=None, blank=True, null=True)
    image = models.CharField(max_length=200, default=None, blank=True, null=True)
    icon = models.CharField(max_length=100, default=None, blank=True, null=True)
    feature = models.ForeignKey(Project_Feature, on_delete=models.CASCADE, default=None, blank=True, null=True)
    tag = models.ForeignKey(Project_Tag, on_delete=models.CASCADE, default=None, blank=True, null=True)
    description = models.TextField(default=None, blank=True, null=True)

    def __str__(self):
        return self.name






