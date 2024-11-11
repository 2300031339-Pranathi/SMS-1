from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.projecthomepage, name='projecthomepage'),
    path('printpagecall/',views.printpagecall, name='printpagecall'),
    path('printpagelogic/',views.printpagelogic, name='printpagelogic'),
    path('exceptionpagecall/',views.exceptionpagecall, name='exceptionpagecall'),
    path('exceptionpagelogic/',views.exceptionpagelogic, name='exceptionpagelogic'),
    path('randompagecall/', views.randompagecall, name='randompagecall'),
    path('randompagelogic/', views.randompagelogic, name='randompagelogic'),
    path('calculatorpagecall/', views.calculatorpagecall, name='calculatorpagecall'),
    path('calculatorlogic/', views.calculatorlogic, name='calculatorlogic'),
    path('datetimepagecall/', views.datetimepagecall, name='datetimepagecall'),
    path('datetimepagelogic/', views.datetimepagelogic, name='datetimepagelogic'),
    path('add_task/', views.add_task, name='add_task'),
    path('<int:pk>/delete/', views.delete_task, name='delete_task'),
    path('UserLoginPageCall/', views.UserLoginPageCall, name='UserLoginPageCall'),
    path('UserLoginLogic/', views.UserLoginLogic, name='UserLoginLogic'),
    path('RegisterPageCall/', views.RegisterPageCall, name='RegisterPageCall'),
    path('RegisterLogic/', views.RegisterLogic, name='RegisterLogic'),
    path('logout/', views.logout, name='logout'),
    path('add_student/', views.add_student, name='add_student'),
    path('student_list/', views.student_list, name='student_list'),
    path('upload_file/',views.upload_file,name='upload_file'),
    path('user_feedback/',views.user_feedback,name='user_feedback'),
    path('manage_contacts/', views.manage_contacts, name='manage_contacts'),
    path('contacts/delete/<int:pk>/', views.contact_delete, name='contact_delete'),
    #path('projectstudentpage/', views.projectstudentpage, name='projectstudentpage'),

]


