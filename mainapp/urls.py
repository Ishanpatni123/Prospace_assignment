from django.urls import path
from .views import *

urlpatterns = [
    path('classes/', classeslist.as_view(), name = 'class_list'),
    path('classes/<int:class_id>', classesdetail.as_view(), name = 'class_detail'),
    
    path('assignment/', assignmentlist.as_view(), name = 'assignment_list'),
    path('assignment/<int:class_id>', assignmentdetail.as_view(), name = 'assignment_detail'),
    
    path('questions/', questionlist.as_view(), name = 'question_list'),
    path('questions/<int:class_id>', questiondetail.as_view(), name = 'question_detail'),
    
]