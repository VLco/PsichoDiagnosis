from django.contrib import admin
from django.urls import path, re_path
from core import views


urlpatterns = [
    path('', views.base_core, name="base_core"),
    path('sign-in/', views.sign_in, name="sign_in"),
    path('register/', views.register, name="register"),
    path('main/', views.main, name="main"),
    path('doctor-<login>/db-patients/', views.db_patients, name="db_patients"),
    path('job-with-db-patients/', views.job_with_db_patients, name="job_with_db_patients"),
    path('doctor-<login>/postuplenie/', views.postuplenie, name="postuplenie"),
    path('doctor-<login>/db-questions/', views.db_questions, name="db_questions"),
    path('job-with-db-questions/', views.job_with_db_questions, name="job_with_db_questions"),
    path('doctor-<login>/db-diseases/', views.db_diseases, name="db_diseases"),
    path('job-with-db-diseases/', views.job_with_db_diseases, name="job_with_db_diseases"),
    path('doctor-<login>/postuplenie/db-anckets', views.db_anckets, name="db_anckets"),
    path('doctor-<login>/profile/', views.profile, name="profile"),
    path('job-with-db-anckets/', views.job_with_db_anckets, name="job_with_db_anckets"),
    path('doctor-<login>/chose-method-work-patient/', views.chose_method_work_patient, name="chose_method_work_patient"),
    path('doctor-<login>/job-with-db-epicriz/', views.job_with_db_epicriz, name="job_with_db_epicriz"),
    path('doctor-<login>/job-with-db-diagnozes/', views.job_with_db_diagnozes, name="job_with_db_diagnozes"),
    path('doctor-<login>/work-with-rules/', views.work_with_rules, name="work_with_rules"),
    path('doctor-<login>/db-symptoms/', views.db_symptoms, name="db_symptoms"),
    path('job-with-db-symptoms/', views.job_with_db_symptoms, name="job_with_db_symptoms"),
    
    path('directory/', views.directory, name="directory"),
    path('diagnos/delete/', views.delete_diagnos, name="delete_diagnos"),
    path('diagnos/add/', views.add_diagnos, name="add_diagnos"),
    path('symptom/delete/', views.delete_symptom, name="delete_symptom"),
    path('symptom/add/', views.add_symptom, name="add_symptom"),






]