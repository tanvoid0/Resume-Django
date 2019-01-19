from django.db import models


# Create your models here.
class Info(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    dob = models.DateField('Date of Birth')
    address = models.TextField(max_length=200)
    nationality = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    about = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


class Social(models.Model):
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, default=None, blank=True, null=True)
    def __str__(self):
        return self.name


class Hobby(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Skill(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Sub_Skill(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default=None, blank=True, null=True)
    proficiency = models.IntegerField()

    def __str__(self):
        return self.name


class Education(models.Model):
    degree = models.CharField(max_length=50)
    institution = models.CharField(max_length=50)
    start = models.IntegerField()
    end = models.IntegerField(default=None, blank=True, null=True)
    pass_year = models.IntegerField(default=None, blank=True, null=True)
    gpa = models.FloatField()
    description = models.TextField(default=None, blank=True, null=True)

    def __str__(self):
        return self.degree

    class Meta:
        ordering = ['-end']

class Training(models.Model):
    name = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    start = models.IntegerField()
    end = models.IntegerField(default=None, blank=True, null=True)
    pass_year = models.IntegerField(default=None, blank=True, null=True)
    description = models.TextField(default=None, blank=True, null=True)

    def __str__(self):
        return self.name


class Training_Topic(models.Model):
    training = models.ForeignKey(Training, on_delete=models.CASCADE)
    topic = models.CharField(max_length=100)

    def __str__(self):
        return self.topic


class Work(models.Model):
    role = models.CharField(max_length=100)
    institution  = models.CharField(max_length=100)
    start = models.IntegerField()
    end = models.IntegerField(default=None, blank=True, null=True)
    contract_year = models.IntegerField(default=None, blank=True, null=True)
    description = models.TextField(default=None, blank=True, null=True)

    def __str__(self):
        return self.institution


class Project_Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    category = models.ForeignKey(Project_Category, on_delete=models.CASCADE)
    image = models.CharField(max_length=200)
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


class Fact(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=100, default='')
    icon = models.CharField(max_length=100, default='')
    quantity = models.IntegerField()

    def __str__(self):
        return self.name+": "+str(self.quantity)

    class Meta:
        ordering = ['name']
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=200)
    designation = models.CharField(max_length=100)
    message = models.CharField(max_length=100)

    def __str__(self):
        return self.name+ ": "+self.message
