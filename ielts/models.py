from django.db import models
from courses.models import Course
from users.models import User

import uuid


class Test(models.Model):
    course = models.ForeignKey(
        Course, related_name='tests', on_delete=models.CASCADE)
    mid = models.SlugField(max_length=200)
    name = models.CharField(max_length=500)
    introduction = models.TextField()
    how_to_practice = models.TextField()
    is_paid = models.BooleanField(default=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class FullTest(models.Model):
    course = models.ForeignKey(
        Course, related_name='fulltests', on_delete=models.CASCADE)
    fid = models.SlugField(max_length=200)
    name = models.CharField(max_length=500)
    is_paid = models.BooleanField(default=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class TestModule(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    test = models.ForeignKey(
        Test, related_name='testmodule', on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class FullTestModule(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_test = models.ForeignKey(
        FullTest, related_name='fulltestmodule', on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class TestResult(models.Model):
    test = models.ForeignKey(TestModule, related_name='testresult', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fluency = models.IntegerField()
    grammar = models.IntegerField()
    vocab = models.IntegerField()
    pronunciation = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class FullTestResult(models.Model):
    full_test = models.ForeignKey(TestModule, related_name='fulltestresult', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fluency = models.IntegerField()
    grammar = models.IntegerField()
    vocab = models.IntegerField()
    pronunciation = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class TestQuestion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    test = models.ForeignKey(TestModule, on_delete=models.CASCADE)
    question = models.TextField()
    time = models.IntegerField()


class FullTestQuestion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_test = models.ForeignKey(FullTestModule, on_delete=models.CASCADE)
    question = models.TextField()


class TestAudio(models.Model):
    testaudio = models.ForeignKey(
        TestModule, related_name='testaudio', on_delete=models.CASCADE)
    audio = models.FileField(
        upload_to='multimedia/audio', blank=True, null=True)


class TestAudioandVideo(models.Model):
    fulltestaudioandvideo = models.ForeignKey(
        FullTestModule, related_name='fulltestaudioandvideo', on_delete=models.CASCADE)
    video = models.FileField(
        upload_to='multimedia/video', blank=True, null=True)


class Coupon(models.Model):
    name = models.CharField(max_length=20)
    discount = models.IntegerField()  # in percent

    def __str__(self):
        return self.name
