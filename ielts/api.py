from django.http import HttpResponse
from .models import TestAudio,TestAudioandVideo,TestResult,FullTestResult,TestModule,TestQuestion,FullTestQuestion,FullTestModule
from .serializers import AudioSerializer,VidandAudSerializer,ResultSerializer,FullResultSerializer,QuestionsSerializer,FullQuestionsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status




@api_view(['GET','POST'])
def audio_list(request):
    if request.method=='GET':
        audios=TestAudio.objects.all()
        serializer=AudioSerializer(audios, many=True)
        return Response(serializer.data)

    elif request.method=='POST':
        serializer=AudioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def audio_detail(request,pk):
    try:
        audio=TestAudio.objects.get(pk=pk)
    except TestAudio.DoeNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer=AudioSerializer(audio)
        return Response(serializer.data)

@api_view(['GET','POST'])
def video_list(request):
    if request.method=='GET':
        videos=TestAudioandVideo.objects.all()
        serializer=VidandAudSerializer(videos, many=True)
        return Response(serializer.data)

    elif request.method=='POST':
        serializer=VidandAudSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def video_detail(request,pk):
    try:
        video=TestAudioandVideo.objects.get(pk=pk)
    except TestAudioandVideo.DoeNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer=VidandAudSerializer(video)
        return Response(serializer.data)

@api_view(['GET','POST'])
def result_list(request):
    if request.method=='GET':
        results=TestResult.objects.all()
        serializer=ResultSerializer(results,many=True)
        return Response(serializer.data)

    elif request.method=='POST':
        serializer=ResultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def result_detail(request,pk):
    try:
        result=TestResult.objects.get(pk=pk)
    except TestResult.DoeNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer=ResultSerializer(result)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def fullresult_list(request):
    if request.method == 'GET':
        fullresults = FullTestResult.objects.all()
        serializer = FullResultSerializer(fullresults, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FullResultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def fullresult_detail(request, pk):
    try:
        fullresult = FullTestResult.objects.get(pk=pk)
    except TestResult.DoeNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FullResultSerializer(fullresult)
        return Response(serializer.data)

@api_view(['GET'])
def getquestions(request,slug):
    if request.method=='GET':
        module=TestModule.objects.get(name=slug)
        questions=TestQuestion.objects.filter(test=module)
        serializer=QuestionsSerializer(questions,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def getfullquestions(request,slug):
    if request.method=='GET':
        module=FullTestModule.objects.get(name=slug)
        questions=FullTestQuestion.objects.filter(full_test=module)
        serializer=FullQuestionsSerializer(questions,many=True)
        return Response(serializer.data)


@api_view(['GET'])
def getmodulequestions(request,slug):
    if request.method=='GET':
        test = TestModule.objects.get(id=slug)
        questions = TestQuestion.objects.filter(test=test)
        result = []
        for question in questions:
            result.append({
                'id': question.id,
                'question': question.question,
                'time': question.time,
            })
        return Response(result)


@api_view(['GET'])
def getfulltestmodulequestions(request,slug):
    if request.method=='GET':
        fulltest = FullTestModule.objects.get(id=slug)
        questions = FullTestQuestion.objects.filter(full_test=fulltest)
        result = []
        for question in questions:
            result.append({
                'id': question.id,
                'question': question.question,
                'time': 10,
            })
        return Response(result)
