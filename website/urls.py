from django.contrib import admin
from django.urls import path, include
from website import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'home'),
    path('ContactUs', views.contactus, name ='ContactUs'),
    path('login', views.login_user, name ='login'),
    path('dashboard/', views.dashboard, name ='dashboard'),
    path('logout', views.logout_user, name ='logout'),
    path('info/', views.enquiry_info, name ='enquiry_info'),
    path('delete/<int:id>/', views.delete_record, name ='delete_record'),
    path('edit/<int:id>/', views.edit_record, name ='edit_record'),
    path('update/<int:id>/', views.update_record, name ='update_record'),
    path('student_data', views.student_data.as_view(), name ='student_data'),
    # path('student_data', views.student_data, name ='student_data'),

]