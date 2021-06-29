from django.urls import path
from ielts import views,api

urlpatterns = [
    path('result/', views.result_page, name='test_result'),
    path('getquestions/<str:slug>/', api.getmodulequestions, name='get_questions'),
    path('getfullquestions/<str:slug>/', api.getfulltestmodulequestions, name='get_full_questions'),
    path('test/<str:slug>/', views.ielts_test, name='ielts_test'),
    path('course/fulltest/'+'<str:slug>',views.fulltest, name='ielts_fulltest'),
    # path('result/'+'<str:slug>',views.result,name='ielts_result'),
    # path('fullresult/'+'<str:slug>',views.fullresult,name='ielts_fullresult'),
    path('', views.ielts, name='ielts'),
    path('course/total/', views.total, name='total'),
    path('audio/', api.audio_list),
    path('audio/<int:pk>/', api.audio_detail),
    path('video/', api.video_list),
    path('video/<int:pk>/', api.video_detail),
    path('result/', api.result_list),
    path('result/<int:pk>/', api.result_detail),
    path('fullresult/', api.fullresult_list),
    path('fullresult/<int:pk>/', api.fullresult_detail),
    path('result/<str:slug>', views.result, name='ielts_result'),
    path('fullresult/<str:slug>', views.fullresult, name='ielts_fullresult'),
    path('test/'+'<slug:test>/<uuid:test_module>/', views.test_module_answer, name='test_module_answer'),
    path('<slug:fulltest>/<uuid:fulltest_module>/', views.fulltest_module_answer, name='fulltest_module_answer'),
    path('course/total/', views.total, name='total'),
    path('<str:slug>/', views.ielts_test, name='ielts_test'),
    path('', views.ielts, name='ielts'),
]
