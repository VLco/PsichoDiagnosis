from django.contrib import admin
from django.urls import path, re_path
from core import views


from .views import PatientRecordView
from .views import SinglePatientRecordView

from .views import DoctorView
from .views import LoginDoctorView

from .views import PatientListView
from .views import SinglePatientListView

from .views import TreatmentView
from .views import SingleTreatmentView

from .views import EpicrisisView
from .views import SingleEpicrisisView

from .views import DiagnosisView
from .views import SingleDiagnosisView

from .views import DiagnosView
from .views import SingleDiagnosView

from .views import FormView
from .views import SingleFormView

from .views import RuleView
from .views import SingleRuleView

from .views import SymptomView
from .views import SingleSymptomView

from .views import RuleSymptomView
from .views import SingleRuleSymptomView

from .views import SelectedSymptomsView
from .views import SingleSelectedSymptomsView

from .views import SelectedSymptomsDoctorView
from .views import SingleSelectedSymptomsDoctorView

from .views import AnamesisView
from .views import SingleAnamesisView

from .views import MamdaniDocView
from .views import MamdaniFormView


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
    path('patient_records/view/<id>/<login>', views.view_patient_records, name="view_patient_records"),

    path("<login>-personal_cabinet/", views.personal_cabinet, name="personal_cabinet"),

    path('patient_records/view/<int:id>/<login>', views.view_patient_records, name="view_patient_records"),
    path('patient_records/view/<int:id_p>/<login>/treatment-<int:id_tr>', views.view_treatment, name="view_treatment"),
    path('patient_records/view/<int:id_p>/<login>/treatment-<int:id_tr>/diagnosis-<int:id_d>', views.view_diagnosis, name="view_diagnosis"),

    path('symrule/delete/', views.delete_symrule, name="delete_symrule"),
    path('symrule/add/', views.add_symrule, name="add_symrule"),
    path('symrule/get/', views.get_symrule, name="get_symrule"),
    path('symrule/update/', views.update_symrule, name="update_symrule"),

    path('questionary/doc-<login>/', views.questionary, name="questionary"),
    path('questdoc/add/', views.add_questdoc, name="add_questdoc"),
    path('questdoc/delete/', views.delete_questdoc, name="delete_questdoc"),
    path('questdoc/deleteall/', views.deleteall_questdoc, name="deleteall_questdoc"),
    path('questdoc/get/', views.get_questdoc, name="get_questdoc"),
    path('questdoc/update/', views.update_questdoc, name="update_questdoc"),

    path('mamdani/', views.alg_mamdani_up, name="alg_mamdani_up"),



    path('api/patient-record/', PatientRecordView.as_view()),
    path('api/patient-record/<int:pk>', PatientRecordView.as_view()),
    path('api/single-patient-record/<int:pk>', SinglePatientRecordView.as_view()),

    path('api/doctor/<login>', DoctorView.as_view()),
    path('api/login-doctor/<login>/<password>', LoginDoctorView.as_view()),

    path('api/patient-list/', PatientListView.as_view()),
    path('api/patient-list/<int:pk>', PatientListView.as_view()),
    path('api/single-patient-list/<int:pk>', SinglePatientListView.as_view()),

    path('api/treatment/', TreatmentView.as_view()),
    path('api/treatment/<int:pk>', TreatmentView.as_view()),
    path('api/single-treatment/<int:pk>', SingleTreatmentView.as_view()),

    path('api/epicrisis/', EpicrisisView.as_view()),
    path('api/epicrisis/<int:pk>', EpicrisisView.as_view()),
    path('api/single-epicrisis/<int:pk>', SingleEpicrisisView.as_view()),

    path('api/diagnosis/', DiagnosisView.as_view()),
    path('api/diagnosis/<int:pk>', DiagnosisView.as_view()),
    path('api/single-diagnosis/<int:pk>', SingleDiagnosisView.as_view()),

    path('api/diagnos/', DiagnosView.as_view()),
    path('api/diagnos/<int:pk>', DiagnosView.as_view()),
    path('api/single-diagnos/<int:pk>', SingleDiagnosView.as_view()),

    path('api/form/', FormView.as_view()),
    path('api/form/<int:pk>', FormView.as_view()),
    path('api/single-form/<int:pk>', SingleFormView.as_view()),

    path('api/rule/', RuleView.as_view()),
    path('api/rule/<int:pk>', RuleView.as_view()),
    path('api/single-rule/<int:pk>', SingleRuleView.as_view()),

    path('api/symptom/', SymptomView.as_view()),
    path('api/symptom/<int:pk>', SymptomView.as_view()),
    path('api/single-symptom/<int:pk>', SingleSymptomView.as_view()),

    path('api/rule-symptom/', RuleSymptomView.as_view()),
    path('api/rule-symptom/<int:pk>', RuleSymptomView.as_view()),
    path('api/single-rule-symptom/<int:pk>', SingleRuleSymptomView.as_view()),
    
    path('api/selected-symptoms/', SelectedSymptomsView.as_view()),
    path('api/selected-symptoms/<int:pk>', SelectedSymptomsView.as_view()),
    path('api/single-selected-symptoms/<int:pk>', SingleSelectedSymptomsView.as_view()),
    
    path('api/selected-symptoms-doctor/', SelectedSymptomsDoctorView.as_view()),
    path('api/selected-symptoms-doctor/<int:pk>', SelectedSymptomsDoctorView.as_view()),
    path('api/single-selected-symptoms-doctor/<int:pk>', SingleSelectedSymptomsDoctorView.as_view()),

    path('api/anamesis/', AnamesisView.as_view()),
    path('api/anamesis/<int:pk>', AnamesisView.as_view()),
    path('api/single-anamesis/<int:pk>', SingleAnamesisView.as_view()),

    path('api/mamdani/doc-<login>', MamdaniDocView.as_view()),
    path('api/mamdani/form-<int:pk>', MamdaniFormView.as_view()),
]