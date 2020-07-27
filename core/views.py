import pdb
import datetime
import math
import json
import random

from django.shortcuts import render
from django.views.generic import View
from django.urls import reverse
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist


from .models import *


from .forms import *


# Create your views here.

g_login = ''
# ok
def base_core(request):
    signin_form = SigninForm()
    template = "core/base_core.html"
    return render(request, template, {"form": signin_form})


# ok
def sign_in(request):
    if request.method == "POST":
        user = Doctor()
        if user.Activated == True:
            fields = {
                'login': request.POST.get("login"),
                'password': request.POST.get("password"),
            }

            if Doctor.objects.all().filter(login=fields['login']):
                user.login = fields['login']
                user.password = fields['password']
                template = 'core/main.html'
                return render(request, template, {"login": user.login})
            else:
                signin_form = SigninForm()
                template = "core/base_core.html"
                return render(request, template, {"form": signin_form, "message": "Данные введены не корректно"})
            
        else:
            signin_form = SigninForm()
            template = "core/sign_in.html"
            return render(request, template, {"form": signin_form, "message": "Аккаунт не активирован"})
    else:
        signin_form = SigninForm()
        template = "core/base_core.html"
        return render(request, template, {"form": signin_form})
        




# ok
def register(request):
    if request.method == "POST":
        user = Doctor()

        fields = {
            'login': request.POST.get("login"),
            'password': request.POST.get("password"),
            'rePassword': request.POST.get("rePassword")
        }

        if Doctor.objects.all().filter(login=fields['login']):
            reg_form = RegisterForm()
            template = "core/register.html"
            return render(request, template, {"form": reg_form, "message":"Пользователь с таким логином уже зарегистрирован"})

        elif fields['password'] != fields['rePassword']:
            reg_form = RegisterForm()
            template = "core/register.html"
            return render(request, template, {"form": reg_form, "message": "Введенные пароли не совпадают. Попробуйте еще раз"})

        else:
            user.login = fields['login']
            user.password = fields['password']
            user.Activated = False
            user.save()
            return HttpResponseRedirect('/sign-in/')
    else:
        reg_form = RegisterForm()
        template = "core/register.html"
        return render(request, template, {"form": reg_form})



# ok
def main(request):
    
    if request.method == "POST":

        fields = {
            'login': request.POST.get("login"),
            'password': request.POST.get("password"),
        }

        if Doctor.objects.all().filter(login=fields['login'], password=fields['password'],Activated = False):
            signin_form = SigninForm()
            template = "core/base_core.html"
            return render(request, template, {"form": signin_form, "message": "Account not activated"})
        if Doctor.objects.all().filter(login=fields['login'], password=fields['password'], Activated = True):
            template = 'core/main.html'
            return HttpResponseRedirect(reverse("patient_records", args=[fields['login']]))
        else:
            signin_form = SigninForm()
            template = "core/base_core.html"
            return render(request, template, {"form": signin_form, "message": "Login or password is not valid"})
        
    else:
        return redirect('/')


# ok
def db_patients(request, login):

    global g_login
    g_login = login

    db_patients_form = DbPatientsForm()

    patients = PatientRecord.objects.all()

    context = {
        'login': login,
        'form': db_patients_form,
        'patients': patients,
    }
    template = "core/db_patients.html"
    return render(request, template, context)



# ok
def job_with_db_patients(request):
    if request.method == "POST":

        fields = {
            'number_card': request.POST.get("number_card"),
            'FIO': request.POST.get("FIO"),
            'date_birth': request.POST.get("date_birth"),
            'sex': request.POST.get("sex"),
            'address': request.POST.get("address"),
            'phone': request.POST.get("phone"),
        }



        if '_add' in request.POST:
            try:
                patient = PatientRecord()
                patient.NumberRecord = fields['number_card']
                patient.FIO = fields['FIO']
                patient.Birthday = fields['date_birth']
                patient.Sex = fields['sex']
                patient.Adress = fields['address']
                patient.Phone = fields['phone']
                patient.save()
            except ObjectDoesNotExist:
                return redirect('/doctor-' + g_login + '/db-patients/')


        if '_delete' in request.POST:
            try:
                if PatientRecord.objects.all().filter(NumberRecord=fields['number_card']):
                    PatientRecord.objects.all().filter(NumberRecord=fields['number_card']).delete()
                else:
                    return redirect('/doctor-' + g_login + '/db-patients/')
            except ObjectDoesNotExist:
                    return redirect('/doctor-' + g_login + '/db-patients/')
        return redirect('/doctor-' + g_login + '/db-patients/')


# ok
def delete_patient(request):

    if request.method == "POST":

        fields = {
            'number_card': request.POST.get("number_card"),
            'FIO': request.POST.get("FIO"),
            'date_birth': request.POST.get("date_birth"),
            'sex': request.POST.get("sex"),
            'nationality': request.POST.get("nationality"),
            'education': request.POST.get("education"),
            'address': request.POST.get("address"),
            'phone': request.POST.get("phone"),
            'job': request.POST.get("job"),
            'position': request.POST.get("position"),
        }

        try:
            patient = PatientRecord()
            patient.number_card = fields['number_card']
            patient.FIO = fields['FIO']
            patient.date_birth = fields['date_birth']
            patient.sex = fields['sex']
            patient.address = fields['address']
            patient.phone = fields['phone']
            patient.save()
        except ObjectDoesNotExist:
            return redirect('/doctor-' + g_login + '/db-patients/')
    return redirect('/doctor-' + g_login + '/db-patients/')

# ok
def change_patient(request):

    if request.method == "POST":

        fields = {
            'number_card': request.POST.get("number_card"),
            'FIO': request.POST.get("FIO"),
            'date_birth': request.POST.get("date_birth"),
            'sex': request.POST.get("sex"),
            'nationality': request.POST.get("nationality"),
            'education': request.POST.get("education"),
            'address': request.POST.get("address"),
            'phone': request.POST.get("phone"),
            'job': request.POST.get("job"),
            'position': request.POST.get("position"),
        }
        try:
            patient = Patient()
            patient.number_card = fields['number_card']
            patient.FIO = fields['FIO']
            patient.date_birth = fields['date_birth']
            patient.sex = fields['sex']
            patient.nationality = fields['nationality']
            patient.education = fields['education']
            patient.address = fields['address']
            patient.phone = fields['phone']
            patient.job = fields['job']
            patient.position = fields['position']
            patient.save()
        except ObjectDoesNotExist:
            return redirect('/doctor-' + g_login + '/db-patients/')
    return redirect('/doctor-' + g_login + '/db-patients/')




# ok
def db_questions(request, login):

    global g_login
    g_login = login
    
    db_questions_form = DbQuestionsForm()
    

    questions = Symptom.objects.all()

    context = {
        'login': login,
        'form': db_questions_form,
        'questions': questions,
    }
    template = "core/db_questions.html"
    return render(request, template, context)

#ok
def job_with_db_questions(request):
   
        if request.method == "POST":

            fields = {
                'question_id': request.POST.get("question_id"),
                'question': request.POST.get("question"),
            }
        
        if '_add' in request.POST:

            question = Symptom()

            if fields['question_id'] !='':
                question.id = fields['question_id']
            question.Name = fields['question']
            question.Description = ''

            question.save()

        if '_delete' in request.POST:
            if Symptom.objects.all().filter(id=fields['question_id']):
                Symptom.objects.all().filter(id=fields['question_id']).delete()
        else:
            return redirect('/doctor-' + g_login + '/db-questions/')
        return redirect('/doctor-' + g_login + '/db-questions/')

# ok
def db_diseases(request, login):

    global g_login
    g_login = login
    
    db_diseases_form = DbDiseasesForm()
    

    diseases = Diagnos.objects.all()

    context = {
        'login': login,
        'form': db_diseases_form,
        'diseases': diseases,
    }
    template = "core/db_diseases.html"
    return render(request, template, context)

# ok
def job_with_db_diseases(request):
   
    if request.method == "POST":

        fields = {
            'diseases_id': request.POST.get("diseases_id"),
            'name': request.POST.get("name"),
            'note': request.POST.get("note"),

        }
        
        if '_add' in request.POST:

            disease = Diagnos()

            if fields['diseases_id'] !='':
                disease.id = fields['diseases_id']
            disease.Name = fields['name']
            disease.Description = fields['note']


            disease.save()


        #pdb.set_trace()
        if '_delete' in request.POST:
            if Diagnos.objects.all().filter(id=fields['diseases_id']):
                Diagnos.objects.all().filter(id=fields['diseases_id']).delete()
        else:
            return redirect('/doctor-' + g_login + '/db-diseases/')

        return redirect('/doctor-' + g_login + '/db-diseases/')

# Страница "данные при поступлении"
def postuplenie(request, login):
    global g_login
    g_login = login
    
    postuplenie_form = PostuplenieForm()

    context = {
        'login': login,
        'form': postuplenie_form,
    }
    template = "core/postuplenie.html"
    return render(request, template, context)

# TODO: Удалить в следующиемм релизе, нигде не используется.    
def db_anckets(request, login, number_card):
    pdb.set_trace()

    if request.method == "POST":

        global g_login
        g_login = login

        db_anckets_form = DBAncketsForm()

        ankets = Ancket.objects.all() #Надо чтобы макеты выбирал по номеру карты а не все анкеты пациентов.

        context = {
            'login': login,
            'number_card': number_card,
            'form': db_anckets_form,
            'ankets': ankets,
        }
        template = "core/db_anckets.html"
        return render(request, template, context)


def chose_method_work_patient(request, login):
    
    if request.method == "POST":
        if 'opros_btn' in request.POST:
            return job_with_db_anckets(request)
        if 'epicriz_btn' in request.POST:   
            return job_with_db_epicriz(request, login)
        if 'diagnoz_btn' in request.POST:   
            return job_with_db_diagnozes(request, login)

def job_with_db_diagnozes(request, login):
        # заход на сайт
        # pdb.set_trace()
        # pdb.set_trace()

        db_diagnos_form = DbDiagnosesForm()
        diagnoses = Diagnos.objects.all()
        # pdb.set_trace()
        patient = Patient.objects.get(number_card = request.POST.get("number_card"))
        user = User.objects.get(login = login)
        if 'diagnoz_btn' in request.POST:
            if Patient.objects.all().filter(number_card=request.POST.get("number_card")):
                db_diagnos_form.fields["number_card"].initial = request.POST.get("number_card")
                epicrizis = Epicriz.objects.filter(patient__number_card=request.POST.get("number_card")).order_by('-date_gospit')
                diagnoses = Diagnos.objects.select_related().all()
                # diagnoses = Diagnos.objects.
            else:
                db_diagnos_form.fields["number_card"].initial = 'ERROR: there are not such card'
            # answers = Answer.objects.all().order_by('-date')
            context = {
                'login': login,
                'form': db_diagnos_form,
                'diagnoses': diagnoses,
                'patient': patient,
                'user': user,
            }
            template = "core/db_diagnoses.html"
            return render(request, template, context)
        # добавление нового диагноза
        elif 'add_btn' in request.POST:
            
            db_diagnos_form.fields["number_card"].initial = request.POST.get("number_card")
            # vovasss
            diagnos = Diagnos()
            # pdb.set_trace()
            diagnos.user = user
            diagnos.epicriz = Epicriz.objects.get(lechenie = request.POST.get("epicriz"))
            diagnos.disease = Disease.objects.get(name = request.POST.get("disease"))
            diagnos.note = request.POST.get("note")

            diagnos.save()

            diagnoses = Diagnos.objects.select_related().all()
            context = {
                'login': login,
                'form': db_diagnos_form,
                'diagnoses': diagnoses,
                'patient': patient,
                'user': user,
            }
            template = "core/db_diagnoses.html"
            return render(request, template, context)
        # удаление 
        elif 'delete_btn' in request.POST:
            diagnos = Diagnos()
            diagnos = Diagnos.objects.get(id = request.POST.get("number_diag"))
            diagnos.delete()
            
            db_diagnos_form.fields["number_card"].initial = request.POST.get("number_card")
            diagnoses = Diagnos.objects.select_related().all()
            context = {
                'login': login,
                'form': db_diagnos_form,
                'diagnoses': diagnoses,
                'patient': patient,
                'user': user,
            }
            template = "core/db_diagnoses.html"
            return render(request, template, context)
        elif 'change_btn' in request.POST:
            db_diagnos_form.fields["number_card"].initial = request.POST.get("number_card")

            diagnos = Diagnos.objects.get(id = request.POST.get("number_diag"))
            diagnos.user = user
            diagnos.epicriz = Epicriz.objects.get(lechenie = request.POST.get("epicriz"))
            diagnos.disease = Disease.objects.get(name = request.POST.get("disease"))
            diagnos.note = request.POST.get("note")

            diagnos.save()

            diagnoses = Diagnos.objects.select_related().all()
            context = {
                'login': login,
                'form': db_diagnos_form,
                'diagnoses': diagnoses,
                'patient': patient,
                'user': user,
            }
            template = "core/db_diagnoses.html"
            return render(request, template, context)
        # TODO: получение данных диагноза в формы
        # elif 'get_data_diag' in request.POST:
        #     db_diagnos_form.fields["number_card"].initial = request.POST.get("number_card")

        #     epicriz = Epicriz.objects.get(id = request.POST.get("number_epic"))
        #     db_diagnos_form.fields["number_epic"].initial = request.POST.get("number_epic")
        #     db_diagnos_form.fields["lechenie"].initial = epicriz.lechenie
        #     db_diagnos_form.fields["date_gospit"].initial = epicriz.date_gospit
        #     db_diagnos_form.fields["date_vipisky"].initial = epicriz.date_vipisky

        #     diagnoses = Diagnos.objects.select_related().all()
        #     context = {
        #         'login': login,
        #         'form': db_diagnos_form,
        #         'diagnoses': diagnoses,
        #         'patient': patient,
        #         'user': user,
        #     }
        #     template = "core/db_diagnoses.html"
        #     return render(request, template, context)

def job_with_db_epicriz(request, login):
        # pdb.set_trace()
        # заход на сайт
        db_epicriz_form = DBEpicrizForm()
        epicrizis = Epicriz.objects.all()
        # pdb.set_trace()
        patient = Patient.objects.get(number_card = request.POST.get("number_card"))
        user = User.objects.get(login = login)
        if 'epicriz_btn' in request.POST:
            if Patient.objects.all().filter(number_card=request.POST.get("number_card")):
                db_epicriz_form.fields["number_card"].initial = request.POST.get("number_card")
                epicrizis = Epicriz.objects.filter(patient__number_card=request.POST.get("number_card")).order_by('-date_gospit')
            else:
                db_epicriz_form.fields["number_card"].initial = 'ERROR: there are not such card'
            # answers = Answer.objects.all().order_by('-date')
            context = {
                'login': login,
                'form': db_epicriz_form,
                'epicrizis': epicrizis,
                'patient': patient,
                'user': user,
            }
            template = "core/db_epicriz.html"
            return render(request, template, context)
        # добавление нового эпикриза
        elif 'add_btn' in request.POST:
            db_epicriz_form.fields["number_card"].initial = request.POST.get("number_card")
            is_invalid = False
            if request.POST.get("invalid"):
                is_invalid = True
            else:
                is_invalid = False
            # fields_add_epic = {
            #     'invalid': is_invalid,
            #     'lechenie': request.POST.get("lechenie"),
            #     'date_gospit': request.POST.get("date_gospit"),
            #     'lechenie': request.POST.get("date_vipisky"),
            # }
            epicriz = Epicriz()
            # pdb.set_trace()
            epicriz.patient = patient
            epicriz.user = user
            epicriz.invalid = is_invalid
            epicriz.lechenie = request.POST.get("lechenie")
            epicriz.date_gospit = request.POST.get("date_gospit")
            epicriz.date_vipisky = request.POST.get("date_vipisky")

            epicriz.save()

            epicrizis = Epicriz.objects.filter(patient__number_card=request.POST.get("number_card")).order_by('-date_gospit')
            context = {
                'login': login,
                'form': db_epicriz_form,
                'epicrizis': epicrizis,
                'patient': patient,
                'user': user,
            }
            template = "core/db_epicriz.html"
            return render(request, template, context)
        # удаление 
        elif 'delete_btn' in request.POST:
            epicriz = Epicriz()
            epicriz = Epicriz.objects.get(id = request.POST.get("number_epic"))
            epicriz.delete()
            
            db_epicriz_form.fields["number_card"].initial = request.POST.get("number_card")
            epicrizis = Epicriz.objects.filter(patient__number_card=request.POST.get("number_card")).order_by('-date_gospit')
            context = {
                'login': login,
                'form': db_epicriz_form,
                'epicrizis': epicrizis,
                'patient': patient,
                'user': user,
            }
            template = "core/db_epicriz.html"
            return render(request, template, context)
        elif 'change_btn' in request.POST:
            db_epicriz_form.fields["number_card"].initial = request.POST.get("number_card")
            is_invalid = False
            if request.POST.get("invalid"):
                is_invalid = True
            else:
                is_invalid = False
            # fields_add_epic = {
            #     'invalid': is_invalid,
            #     'lechenie': request.POST.get("lechenie"),
            #     'date_gospit': request.POST.get("date_gospit"),
            #     'lechenie': request.POST.get("date_vipisky"),
            # }
            epicriz = Epicriz.objects.get(id = request.POST.get("number_epic"))
            epicriz.patient = patient
            epicriz.user = user
            epicriz.invalid = is_invalid
            epicriz.lechenie = request.POST.get("lechenie")
            epicriz.date_gospit = request.POST.get("date_gospit")
            epicriz.date_vipisky = request.POST.get("date_vipisky")

            epicriz.save()

            epicrizis = Epicriz.objects.filter(patient__number_card=request.POST.get("number_card")).order_by('-date_gospit')
            context = {
                'login': login,
                'form': db_epicriz_form,
                'epicrizis': epicrizis,
                'patient': patient,
                'user': user,
            }
            template = "core/db_epicriz.html"
            return render(request, template, context)
        elif 'get_data_epic' in request.POST:
            db_epicriz_form.fields["number_card"].initial = request.POST.get("number_card")
            is_invalid = False
            if request.POST.get("invalid"):
                is_invalid = True
            else:
                is_invalid = False
            epicriz = Epicriz.objects.get(id = request.POST.get("number_epic"))
            db_epicriz_form.fields["number_epic"].initial = request.POST.get("number_epic")
            db_epicriz_form.fields["lechenie"].initial = epicriz.lechenie
            db_epicriz_form.fields["date_gospit"].initial = epicriz.date_gospit
            db_epicriz_form.fields["date_vipisky"].initial = epicriz.date_vipisky

            epicrizis = Epicriz.objects.filter(patient__number_card=request.POST.get("number_card")).order_by('-date_gospit')
            context = {
                'login': login,
                'form': db_epicriz_form,
                'epicrizis': epicrizis,
                'patient': patient,
                'user': user,
            }
            template = "core/db_epicriz.html"
            return render(request, template, context)
        

def job_with_db_anckets(request):
    # pdb.set_trace()
    if request.method == "POST":
        # заход на сайт
        db_anckets_form = DBAncketsForm()
        ankets = Ancket.objects.all()
        
        if 'opros_btn' in request.POST:
            if Patient.objects.all().filter(number_card=request.POST.get("number_card")):
                db_anckets_form.fields["number_card"].initial = request.POST.get("number_card")
                ankets = Ancket.objects.filter(patient__number_card=request.POST.get("number_card")).order_by('-date')
                # ankets.reverse()

            else:
                db_anckets_form.fields["number_card"].initial = 'ERROR: there are not such card'

            answers = Answer.objects.all().order_by('-date')
            context = {
                'login': request.POST.get("login"),
                'form': db_anckets_form,
                'ankets': ankets,
                'answers': answers,
            }
            template = "core/db_anckets.html"
            return render(request, template, context)
        # добавление новой анкеты
        elif 'add_opros' in request.POST:
            fields_add_opros = {
                'number_ancket': request.POST.get("number_ancket"),
                'number_card': request.POST.get("number_card"),
            }
            ancket = Ancket()
            
            some_patient = Patient.objects.get(number_card = fields_add_opros['number_card'])
            ancket.patient = some_patient
            ancket.date = datetime.datetime.now()
            ancket.save()

            db_anckets_form.fields["number_card"].initial = request.POST.get("number_card")

            ankets = Ancket.objects.filter(patient__number_card=request.POST.get("number_card")).order_by('-date')
            # ankets.reverse()
            answers = Answer.objects.all().order_by('-date')
            context = {
                'login': request.POST.get("login"),
                'form': db_anckets_form,
                'ankets': ankets,
                'answers': answers,
            }
            template = "core/db_anckets.html"
            return render(request, template, context)
        # добавление ответа к выбранной анкете
        elif 'add_answer' in request.POST:
            fields_add_answer = {
                'number_ancket': request.POST.get("number_ancket"),
                'number_card': request.POST.get("number_card"),
                'question': request.POST.get("question"),
                'answer': request.POST.get("answer"),
                'conviction': request.POST.get("conviction"),
                
            }
            # pdb.set_trace()
            somevalue = fields_add_answer['number_ancket']
            ancket = Ancket.objects.get(id = fields_add_answer['number_ancket'])
            
            answer = Answer()
            answer.ancket = ancket
            answer.date = datetime.datetime.now()
            answer.note = fields_add_answer['answer']
            answer.question = Question.objects.get(question = fields_add_answer['question'])#fields_add_answer['question']
            answer.conviction = fields_add_answer['conviction']
            answer.save()

            db_anckets_form.fields["number_card"].initial = request.POST.get("number_card")
            db_anckets_form.fields["number_ancket"].initial = request.POST.get("number_ancket")


            ankets = Ancket.objects.filter(patient__number_card=request.POST.get("number_card")).order_by('-date')

            answers = Answer.objects.all().order_by('-date')
            context = {
                'login': request.POST.get("login"),
                'form': db_anckets_form,
                'ankets': ankets,
                'answers': answers,
            }
            template = "core/db_anckets.html"
            return render(request, template, context)
            
def profile(request,login):
    global g_login
    g_login = login

    profile_form = ProfileForm()
    # pdb.set_trace()
    user = User.objects.get(login = login)
    fields_save = {
            'login': "",
            'FIO': "",
            'postion': "",
            'department': "",
            'password': "",
        }

    if request.method == "POST":
            if 'save' in request.POST:
                fields_save = {
                    'login': request.POST.get("login"),
                    'FIO': request.POST.get("FIO"),
                    'position': request.POST.get("position"),
                    'department': request.POST.get("department"),
                    'password': request.POST.get("password"),
                }
                user = Doctor.objects.get(login = login)
                user.FIO = fields_save['FIO']
                if Doctor.objects.all().filter(login = fields_save['login']):
                    donothing = 0
                else:
                    user.login = fields_save['login']
                user.Position = fields_save['position']
                user.Department = fields_save['department']
                user.password = fields_save['password']
                
                user.save()

    # pdb.set_trace()
    template = "core/profile.html"

    profile_form = ProfileForm()
    profile_form.fields['FIO'].initial = user.FIO
    profile_form.fields['login'].initial = user.login
    profile_form.fields['position'].initial = user.Position
    profile_form.fields['department'].initial = user.Department
    profile_form.fields['password'].initial = user.password

    context = {
        'login': login,
        'form': profile_form,
        }
    return render(request, template, context)


def work_with_rules(request, login):
    global g_login
    g_login = login

    work_with_rules_form = WorkWithRulesForm()

    fields_save = {
            'symptom1': "",
            'symptom2': "",
            'symptom3': "",
            'symptom4': "",
            'conviction1': "",
            'conviction2': "",
            'conviction3': "",
            'conviction4': "",
        }

    if request.method == "POST":
            if 'diagnose_this' in request.POST:
                pdb.set_trace()
                _r1 = ((int(request.POST.get("conviction1")))*10)*(25/10)
                _r2 = ((int(request.POST.get("conviction2")))*10)*(25/10)
                _r3 = ((int(request.POST.get("conviction3")))*10)*(25/10)
                _r4 = ((int(request.POST.get("conviction4")))*10)*(25/10)

                

                someQuestion = request.POST.get("symptom1")
                _v1 = Question.objects.get(question = someQuestion)
                someQuestion = request.POST.get("symptom2")
                _v2 = Question.objects.get(question = someQuestion)
                someQuestion = request.POST.get("symptom3")
                _v3 = Question.objects.get(question = someQuestion)
                someQuestion = request.POST.get("symptom4")
                _v4 = Question.objects.get(question = someQuestion)

                mju = (_r1 + _r2 + _r3 + _r4) / 4

                command = PravilaRule.objects.select_related().all()

                min = 100
                _id = 0
                diagnos = ""
                ver = 0

                try:
                    # pdb.set_trace()
                    for pravila in command:
                        ### это я добавил свое (может я что то неправильно понял? Но должно работать)
                        id_q = pravila.question.id
                        if id_q == _v1.id or  id_q == _v2.id or  id_q == _v3.id or  id_q == _v4.id:  
                        ###
                            uver = pravila.rule.conviction
                            rast = math.sqrt(uver * uver - mju * mju)
                            
                            if rast<min:
                                min = rast
                                _id = pravila.id
                                diagnos = pravila.rule.disease.name
                                ver = uver
                except:
                    nothing = True
                
                # pdb.set_trace()
                work_with_rules_form.fields['diagnose_result'].initial = diagnos
                work_with_rules_form.fields['conviction_result'].initial = ver

                work_with_rules_form.fields['conviction1'].initial = _r1
                work_with_rules_form.fields['conviction2'].initial = _r2
                work_with_rules_form.fields['conviction3'].initial = _r3
                work_with_rules_form.fields['conviction4'].initial = _r4
                work_with_rules_form.fields['symptom1'].initial = _v1
                work_with_rules_form.fields['symptom2'].initial = _v2
                work_with_rules_form.fields['symptom3'].initial = _v3
                work_with_rules_form.fields['symptom4'].initial = _v4

    context = {
        'login': login,
        'form': work_with_rules_form,
        }
    template = "core/work_with_rules.html"
    return render(request, template, context)

def db_symptoms(request, login):

    global g_login
    g_login = login
    
    db_symptoms_form = DBSymptomsForm()
    

    pravila = PravilaRule.objects.all()

    context = {
        'login': login,
        'form': db_symptoms_form,
        'pravila': pravila,
    }
    template = "core/db_symptoms.html"
    return render(request, template, context)

def job_with_db_symptoms(request):
   
    if request.method == "POST":

        fields = {
            'login': request.POST.get("login"),
            'pravila_id': request.POST.get("pravila_id"),
            'diagnos': request.POST.get("diagnos"),
            'question': request.POST.get("question"),
            'conviction': request.POST.get("conviction"),

        }
        
        if '_add' in request.POST:

            pravila = PravilaRule()
            rule = Rule()

            if fields['pravila_id'] !='':
                question.id = fields['pravila_id']
            someQuestion = fields['question']
            pravila.question = Question.objects.get(question = someQuestion)
            someDisease = fields['diagnos']
            rule.disease = Disease.objects.get(name = someDisease)
            rule.conviction = fields['conviction']
            rule.save()
            pravila.rule = rule

            pravila.save()


        #pdb.set_trace()
        if '_delete' in request.POST:
            if PravilaRule.objects.all().filter(id=fields['pravila_id']):
                PravilaRule.objects.all().filter(id=fields['pravila_id']).delete()
        else:
            return redirect('/doctor-' + g_login + '/db-symptoms/')

         


        #if '_change' in request.POST:


        return redirect('/doctor-' + g_login + '/db-symptoms/')



######
#Каталог с диагнозами, симптомами и синтромами
def directory(request, login):

    rules = Rule.objects.all()
    RuleSymptomes = RuleSymptom.objects.all()
    symptomes = Symptom.objects.all()
    diagnoses = Diagnos.objects.all()

    formDiagnos = DiagnosesForm()
    formSymptom = SymptomesForm()
    formSyndrom = SyndromesForm()

    ruleAll = []
    for rule in rules:
        diagnos = rule.Diagnos.Name
        frequency = rule.Frequency.Name
        num = RuleSymptomes.filter(Rule=rule.id).count()
        ruleAll.append({'id': rule.id ,'diagnos':diagnos, 'frequency':frequency, 'num':num})


    context = {
        'login':login,
        'formDiagnos': formDiagnos,
        'formSymptom': formSymptom,
        'formSyndrom': formSyndrom,
        'ruleAll': ruleAll,
        'diagnoses': diagnoses,
        'symptomes': symptomes,
        'login':login
    }
    template = "core/directory.html"
    return render(request, template, context)

##Диагнозы
def delete_diagnos(request):
    error=1
    if request.method == "POST":
        id = request.POST.get("id")
        if Diagnos.objects.all().filter(id=id):
            Diagnos.objects.all().filter(id=id).delete()
            error=0
    return HttpResponse(error)


def add_diagnos(request):
    error=-1

    if request.method == "POST":
        name = request.POST.get("nameDiag")
        if not (Diagnos.objects.all().filter(Name=name) or name==''):
            diagnos = Diagnos()
            diagnos.Name=name
            diagnos.Description=request.POST.get("descriptionDiag")
            diagnos.save()
            error=diagnos.id
        else:
            error=-2
    return HttpResponse(error)

def get_diagnos(request):
    error=-1
    if request.method == "POST":
        id = request.POST.get("id")
        if Diagnos.objects.all().filter(id=id):
            diagnos = Diagnos.objects.get(id=id)
            return HttpResponse(json.dumps({'id': diagnos.id, 'name':diagnos.Name, 'description':diagnos.Description}), content_type="application/json")
    return HttpResponse(json.dumps({'id': error}), content_type="application/json")

def update_diagnos(request):
    error=-1
    if request.method == "POST":
        id = request.POST.get("idDiag")
        name = request.POST.get("nameDiag")
        if  name!='':
            diagnos = Diagnos.objects.get(id=id)
            diagnos.Name=name
            diagnos.Description=request.POST.get("descriptionDiag")
            diagnos.save()
            error=0
        else:
            error=-2
    return HttpResponse(error)


##Симптомы
def delete_symptom(request):
    error=1
    if request.method == "POST":
        id = request.POST.get("id")
        if Symptom.objects.all().filter(id=id):
            Symptom.objects.all().filter(id=id).delete()
            error=0
    return HttpResponse(error)

##Симптомы
def add_symptom(request):
    error=-1

    if request.method == "POST":
        name = request.POST.get("nameSym")
        if not (Symptom.objects.all().filter(Name=name) or name==''):
            symptom = Symptom()
            symptom.Name=name
            symptom.Description=request.POST.get("descriptionSym")
            newd = symptom.save()
            error=symptom.id
        else:
            error=-2
    return HttpResponse(error)

def get_symptom(request):
    error=-1
    if request.method == "POST":
        id = request.POST.get("id")
        if Symptom.objects.all().filter(id=id):
            symptom = Symptom.objects.get(id=id)
            return HttpResponse(json.dumps({'id': symptom.id, 'name':symptom.Name, 'description':symptom.Description}), content_type="application/json")
    return HttpResponse(json.dumps({'id': error}), content_type="application/json")
    
def update_symptom(request):
    error=-1
    if request.method == "POST":
        id = request.POST.get("idSym")
        name = request.POST.get("nameSym")
        if  name!='':
            symptom = Symptom.objects.get(id=id)
            symptom.Name=name
            symptom.Description=request.POST.get("descriptionSym")
            symptom.save()
            error=0
        else:
            error=-2
    return HttpResponse(error)


## Синдромы
def syndrom_get_form(request):
    formSyndrom = SyndromesForm()
    return HttpResponse(formSyndrom)

def delete_syndrom(request):
    error=1
    if request.method == "POST":
        id = request.POST.get("id")
        if Rule.objects.all().filter(id=id):
            Rule.objects.all().filter(id=id).delete()
            error=0
    return HttpResponse(error)


def patient_records(request,login):
    records = PatientRecord.objects.all()
    global g_login
    g_login = login

    formRecords = PatientsForm()
    context = {
        'login':login,
        'formRecords':formRecords,
        'records':records
    }
    template = "core/patient_record.html"
    return render(request, template, context)


def delete_patient_records(request):
    error=1
    if request.method == "POST":
        id = request.POST.get("id")
        if PatientRecord.objects.all().filter(id=id):
            PatientRecord.objects.all().filter(id=id).delete()
            error=0
    return HttpResponse(error)


def add_patient_records(request):
    error=-1

    if request.method == "POST":
        number_card = request.POST.get("number_card")
        FIO = request.POST.get("FIO")
        date_birth = request.POST.get("date_birth")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        sex = request.POST.get("sex")
        if not (PatientRecord.objects.all().filter(NumberRecord=number_card) or number_card==''):
            patient = PatientRecord()
            patient.NumberRecord = number_card
            patient.FIO = FIO
            patient.Birthday = date_birth
            patient.Adress = address
            patient.Phone = phone
            patient.Sex = sex
            patient.save()
            error=patient.id
        else:
            error=-2
    return HttpResponse(error)

def update_patient_records(request):
    error=-1
    if request.method == "POST":
        id = request.POST.get("idPatient")
        number_card = request.POST.get("number_card")
        if  number_card!='':
            patient = PatientRecord.objects.get(id=id)
            patient.NumberRecord = number_card
            patient.FIO = request.POST.get("FIO")
            patient.Birthday = request.POST.get("date_birth")
            patient.Sex = request.POST.get("sex")
            patient.Adress = request.POST.get("address")
            patient.Phone = request.POST.get("phone")
            patient.save()
            error=0
        else:
            error=-2
    return HttpResponse(error)


def get_patient_records(request):
    error=-1
    if request.method == "POST":
        id = request.POST.get("id")
        if PatientRecord.objects.all().filter(id=id):
            patient = PatientRecord.objects.get(id=id)
            return HttpResponse(json.dumps({'id': patient.id, 'Card_number':patient.NumberRecord, 'FIO':patient.FIO, 'Birthday':patient.Birthday.strftime("%Y-%m-%d"), 'Sex':patient.Sex, 'Adress':patient.Adress,'Phone':patient.Phone}), content_type="application/json")
    return HttpResponse(json.dumps({'id': error}), content_type="application/json")



def view_patient_records(request, id, login):
    user = Doctor.objects.get(login=login)
    patient = PatientRecord.objects.get(id=id)
    treatment = Treatment.objects.filter(Record=patient)
    if request.method != "POST":
        form = formTreatment()
    if request.method == "POST":
        formAdd = formTreatment(request.POST)
        if formAdd.is_valid():
            tr = Treatment()
            tr.Record = patient
            tr.Doctor = Doctor.objects.get(login=request.POST.get('doctor'))
            tr.Name = request.POST.get('name')
            tr.Note = request.POST.get('note')
            if tr.Date is request.POST.get('date', False):
                tr.Date = request.POST.get('date')
            tr.save()
            return HttpResponseRedirect(reverse("view_patient_records", args=[patient.id, user.login]))
    context = {
        'login': login,
        'patient': patient,
        'user': user,
        'formTreatment': form,
        "listTre": treatment
    }
    template = "core/view_patient.html"
    return render(request, template, context)
    pass


def view_treatment(request, id_p, login, id_tr):
    user = Doctor.objects.get(login=login)
    patient = PatientRecord.objects.get(id=id_p)
    treatment = Treatment.objects.get(id=id_tr)
    diag = Diagnosis.objects.filter(Treatment=treatment)
    if request.method != "POST":
        form = formDiagnosis()
    else:
        formAdd = formDiagnosis(request.POST)
        if formAdd.is_valid():
            di = Diagnosis()
            di.Treatment = treatment
            di.Doctor = Doctor.objects.get(login=request.POST.get('doctor'))
            di.Name = request.POST.get('name')
            di.Note = request.POST.get('note')
            if di.StartDiagnosis is request.POST.get('date', False):
                di.StartDiagnosis = request.POST.get('date')
            di.save()
            return HttpResponseRedirect(reverse("view_treatment", args=[patient.id, user.login, treatment.id]))
    context = {
        'login': login,
        'patient': patient,
        'user': user,
        'listD': diag,
        "treatment": treatment,
        "formDiagnosis": form
    }
    template = "core/view_treatment.html"
    return render(request, template, context)
    pass


def view_diagnosis(request, id_p, login, id_tr, id_d):
    user = Doctor.objects.get(login=login)
    patient = PatientRecord.objects.get(id=id_p)
    treatment = Treatment.objects.get(id=id_tr)
    diag = Diagnosis.objects.get(id=id_d)
    listForm = Form.objects.filter(Diagnosis=diag)
    if request.method != "POST":
        form = formForm()
    else:
        formAdd = formForm(request.POST)
        if formAdd.is_valid():
            f = Form()
            f.Diagnosis = diag
            f.Diagnos = Diagnos.objects.get(id=request.POST.get('diagnos'))
            f.Name = request.POST.get('name')
            f.Note = request.POST.get('note')
            f.Conviction = 0
            if f.DateForm is request.POST.get('dateForm', False):
                f.StartDiagnosis = request.POST.get('dateForm')
            f.save()
            return HttpResponseRedirect(
                reverse("view_diagnosis", args=[patient.id, user.login, treatment.id, diag.id]))
    context = {
        'login': login,
        'patient': patient,
        'user': user,
        'diagnosis': diag,
        "treatment": treatment,
        "listForm": listForm,
        "formForm": form
    }
    template = "core/view_diagnosis.html"
    return render(request, template, context)
    pass

#####
#Персона
def personal_cabinet(request, login):
    global g_login
    g_login = login
    formUser = UserForm()
    user = Doctor.objects.get(login = g_login)
    context = {
        'login':login,
        'formUser':formUser,
        'user': user
    }
    template = "core/personal_cabinet.html"
    
    return render(request, template, context)

def get_person(request):
    error=-1
    if request.method == "POST":
        login = request.POST.get("login")
        if Doctor.objects.all().filter(login = login):
            user = Doctor.objects.get(login = login)
            return HttpResponse(json.dumps({'id': user.id, 'FIO':user.FIO, 'email':user.email, 'password':user.password, 'social_network':user.SocialNetwork, 'position':user.Position, 'department':user.Department}), content_type="application/json")
    return HttpResponse(json.dumps({'id': error}), content_type="application/json")



def update_person(request):
    error=-1
    if request.method == "POST":
        login = request.POST.get("login")
        if Doctor.objects.all().filter(login = login):
            user = Doctor.objects.get(login = login)
            user.FIO = request.POST.get("FIO")
            user.email = request.POST.get("email")
            user.password = request.POST.get("password")
            user.SocialNetwork = request.POST.get("social_networks")
            user.Position = request.POST.get("position")
            user.Department = request.POST.get("department")
            user.save()
            return HttpResponse(json.dumps({'id': user.id, 'FIO':user.FIO, 'email':user.email, 'password':user.password, 'social_network':user.SocialNetwork, 'position':user.Position, 'department':user.Department}), content_type="application/json")
        else:
            error=-2
    return HttpResponse(json.dumps({'id': error}), content_type="application/json")

def add_syndrom(request):
    error=-1
    if request.method == "POST":
        iddiag = request.POST.get("idDiagSyn")
        idfreq = request.POST.get("idFreqSyn")
        rule = Rule()
        rule.Diagnos=Diagnos.objects.get(id=iddiag)
        rule.Frequency=Frequency.objects.get(id=idfreq)
        rule.save()
        error = rule.id
        return HttpResponse(json.dumps({'id': error, 'diag':rule.Diagnos.Name, 'freq':rule.Frequency.Name, 'num' :RuleSymptom.objects.all().filter(Rule=rule.id).count()}), content_type="application/json")
    return HttpResponse(json.dumps({'id': error}), content_type="application/json")


def open_syndrom(request, login, id):
    error=-1

    if RuleSymptom.objects.filter(Rule=id):
        symptoms = RuleSymptom.objects.all().filter(Rule=id)
    else:
        symptoms = []
    context = {
        'formRule': SyndromForm(),
        'fromSym':RuleSymptomForm(),
        'rule': Rule.objects.get(id=id),
        'symptomes': symptoms,
        'login': login
    }

    template = "core/edit_syndrom.html"
    return render(request, template, context)



#####
#Добавление правил
def delete_symrule(request):
    error=1
    if request.method == "POST":
        id = request.POST.get("id")
        if RuleSymptom.objects.all().filter(id=id):
            RuleSymptom.objects.all().filter(id=id).delete()
            error=0
    return HttpResponse(error)

def add_symrule(request):
    error=-1

    if request.method == "POST":
        idRul= request.POST.get("idSRuleRule")
        idSym = request.POST.get("idSymRule")
        idConv = request.POST.get("idConvRule")
        if not RuleSymptom.objects.all().filter(Symptom=idSym, Rule=idRul):
            ruleSymptom = RuleSymptom()
            ruleSymptom.Rule = Rule.objects.get(id=idRul)
            ruleSymptom.Symptom=Symptom.objects.get(id=idSym)
            ruleSymptom.Conviction=Conviction.objects.get(id=idConv)
            ruleSymptom.save()
            error=ruleSymptom.id
            return HttpResponse(json.dumps({'id': error, 'sym':ruleSymptom.Symptom.Name, 'conv':ruleSymptom.Conviction.Name}), content_type="application/json")
        else:
            error=-2

    return HttpResponse(json.dumps({'id': error}), content_type="application/json")

def get_symrule(request):
    error=-1
    if request.method == "POST":
        id = request.POST.get("id")
        if RuleSymptom.objects.all().filter(id=id):
            relsym = RuleSymptom.objects.get(id=id)
            return HttpResponse(json.dumps({'id': relsym.id, 'sym':relsym.Symptom.id, 'conv':relsym.Conviction.id,'namesym':relsym.Symptom.Name, 'nameconv':relsym.Conviction.Name}), content_type="application/json")
    return HttpResponse(json.dumps({'id': error}), content_type="application/json")

def update_symrule(request):
    error=-1
    if request.method == "POST":
        id = request.POST.get("idSymId")
        idRul= request.POST.get("idSRuleRule")
        idSym = request.POST.get("idSymRule")
        idConv = request.POST.get("idConvRule")
        if not RuleSymptom.objects.all().filter(Symptom=idSym, Rule=idRul):
            ruleSymptom = RuleSymptom.objects.get(id=id)
            ruleSymptom.Rule = Rule.objects.get(id=idRul)
            ruleSymptom.Symptom=Symptom.objects.get(id=idSym)
            ruleSymptom.Conviction=Conviction.objects.get(id=idConv)
            ruleSymptom.save()
            error=ruleSymptom.id
            return HttpResponse(json.dumps({'id': error, 'sym':ruleSymptom.Symptom.Name, 'conv':ruleSymptom.Conviction.Name}), content_type="application/json")
        else:
            error=-2
    return HttpResponse(json.dumps({'id': error}), content_type="application/json")

def update_syndrom(request):
    error=-1
    if request.method == "POST":
        id = request.POST.get("id")
        diag = request.POST.get("diag")
        freq = request.POST.get("freq")
        rule = Rule.objects.get(id=id)
        rule.Diagnos=Diagnos.objects.get(id=diag)
        rule.Frequency=Frequency.objects.get(id=freq)
        rule.save()
        error = rule.id
        return HttpResponse(json.dumps({'id': error}), content_type="application/json")
    return HttpResponse(json.dumps({'id': error}), content_type="application/json")

#####
#Вопросник
def questionary(request,login):

    id = Doctor.objects.get(login=login).id
    symptoms=SelectedSymptomsDoctor.objects.filter(Doctor=id)
    
    context = {
        'DocForm':DoctorSymptomForm(),
        'uDocFrom':uDoctorSymptomForm(),
        'symptomes': symptoms,
        'login':login
    }

    template = "core/questionary.html"
    return render(request, template, context)

def add_questdoc(request):
    error=-1

    if request.method == "POST":
        idSym = request.POST.get("idSym")
        idConv = request.POST.get("idConv")
        logDoc= request.POST.get("logDoc")
        idDoc = Doctor.objects.get(login=logDoc).id
        note= request.POST.get("note")
        if not SelectedSymptomsDoctor.objects.all().filter(Symptom=idSym, Doctor=idDoc):
            selectDoctor = SelectedSymptomsDoctor()
            selectDoctor.Doctor = Doctor.objects.get(id=idDoc)
            selectDoctor.Symptom=Symptom.objects.get(id=idSym)
            selectDoctor.Conviction=Conviction.objects.get(id=idConv)
            selectDoctor.Note=note
            selectDoctor.save()
            error=selectDoctor.id
            return HttpResponse(json.dumps({'id': error, 'sym':selectDoctor.Symptom.Name, 'conv':selectDoctor.Conviction.Name, 'note':selectDoctor.Note}), content_type="application/json")
        else:
            error=-2
    return HttpResponse(json.dumps({'id': error}), content_type="application/json")

def delete_questdoc(request):
    error=1
    if request.method == "POST":
        id = request.POST.get("id")
        if SelectedSymptomsDoctor.objects.all().filter(id=id):
            SelectedSymptomsDoctor.objects.all().filter(id=id).delete()
            error=0
    return HttpResponse(error)


def deleteall_questdoc(request):
    error=1
    if request.method == "POST":
        login = request.POST.get("login")
        if SelectedSymptomsDoctor.objects.all().filter(Doctor=Doctor.objects.get(login=login).id):
            SelectedSymptomsDoctor.objects.all().filter(Doctor=Doctor.objects.get(login=login).id).delete()
            error=0
    return HttpResponse(error)

def get_questdoc(request):
    error=-1
    if request.method == "POST":
        id = request.POST.get("id")
        if SelectedSymptomsDoctor.objects.all().filter(id=id):
            relsym = SelectedSymptomsDoctor.objects.get(id=id)
            return HttpResponse(json.dumps({'id': relsym.id, 'sym':relsym.Symptom.id, 'conv':relsym.Conviction.id, 'note':relsym.Note, 'namesym':relsym.Symptom.Name, 'nameconv':relsym.Conviction.Name}), content_type="application/json")
    return HttpResponse(json.dumps({'id': error}), content_type="application/json")

def update_questdoc(request):
    error=-1

    if request.method == "POST":
        id = request.POST.get("uqidSymId")
        idSym = request.POST.get("uqidSym")
        idConv = request.POST.get("uqidConv")
        logDoc= request.POST.get("uqlogDoc")
        idDoc = Doctor.objects.all().get(login=logDoc).id
        note= request.POST.get("uqnote")
        if not SelectedSymptomsDoctor.objects.all().filter(Symptom=idSym, Doctor=idDoc):
            selectDoctor = SelectedSymptomsDoctor.objects.get(id=id)
            selectDoctor.Doctor = Doctor.objects.get(id=idDoc)
            selectDoctor.Symptom=Symptom.objects.all().get(id=idSym)
            selectDoctor.Conviction=Conviction.objects.get(id=idConv)
            selectDoctor.Note=note
            selectDoctor.save()
            error=selectDoctor.id
            return HttpResponse(json.dumps({'id': error, 'sym':selectDoctor.Symptom.Name, 'conv':selectDoctor.Conviction.Name, 'note':selectDoctor.Note}), content_type="application/json")
        else:
            error=-2
    return HttpResponse(json.dumps({'id': error}), content_type="application/json")



def alg_mamdani_up(request):
    login = request.POST.get("login")
    idDoc = Doctor.objects.get(login=login).id
    selectsDoctor = SelectedSymptomsDoctor.objects.filter(Doctor=idDoc)
    diag_id, conv_id = alg_mamdani(selectsDoctor)

    if diag_id == -1:
        # Диагноз не найден
        return HttpResponse(json.dumps({'id': -1}), content_type="application/json")
    else:
        # Выдаем диагноз
        diag = Diagnos.objects.get(id=diag_id)
        return HttpResponse(json.dumps({'id': diag.id, 'name':diag.Name, 'idconv':conv_id, 'nameconv': Conviction.objects.get(id=conv_id).Name}), content_type="application/json")

    # selectDoctor.Symptom
    # selectDoctor.Conviction


def verity_conv(sim, rul):
    if sim==rul:
        return 1
    elif sim+1==rul or sim-1==rul:
        return 0.6
    else:
        return 0

def getid_conv(ver):
    if ver<=0.33:
        return 1
    elif ver<=0.66:
        return 2
    else:
        return 3

def alg_mamdani(selectsDoctor):

    ver_max=0
    id_max=[]
    ver_idmax=[]

    #Пробегаем по всем правилам
    for rule in Rule.objects.all():

        verity_rule=[]
        includeAll = False

        #Пробегаем по всем под условиям и проверяем вхождение в указанные симптомы
        for rsymti in RuleSymptom.objects.filter(Rule=rule.id):
            include = False
            #Если входит в правило, то назначаем подусловию истинность, иначе считаем нулевой
            for selectDoctor in selectsDoctor:
                if selectDoctor.Symptom.id==rsymti.Symptom.id:
                    include = True
                    includeAll = True
                    verity_rule.append(verity_conv(selectDoctor.Conviction.Position, rsymti.Conviction.Position))
            if not include:
                verity_rule.append(0)

        #Учитываем только те что включают хотябы один из симптомов
        if includeAll:
            #Добавляем в правило не совпавшие симптомы
            for selectDoctor in selectsDoctor:
                include = False
                for rsymti in RuleSymptom.objects.filter(Rule=rule.id):
                    if selectDoctor.Symptom.id==rsymti.Symptom.id:
                        include = True
                if not include:
                    verity_rule.append(0)
            #Получаем общее значение истинности
            mean_ver=0
            sum_ver=0
            for veri in verity_rule:
                sum_ver=sum_ver+veri
            mean_ver= sum_ver / len(verity_rule)

            #Получаем значение истинности заключения (поменял местами этапы, так проще, разницы нет)
            fin_ver=mean_ver*rule.Frequency.Coef

            if fin_ver>ver_max:
                ver_max=fin_ver
                id_max=[]
                ver_idmax=[]
                id_max.append(rule.Diagnos.id)
                ver_idmax.append(mean_ver)
            elif fin_ver == ver_max:
                id_max.append(rule.Diagnos.id)
                ver_idmax.append(mean_ver)

    if len(id_max)==0:
        # Диагноз не найден
        return -1, -1
    elif len(id_max)>1:
        # Выбираем один из
        ind = random.randint(0, len(id_max)-1)
        diag = Diagnos.objects.get(id=id_max[ind])
        conv =  Conviction.objects.get(Position = getid_conv(ver_idmax[ind]))
        return diag.id, conv.id
    else:
        # Выдаем диагноз
        diag = Diagnos.objects.get(id=id_max[0])
        conv =  Conviction.objects.get(Position = getid_conv(ver_idmax[0]))
        return diag.id, conv.id



###############################
#API
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PatientRecordSerializer
from .serializers import DoctorSerializer

from .serializers import GetPatientListSerializer
from .serializers import SetPatientListSerializer

from .serializers import GetTreatmentSerializer
from .serializers import SetTreatmentSerializer

from .serializers import GetEpicrisisSerializer
from .serializers import SetEpicrisisSerializer

from .serializers import GetDiagnosisSerializer
from .serializers import SetDiagnosisSerializer

from .serializers import DiagnosSerializer

from .serializers import GetFormSerializer
from .serializers import SetFormSerializer

from .serializers import GetRuleSerializer
from .serializers import SetRuleSerializer

from .serializers import SymptomSerializer

from .serializers import GetRuleSymptomSerializer
from .serializers import SetRuleSymptomSerializer

from .serializers import GetSelectedSymptomsSerializer
from .serializers import SetSelectedSymptomsSerializer

from .serializers import GetSelectedSymptomsDoctorSerializer
from .serializers import SetSelectedSymptomsDoctorSerializer

from .serializers import GetAnamesisSerializer
from .serializers import SetAnamesisSerializer

from django.db.models.base import ObjectDoesNotExist
from django.db import IntegrityError

#####
class PatientRecordView(APIView):
    def get(self, request):
        patientRecord = PatientRecord.objects.all()
        serializer = PatientRecordSerializer(patientRecord, many=True)
        return Response({"PatientRecord": serializer.data})

    def post(self, request):
        try:
            patientRecord = request.data.get('PatientRecord')
            serializer = PatientRecordSerializer(data=patientRecord)
            if serializer.is_valid(raise_exception=True):
                patientRecord_saved = serializer.save()
            return Response({"success": "'{}' created successfully".format(patientRecord_saved.id)})
        except ObjectDoesNotExist:
            return Response({"denied": "not updated"})
        except IntegrityError:
            return Response({"denied": "not updated"})

    def put(self, request, pk):
        try:
            saved_patient_record = get_object_or_404(PatientRecord.objects.all(), pk=pk)
            data = request.data.get('PatientRecord')
            serializer = PatientRecordSerializer(instance=saved_patient_record, data=data, partial=True)
            if serializer.is_valid(raise_exception=True):
                patient_record_saved = serializer.save()
            return Response({"success": "'{}' updated successfully".format(patient_record_saved.id)})
        except ObjectDoesNotExist:
            return Response({"denied": "not updated"})
        except IntegrityError:
            return Response({"denied": "not updated"})

    def delete(self, request, pk):
        article = get_object_or_404(PatientRecord.objects.all(), pk=pk)
        article.delete()
        return Response({"message": "`{}` has been deleted.".format(pk)}, status=204)

class SinglePatientRecordView(APIView):
    def get(self, request, pk):
        patientRecord = get_object_or_404(PatientRecord.objects.all(), pk=pk)
        serializer = PatientRecordSerializer(patientRecord)
        return Response({"PatientRecord": serializer.data})


#####
class DoctorView(APIView):
    def get(self, request, login):
        doctor = get_object_or_404(Doctor.objects.all(), login=login)
        serializer = DoctorSerializer(doctor)
        return Response({"Doctor": serializer.data})

    def put(self, request, login):
        try:
            saved_doctor = get_object_or_404(Doctor.objects.all(), login=login)
            data = request.data.get('Doctor')
            serializer = DoctorSerializer(instance=saved_doctor, data=data, partial=True)
            if serializer.is_valid(raise_exception=True):
                doctor_saved = serializer.save()
            return Response({"success": "'{}' updated successfully".format(doctor_saved.login)})
        except ObjectDoesNotExist:
            return Response({"denied": "not updated"})
        except IntegrityError:
            return Response({"denied": "not updated"})

class LoginDoctorView(APIView):
    def get(self, request, login, password):
        doctor = get_object_or_404(Doctor.objects.all(), login=login)
        if doctor.password==password:
            return Response({"Doctor": "true"})
        else:
            return Response({"Doctor": "false"})



#####
class PatientListView(APIView):
    def get(self, request):
        patientList = PatientList.objects.all()
        serializer = GetPatientListSerializer(patientList, many=True)
        return Response({"PatientList": serializer.data})

    def post(self, request):
        try:
            patientList = request.data.get('PatientList')
            serializer = SetPatientListSerializer(data=patientList)
            if serializer.is_valid(raise_exception=True):
                patientList_saved = serializer.save()
            return Response({"success": "'{}' created successfully".format(patientList_saved.id)})
        except ObjectDoesNotExist:
            return Response({"denied": "not created"})
        except IntegrityError:
            return Response({"denied": "not updated"})

    def put(self, request, pk):
        try:
            saved_patient_list = get_object_or_404(PatientList.objects.all(), pk=pk)
            data = request.data.get('PatientList')
            serializer = SetPatientListSerializer(instance=saved_patient_list, data=data, partial=True)
            if serializer.is_valid(raise_exception=True):
                patient_list_saved = serializer.save()
            return Response({"success": "'{}' updated successfully".format(patient_list_saved.id)})
        except ObjectDoesNotExist:
            return Response({"denied": "not updated"})
        except IntegrityError:
            return Response({"denied": "not updated"})

    def delete(self, request, pk):
        article = get_object_or_404(PatientList.objects.all(), pk=pk)
        article.delete()
        return Response({"message": "`{}` has been deleted.".format(pk)}, status=204)

class SinglePatientListView(APIView):
    def get(self, request, pk):
        patientList = get_object_or_404(PatientList.objects.all(), pk=pk)
        serializer = GetPatientListSerializer(patientList)
        return Response({"PatientList": serializer.data})


#####
class TreatmentView(APIView):
    def get(self, request):
        treatment = Treatment.objects.all()
        serializer = GetTreatmentSerializer(treatment, many=True)
        return Response({"Treatment": serializer.data})

    def post(self, request):
        try:
            treatment = request.data.get('Treatment')
            serializer = SetTreatmentSerializer(data=treatment)
            if serializer.is_valid(raise_exception=True):
                treatment_saved = serializer.save()
            return Response({"success": "'{}' created successfully".format(treatment_saved.id)})
        except ObjectDoesNotExist:
            return Response({"denied": "not created"})
        except IntegrityError:
            return Response({"denied": "not updated"})

    def put(self, request, pk):
        try:
            saved_treatment = get_object_or_404(Treatment.objects.all(), pk=pk)
            data = request.data.get('Treatment')
            serializer = SetTreatmentSerializer(instance=saved_treatment, data=data, partial=True)
            if serializer.is_valid(raise_exception=True):
                treatment_saved = serializer.save()
            return Response({"success": "'{}' updated successfully".format(treatment_saved.id)})
        except ObjectDoesNotExist:
            return Response({"denied": "not updated"})
        except IntegrityError:
            return Response({"denied": "not updated"})

    def delete(self, request, pk):
        article = get_object_or_404(Treatment.objects.all(), pk=pk)
        article.delete()
        return Response({"message": "`{}` has been deleted.".format(pk)}, status=204)

class SingleTreatmentView(APIView):
    def get(self, request, pk):
        treatment = get_object_or_404(Treatment.objects.all(), pk=pk)
        serializer = GetTreatmentSerializer(treatment)
        return Response({"Treatment": serializer.data})


#####
class EpicrisisView(APIView):
    def get(self, request):
        epicrisis = Epicrisis.objects.all()
        serializer = GetEpicrisisSerializer(epicrisis, many=True)
        return Response({"Epicrisis": serializer.data})

    def post(self, request):
        try:
            epicrisis = request.data.get('Epicrisis')
            serializer = SetEpicrisisSerializer(data=epicrisis)
            if serializer.is_valid(raise_exception=True):
                epicrisis_saved = serializer.save()
            return Response({"success": "'{}' created successfully".format(epicrisis_saved.id)})
        except ObjectDoesNotExist:
            return Response({"denied": "not created"})
        except IntegrityError:
            return Response({"denied": "not updated"})

    def put(self, request, pk):
        try:
            saved_epicrisis = get_object_or_404(Epicrisis.objects.all(), pk=pk)
            data = request.data.get('Epicrisis')
            serializer = SetEpicrisisSerializer(instance=saved_epicrisis, data=data, partial=True)
            if serializer.is_valid(raise_exception=True):
                epicrisis_saved = serializer.save()
            return Response({"success": "'{}' updated successfully".format(epicrisis_saved.id)})
        except ObjectDoesNotExist:
            return Response({"denied": "not updated"})
        except IntegrityError:
            return Response({"denied": "not updated"})

    def delete(self, request, pk):
        article = get_object_or_404(Epicrisis.objects.all(), pk=pk)
        article.delete()
        return Response({"message": "`{}` has been deleted.".format(pk)}, status=204)

class SingleEpicrisisView(APIView):
    def get(self, request, pk):
        epicrisis = get_object_or_404(Epicrisis.objects.all(), pk=pk)
        serializer = GetEpicrisisSerializer(epicrisis)
        return Response({"Epicrisis": serializer.data})


#####
class DiagnosisView(APIView):
    def get(self, request):
        diagnosis = Diagnosis.objects.all()
        serializer = GetDiagnosisSerializer(diagnosis, many=True)
        return Response({"Diagnosis": serializer.data})

    def post(self, request):
        try:
            diagnosis = request.data.get('Diagnosis')
            serializer = SetDiagnosisSerializer(data=diagnosis)
            if serializer.is_valid(raise_exception=True):
                diagnosis_saved = serializer.save()
            return Response({"success": "'{}' created successfully".format(diagnosis_saved.id)})
        except ObjectDoesNotExist:
            return Response({"denied": "not created"})
        except IntegrityError:
            return Response({"denied": "not updated"})

    def put(self, request, pk):
        try:
            saved_diagnosis = get_object_or_404(Diagnosis.objects.all(), pk=pk)
            data = request.data.get('Diagnosis')
            serializer = SetDiagnosisSerializer(instance=saved_diagnosis, data=data, partial=True)
            if serializer.is_valid(raise_exception=True):
                diagnosis_saved = serializer.save()
            return Response({"success": "'{}' updated successfully".format(diagnosis_saved.id)})
        except ObjectDoesNotExist:
            return Response({"denied": "not updated"})
        except IntegrityError:
            return Response({"denied": "not updated"})

    def delete(self, request, pk):
        diagnosis = get_object_or_404(Diagnosis.objects.all(), pk=pk)
        diagnosis.delete()
        return Response({"message": "`{}` has been deleted.".format(pk)}, status=204)

class SingleDiagnosisView(APIView):
    def get(self, request, pk):
        diagnosis = get_object_or_404(Diagnosis.objects.all(), pk=pk)
        serializer = GetDiagnosisSerializer(diagnosis)
        return Response({"Diagnosis": serializer.data})


#####
class DiagnosView(APIView):
    def get(self, request):
        diagnos = Diagnos.objects.all()
        serializer = DiagnosSerializer(diagnos, many=True)
        return Response({"Diagnos": serializer.data})

    def post(self, request):
        try:
            diagnos = request.data.get('Diagnos')
            serializer = DiagnosSerializer(data=diagnos)
            if serializer.is_valid(raise_exception=True):
                diagnos_saved = serializer.save()
            return Response({"success": "'{}' created successfully".format(diagnos_saved.id)})
        except ObjectDoesNotExist:
            return Response({"denied": "not created"})
        except IntegrityError:
            return Response({"denied": "not updated"})

    def put(self, request, pk):
        try:
            saved_diagnos = get_object_or_404(Diagnos.objects.all(), pk=pk)
            data = request.data.get('Diagnos')
            serializer = DiagnosSerializer(instance=saved_diagnos, data=data, partial=True)
            if serializer.is_valid(raise_exception=True):
                diagnos_saved = serializer.save()
            return Response({"success": "'{}' updated successfully".format(diagnos_saved.id)})
        except ObjectDoesNotExist:
            return Response({"denied": "not updated"})
        except IntegrityError:
            return Response({"denied": "not updated"})

    def delete(self, request, pk):
        diagnos = get_object_or_404(Diagnos.objects.all(), pk=pk)
        diagnos.delete()
        return Response({"message": "`{}` has been deleted.".format(pk)}, status=204)

class SingleDiagnosView(APIView):
    def get(self, request, pk):
        diagnos = get_object_or_404(Diagnos.objects.all(), pk=pk)
        serializer = DiagnosSerializer(diagnos)
        return Response({"Diagnos": serializer.data})


#####
class FormView(APIView):
    def get(self, request):
        form = Form.objects.all()
        serializer = GetFormSerializer(form, many=True)
        return Response({"Form": serializer.data})

    def post(self, request):
        try:
            form = request.data.get('Form')
            serializer = SetFormSerializer(data=form)
            if serializer.is_valid(raise_exception=True):
                form_saved = serializer.save()
            return Response({"success": "'{}' created successfully".format(form_saved.id)})
        except ObjectDoesNotExist:
            return Response({"denied": "not created"})
        except IntegrityError:
            return Response({"denied": "not updated"})

    def put(self, request, pk):
        try:
            saved_form = get_object_or_404(Form.objects.all(), pk=pk)
            data = request.data.get('Form')
            serializer = SetFormSerializer(instance=saved_form, data=data, partial=True)
            if serializer.is_valid(raise_exception=True):
                form_saved = serializer.save()
            return Response({"success": "'{}' updated successfully".format(form_saved.id)})
        except ObjectDoesNotExist:
            return Response({"denied": "not updated"})
        except IntegrityError:
            return Response({"denied": "not updated"})

    def delete(self, request, pk):
        form = get_object_or_404(Form.objects.all(), pk=pk)
        form.delete()
        return Response({"message": "`{}` has been deleted.".format(pk)}, status=204)

class SingleFormView(APIView):
    def get(self, request, pk):
        form = get_object_or_404(Form.objects.all(), pk=pk)
        serializer = GetFormSerializer(form)
        return Response({"Form": serializer.data})

#####
class RuleView(APIView):
    def get(self, request):
        rule = Rule.objects.all()
        serializer = GetRuleSerializer(rule, many=True)
        return Response({"Rule": serializer.data})

    def post(self, request):
        try:
            rule = request.data.get('Rule')
            serializer = SetRuleSerializer(data=rule)
            if serializer.is_valid(raise_exception=True):
                rule_saved = serializer.save()
            return Response({"success": "'{}' created successfully".format(rule_saved.id)})
        except ObjectDoesNotExist:
            return Response({"denied": "not updated"})
        except IntegrityError:
            return Response({"denied": "not updated"})

    def put(self, request, pk):
        try:
            saved_rule = get_object_or_404(Rule.objects.all(), pk=pk)
            data = request.data.get('Rule')
            serializer = SetRuleSerializer(instance=saved_rule, data=data, partial=True)
            if serializer.is_valid(raise_exception=True):
                rule_saved = serializer.save()
            return Response({"success": "'{}' updated successfully".format(rule_saved.id)})
        except ObjectDoesNotExist:
            return Response({"denied": "not updated"})
        except IntegrityError:
            return Response({"denied": "not updated"})

    def delete(self, request, pk):
        article = get_object_or_404(Rule.objects.all(), pk=pk)
        article.delete()
        return Response({"message": "`{}` has been deleted.".format(pk)}, status=204)

class SingleRuleView(APIView):
    def get(self, request, pk):
        rule = get_object_or_404(Rule.objects.all(), pk=pk)
        serializer = GetRuleSerializer(rule)
        return Response({"Rule": serializer.data})

#####
class SymptomView(APIView):
    def get(self, request):
        symptom = Symptom.objects.all()
        serializer = SymptomSerializer(symptom, many=True)
        return Response({"Symptom": serializer.data})

    def post(self, request):
        try:
            symptom = request.data.get('Symptom')
            serializer = SymptomSerializer(data=symptom)
            if serializer.is_valid(raise_exception=True):
                symptom_saved = serializer.save()
            return Response({"success": "'{}' created successfully".format(symptom_saved.id)})
        except ObjectDoesNotExist:
            return Response({"denied": "not created"})
        except IntegrityError:
            return Response({"denied": "not updated"})

    def put(self, request, pk):
        try:
            saved_symptom = get_object_or_404(Symptom.objects.all(), pk=pk)
            data = request.data.get('Symptom')
            serializer = SymptomSerializer(instance=saved_symptom, data=data, partial=True)
            if serializer.is_valid(raise_exception=True):
                symptom_saved = serializer.save()
            return Response({"success": "'{}' updated successfully".format(symptom_saved.id)})
        except ObjectDoesNotExist:
            return Response({"denied": "not updated"})
        except IntegrityError:
            return Response({"denied": "not updated"})

    def delete(self, request, pk):
        symptom = get_object_or_404(Symptom.objects.all(), pk=pk)
        symptom.delete()
        return Response({"message": "`{}` has been deleted.".format(pk)}, status=204)

class SingleSymptomView(APIView):
    def get(self, request, pk):
        symptom = get_object_or_404(Symptom.objects.all(), pk=pk)
        serializer = SymptomSerializer(symptom)
        return Response({"Symptom": serializer.data})


#####
class RuleSymptomView(APIView):
    def get(self, request):
        ruleSymptom = RuleSymptom.objects.all()
        serializer = GetRuleSymptomSerializer(ruleSymptom, many=True)
        return Response({"RuleSymptom": serializer.data})

    def post(self, request):
        try:
            ruleSymptom = request.data.get('RuleSymptom')
            serializer = SetRuleSymptomSerializer(data=ruleSymptom)
            if serializer.is_valid(raise_exception=True):
                ruleSymptom_saved = serializer.save()
            return Response({"success": "'{}' created successfully".format(ruleSymptom_saved.id)})
        except ObjectDoesNotExist:
            return Response({"denied": "not updated"})
        except IntegrityError:
            return Response({"denied": "not updated"})

    def put(self, request, pk):
        try:
            saved_ruleSymptom = get_object_or_404(RuleSymptom.objects.all(), pk=pk)
            data = request.data.get('RuleSymptom')
            serializer = SetRuleSymptomSerializer(instance=saved_ruleSymptom, data=data, partial=True)
            if serializer.is_valid(raise_exception=True):
                ruleSymptom_saved = serializer.save()
            return Response({"success": "'{}' updated successfully".format(ruleSymptom_saved.id)})
        except ObjectDoesNotExist:
            return Response({"denied": "not updated"})
        except IntegrityError:
            return Response({"denied": "not updated"})

    def delete(self, request, pk):
        ruleSymptom = get_object_or_404(RuleSymptom.objects.all(), pk=pk)
        ruleSymptom.delete()
        return Response({"message": "`{}` has been deleted.".format(pk)}, status=204)

class SingleRuleSymptomView(APIView):
    def get(self, request, pk):
        ruleSymptom = get_object_or_404(RuleSymptom.objects.all(), pk=pk)
        serializer = GetRuleSymptomSerializer(ruleSymptom)
        return Response({"RuleSymptom": serializer.data})


#####
class SelectedSymptomsView(APIView):
    def get(self, request):
        selectedSymptoms = SelectedSymptoms.objects.all()
        serializer = GetSelectedSymptomsSerializer(selectedSymptoms, many=True)
        return Response({"SelectedSymptoms": serializer.data})

    def post(self, request):
        try:
            selectedSymptoms = request.data.get('SelectedSymptoms')
            serializer = SetSelectedSymptomsSerializer(data=selectedSymptoms)
            if serializer.is_valid(raise_exception=True):
                selectedSymptoms_saved = serializer.save()
            return Response({"success": "'{}' created successfully".format(selectedSymptoms_saved.id)})
        except ObjectDoesNotExist:
            return Response({"denied": "not updated"})
        except IntegrityError:
            return Response({"denied": "not updated"})

    def put(self, request, pk):
        try:
            saved_selectedSymptoms = get_object_or_404(SelectedSymptoms.objects.all(), pk=pk)
            data = request.data.get('SelectedSymptoms')
            serializer = SetSelectedSymptomsSerializer(instance=saved_selectedSymptoms, data=data, partial=True)
            if serializer.is_valid(raise_exception=True):
                selectedSymptoms_saved = serializer.save()
            return Response({"success": "'{}' updated successfully".format(selectedSymptoms_saved.id)})
        except ObjectDoesNotExist:
            return Response({"denied": "not updated"})
        except IntegrityError:
            return Response({"denied": "not updated"})

    def delete(self, request, pk):
        selectedSymptoms = get_object_or_404(SelectedSymptoms.objects.all(), pk=pk)
        selectedSymptoms.delete()
        return Response({"message": "`{}` has been deleted.".format(pk)}, status=204)

class SingleSelectedSymptomsView(APIView):
    def get(self, request, pk):
        selectedSymptoms = get_object_or_404(SelectedSymptoms.objects.all(), pk=pk)
        serializer = GetSelectedSymptomsSerializer(selectedSymptoms)
        return Response({"SelectedSymptoms": serializer.data})


#####
class SelectedSymptomsDoctorView(APIView):
    def get(self, request):
        selectedSymptomsDoctor = SelectedSymptomsDoctor.objects.all()
        serializer = GetSelectedSymptomsDoctorSerializer(selectedSymptomsDoctor, many=True)
        return Response({"SelectedSymptomsDoctor": serializer.data})

    def post(self, request):
        try:
            selectedSymptomsDoctor = request.data.get('SelectedSymptomsDoctor')
            serializer = SetSelectedSymptomsDoctorSerializer(data=selectedSymptomsDoctor)
            if serializer.is_valid(raise_exception=True):
                selectedSymptomsDoctor_saved = serializer.save()
            return Response({"success": "'{}' created successfully".format(selectedSymptomsDoctor_saved.id)})
        except ObjectDoesNotExist:
            return Response({"denied": "not updated"})
        except IntegrityError:
            return Response({"denied": "not updated"})

    def put(self, request, pk):
        try:
            saved_selectedSymptomsDoctor = get_object_or_404(SelectedSymptomsDoctor.objects.all(), pk=pk)
            data = request.data.get('SelectedSymptomsDoctor')
            serializer = SetSelectedSymptomsDoctorSerializer(instance=saved_selectedSymptomsDoctor, data=data, partial=True)
            if serializer.is_valid(raise_exception=True):
                selectedSymptomsDoctor_saved = serializer.save()
            return Response({"success": "'{}' updated successfully".format(selectedSymptomsDoctor_saved.id)})
        except ObjectDoesNotExist:
            return Response({"denied": "not updated"})
        except IntegrityError:
            return Response({"denied": "not updated"})

    def delete(self, request, pk):
        selectedSymptomsDoctor = get_object_or_404(SelectedSymptomsDoctor.objects.all(), pk=pk)
        selectedSymptomsDoctor.delete()
        return Response({"message": "`{}` has been deleted.".format(pk)}, status=204)

class SingleSelectedSymptomsDoctorView(APIView):
    def get(self, request, pk):
        selectedSymptomsDoctor = get_object_or_404(SelectedSymptomsDoctor.objects.all(), pk=pk)
        serializer = GetSelectedSymptomsDoctorSerializer(selectedSymptomsDoctor)
        return Response({"SelectedSymptomsDoctor": serializer.data})


#####
class AnamesisView(APIView):
    def get(self, request):
        anamesis = Anamesis.objects.all()
        serializer = GetAnamesisSerializer(anamesis, many=True)
        return Response({"Anamesis": serializer.data})

    def post(self, request):
        try:
            anamesis = request.data.get('Anamesis')
            serializer = SetAnamesisSerializer(data=anamesis)
            if serializer.is_valid(raise_exception=True):
                anamesis_saved = serializer.save()
            return Response({"success": "'{}' created successfully".format(anamesis_saved.id)})
        except ObjectDoesNotExist:
            return Response({"denied": "not updated"})

    def put(self, request, pk):
        saved_anamesis = get_object_or_404(Anamesis.objects.all(), pk=pk)
        data = request.data.get('Anamesis')
        serializer = SetAnamesisSerializer(instance=saved_anamesis, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            anamesis_saved = serializer.save()
        return Response({"success": "'{}' updated successfully".format(anamesis_saved.id)})

    def delete(self, request, pk):
        anamesis = get_object_or_404(Anamesis.objects.all(), pk=pk)
        anamesis.delete()
        return Response({"message": "`{}` has been deleted.".format(pk)}, status=204)

class SingleAnamesisView(APIView):
    def get(self, request, pk):
        anamesis = get_object_or_404(Anamesis.objects.all(), pk=pk)
        serializer = GetAnamesisSerializer(anamesis)
        return Response({"Anamesis": serializer.data})

#####
class MamdaniDocView(APIView):
    def get(self, request, login):
        idDoc = get_object_or_404(Doctor.objects.all(), login=login).id
        selectsDoctor = SelectedSymptomsDoctor.objects.filter(Doctor=idDoc)
        diag_id, conv_id = alg_mamdani(selectsDoctor)

        if diag_id == -1:
            # Диагноз не найден
            return HttpResponse({'id': -1})
        else:
            # Выдаем диагноз
            diag = Diagnos.objects.get(id=diag_id)
            return Response({'id': diag.id, 'name':diag.Name, 'idconv':conv_id, 'nameconv': Conviction.objects.get(id=conv_id).Name})

class MamdaniFormView(APIView):
    def get(self, request, pk):
        selectsDoctor = SelectedSymptoms.objects.filter(Form=pk)
        diag_id, conv_id = alg_mamdani(selectsDoctor)

        if diag_id == -1:
            # Диагноз не найден
            return Response({'id': -1})
        else:
            # Выдаем диагноз
            diag = Diagnos.objects.get(id=diag_id)
            return Response({'id': diag.id, 'name':diag.Name, 'idconv':conv_id, 'nameconv': Conviction.objects.get(id=conv_id).Name})


