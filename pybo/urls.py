from django.urls import path

from . import views

app_name = 'pybo'#url 네임 스페이스로 다른 앱이 추가되어 별칭이 같아도 사용할 수 있게

urlpatterns = [
    path('', views.index, name='index'),#8000/pybo 뒤에 index 밑에는 /pybo2와 같은 detail부여 이걸로 템플릿에서 사용가능
    path('<int:question_id>/', views.detail, name='detail'),
    #
    path('answer/create/<int:question_id>/',views.answer_create, name='answer_create'),
    #페이지를 호출하면 views.answer_create로 인해 함수가 호출됨 
]