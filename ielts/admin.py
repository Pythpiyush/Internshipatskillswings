from django.contrib import admin
from .models import (
    Test,
    FullTest,
    TestModule,
    FullTestModule,
    TestResult,
    FullTestResult,
    Coupon,
    TestQuestion,
    FullTestQuestion,
    TestAudio,
    TestAudioandVideo
)


ieltsmodels = [Test, FullTest, TestModule,
               FullTestModule, TestResult, FullTestResult, Coupon, TestQuestion, FullTestQuestion,TestAudio,TestAudioandVideo]
admin.site.register(ieltsmodels)
