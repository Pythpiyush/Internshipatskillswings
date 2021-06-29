from django.shortcuts import render, HttpResponse, redirect
from courses.models import Course
from ielts.models import Test, Coupon, FullTest, TestModule, TestResult, FullTestResult, FullTestModule,TestQuestion,FullTestQuestion

def ielts(request):
    course = Course.objects.get(cid='ielts')
    tests = Test.objects.all()
    full_tests = FullTest.objects.all()
    return render(request, 'ielts/ielts.html', {'course': course, 'tests': tests, 'full_tests': full_tests})


def ielts_test(request, slug):
    course = Course.objects.get(cid='ielts')
    test = Test.objects.get(mid=slug)
    testmodules = TestModule.objects.filter(test=test)
    return render(request, 'ielts/ielts_test.html', {'course': course, 'test': test, 'testmodules': testmodules})


def result(request, slug):
    incominguser = request.user
    incomingmodule = TestModule.objects.get(name=slug)
    resultobtained = TestResult.objects.filter(
        user=incominguser, testresult=incomingmodule).order_by('-created_at')[0]
    return render(request, 'ielts/result.html', {'result': resultobtained})


def fulltest(request, slug):
    course = Course.objects.get(cid='ielts')
    fulltest = FullTest.objects.get(fid=slug)
    fulltestmodules = FullTestModule.objects.filter(full_test=fulltest)
    return render(request, 'ielts/ielts_full_test.html', {'course': course, 'fulltest': fulltest, 'fulltestmodules': fulltestmodules})


def fullresult(request, slug):
    incominguser = request.user
    incomingmodule = FullTestModule.objects.get(name=slug)
    resultobtained = TestResult.objects.filter(
        user=incominguser, fulltestresult=incomingmodule).order_by('-created_at')[0]
    return render(request, 'ielts/result.html', {'result': resultobtained})


def total(request):
    courseamount = Course.objects.get(cid='ielts').price
    if request.method == 'POST':
        incomingcouponcode = request.POST.get("coupon")
        coupon = Coupon.objects.filter(name=incomingcouponcode)[0]
        print(coupon)
        totalvalue = courseamount-(coupon.discount/100)*courseamount
        return render(request, 'simple.html', {"total": totalvalue})

    return redirect('ielts')


def test_module_answer(request, test, test_module):
    test_name=Test.objects.get(mid=test)
    test_module = TestModule.objects.get(id=test_module)
    test_questions=TestQuestion.objects.filter(test=test_module)
    return render(request, 'ielts/test_module_answer.html', {'test':test_name,'test_module': test_module,'test_questions':test_questions})

def fulltest_module_answer(request, fulltest, fulltest_module):
    full_testname = FullTest.objects.get(fid=fulltest)
    full_test_module = FullTestModule.objects.get(id=fulltest_module)
    full_test_questions = FullTestQuestion.objects.filter(full_test=fulltest_module)
    return render(request, 'ielts/full_test_module_answer.html', {'test':full_testname,'test_module': full_test_module,'test_questions':full_test_questions})


def success(request):
    return HttpResponse("Hello")


def result_page(request):
    return render(request, 'ielts/test_result.html')


# class GetQuestions(APIView):
#     def get(self, request, format=None):
#         test = TestModule.objects.get(name='test module 1')
#         questions = TestQuestion.objects.filter(test=test)
#         result = []
#         for question in questions:
#             result.append({
#                 'id': question.id,
#                 'question': question.question,
#                 'time': question.time,
#             })
#         return Response(result)
