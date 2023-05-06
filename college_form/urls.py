from django.urls import path
from .import views
from django.conf import settings

urlpatterns = [
    path('test/', views.test),

    # login urls
    path('', views.login_page, name="login_page"),
    path('new_Register/', views.new_Register, name="new_Register"),
    path('login_Request/', views.login_Request, name="login_Request"),
    path('signout/', views.signout, name="signout"),
    path('registerd/', views.already_fill_fomr, name="registerd"),
    
    # After login urls
    path('Personal-details/', views.page_1, name="personal_details"),
    path('submit_personal/', views.submit_personal_details, name="submit_personal_details"),

    path('address-details/', views.page_2, name="address_details"),
    path('submit_address/', views.submit_address, name="submit_address"),

    path('education-details/', views.page_3, name="education_details"),
    path('submit_education/', views.submit_education, name="submit_education_details"),

    path('photo-signature/', views.page_4, name="photo_signature"),
    path('submit_photo_signature/', views.submit_photo_signature, name="submit_photo_signature"),

    path('course-select/', views.page_5, name="coures_select"),
    path('select_course/', views.select_course, name="select_course"),
    path('confirm/', views.confirm, name="confirm"),

    path('preview/', views.preview_html, name="preview"),


] 
