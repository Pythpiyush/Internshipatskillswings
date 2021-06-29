from django.db import models


class Course(models.Model):
    cid = models.SlugField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    course_image = models.ImageField(upload_to='images/course_image', blank=True, null=True)
    display_image = models.ImageField(upload_to='images/display_image', blank=True, null=True)
    video = models.URLField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    student_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name
