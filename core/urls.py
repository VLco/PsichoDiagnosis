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
    
    path('<login>-directory/', views.directory, name="directory"),
    path('diagnos/delete/', views.delete_diagnos, name="delete_diagnos"),
    path('diagnos/add/', views.add_diagnos, name="add_diagnos"),
    path('diagnos/get/', views.get_diagnos, name="get_diagnos"),
    path('diagnos/update/', views.update_diagnos, name="update_diagnos"),

    path('symptom/delete/', views.delete_symptom, name="delete_symptom"),
    path('symptom/add/', views.add_symptom, name="add_symptom"),
    path('symptom/get/', views.get_symptom, name="get_symptom"),
    path('symptom/update/', views.update_symptom, name="update_symptom"),

    path('syndrom/getform/', views.syndrom_get_form, name="syndrom_get_form"),
    path('syndrom/delete/', views.delete_syndrom, name="delete_syndrom"),
    path('syndrom/add/', views.add_syndrom, name="add_syndrom"),
    path('syndrom/open-<id>/doc-<login>/', views.open_syndrom, name="open_syndrom"),
    path('syndrom/update/', views.update_syndrom, name="update_syndrom"),

    path('<login>-patient_records/',views.patient_records, name="patient_records"),
    path('patient_records/add/', views.add_patient_records, name="add_patient_records"),
    path('patient_records/delete/', views.delete_patient_records, name="delete_patient_records"),
    path('patient_records/update/', views.update_patient_records, name="update_patient_records"),
    path('patient_records/get/', views.get_patient_records, name="get_patient_records"),

    path("<login>-personal_cabinet/", views.personal_cabinet, name="personal_cabinet"),

    path('symrule/delete/', views.delete_symrule, name="delete_symrule"),
    path('symrule/add/', views.add_symrule, name="add_symrule"),
    path('symrule/get/', views.get_symrule, name="get_symrule"),
    path('symrule/update/', views.update_symrule, name="update_symrule"),

    path('questionary/doc-<login>/', views.questionary, name="questionary"),
    path('questdoc/add/', views.add_questdoc, name="add_questdoc"),
    path('questdoc/delete/', views.delete_questdoc, name="delete_questdoc"),
    path('questdoc/get/', views.get_questdoc, name="get_questdoc"),
    path('questdoc/update/', views.update_questdoc, name="update_questdoc"),

    path('mamdani/', views.alg_mamdani_up, name="alg_mamdani_up"),


]