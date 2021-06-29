from rest_framework import serializers
from .models import TestAudio,TestAudioandVideo,TestResult,FullTestResult,TestQuestion,FullTestQuestion


class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestAudio
        fields = '__all__'

class VidandAudSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestAudioandVideo
        fields = '__all__'

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestResult
        fields = '__all__'

class FullResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = FullTestResult
        fields = '__all__'

class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestQuestion
        fields = '__all__'

class FullQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FullTestQuestion
        fields = '__all__'