import datetime

from django import forms
from django.core.exceptions import ValidationError


# from .models import User
# #from .models import Doctor
# from .models import Patient
# from .models import Ancket
# from .models import Question
# from .models import Disease
# from .models import Epicriz
# from .models import Diagnos
# from .models import Rule
# from .models import PravilaRule
from .models import Frequency
from .models import Diagnos
from .models import Symptom
from .models import Conviction
from .models import Rule

class SigninForm(forms.Form):
    login = forms.CharField(max_length=50, label="login")
    password = forms.CharField(max_length=50, label="password", widget=forms.PasswordInput())
    isAdmin = forms.BooleanField(required=False, label='i am admin')

    login.widget.attrs.update({'class': 'form-control'})
    password.widget.attrs.update({'class': 'form-control'})
    isAdmin.widget.attrs.update({'class': 'form-control'})



class RegisterForm(forms.Form):
    login = forms.CharField(max_length=50, label="login")
    email = forms.CharField(max_length=50, label="email")
    password = forms.CharField(max_length=50, label="password", widget=forms.PasswordInput())
    rePassword = forms.CharField(max_length=50, label="repeat password", widget=forms.PasswordInput())
    
    login.widget.attrs.update({'class': 'form-control'})
    email.widget.attrs.update({'class': 'form-control'})
    password.widget.attrs.update({'class': 'form-control'})
    rePassword.widget.attrs.update({'class': 'form-control'})

    

class DbPatientsForm(forms.Form):
    number_card = forms.CharField(required='', max_length=50, label="number card")
    FIO = forms.CharField(required='', max_length=100, label="First last middle name")
    date_birth = forms.CharField(required='', label='birthday', widget=forms.TextInput(attrs={'placeholder': 'Please use the following format: YYYY-MM-DD'}))
    sex = forms.CharField(required='', max_length=50, label="sex")
    nationality = forms.CharField(required='', max_length=50, label="nationality")
    education = forms.CharField(required='', max_length=100, label="education")
    address = forms.CharField(required='', max_length=100, label="adress")
    phone = forms.CharField(required='', max_length=50, label="phons")
    job = forms.CharField(required='', max_length=100, label="where work")
    position = forms.CharField(required='', max_length=100, label="position")

    number_card.widget.attrs.update({'class': 'form-control'})
    FIO.widget.attrs.update({'class': 'form-control'})
    date_birth.widget.attrs.update({'class': 'form-control'})
    sex.widget.attrs.update({'class': 'form-control'})
    nationality.widget.attrs.update({'class': 'form-control'})
    education.widget.attrs.update({'class': 'form-control'})
    address.widget.attrs.update({'class': 'form-control'})
    phone.widget.attrs.update({'class': 'form-control'})
    job.widget.attrs.update({'class': 'form-control'})
    position.widget.attrs.update({'class': 'form-control'})

    
class DbQuestionsForm(forms.Form):
    question_id = forms.IntegerField(required='', label="id")
    question = forms.CharField(required='', max_length=100, label="First last middle name")

    question_id.widget.attrs.update({'class': 'form-control'})
    question.widget.attrs.update({'class': 'form-control'})

class DbDiseasesForm(forms.Form):
    diseases_id = forms.IntegerField(required='', label="id")
    name = forms.CharField(required='', max_length=100, label="name")
    note = forms.CharField(required='', label="note")

    diseases_id.widget.attrs.update({'class': 'form-control'})
    name.widget.attrs.update({'class': 'form-control'})
    note.widget.attrs.update({'class': 'form-control'})

# анкета
# class DBAncketsForm(forms.Form):
#     number_card = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
#     number_ancket = forms.CharField(required='', label="card")
#     question = forms.ModelChoiceField (queryset = Question.objects.all(),to_field_name="question")
#     answer = forms.CharField(required='', label="answer")
#     conviction = forms.IntegerField(required='', label="conviction")

#     number_card.widget.attrs.update({'class': 'form-control'})
#     number_ancket.widget.attrs.update({'class': 'form-control'})
#     question.widget.attrs.update({'class': 'form-control'})
#     answer.widget.attrs.update({'class': 'form-control'})
#     conviction.widget.attrs.update({'class': 'form-control'})
    
class PostuplenieForm(forms.Form):
    number_card = forms.IntegerField(label="number card")

    number_card.widget.attrs.update({'class': 'form-control'})


class ProfileForm(forms.Form):
    FIO = forms.CharField(required='', label="First last middle name doctor")
    login = forms.CharField(required='', label="login")
    position = forms.CharField(required='', label="position")
    department = forms.CharField(required='', label="department")
    password = forms.CharField(label="login", widget=forms.PasswordInput())

    FIO.widget.attrs.update({'class': 'form-control'})
    login.widget.attrs.update({'class': 'form-control'})
    position.widget.attrs.update({'class': 'form-control'})
    department.widget.attrs.update({'class': 'form-control'})
    password.widget.attrs.update({'class': 'form-control'})
    
class DBEpicrizForm(forms.Form):
    number_card = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    number_epic = forms.CharField(required='')
    invalid = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    lechenie = forms.CharField(required='', label='lechenie')
    date_gospit = forms.CharField(required='', label='date hospital', widget=forms.TextInput(attrs={'placeholder': 'Please use the following format: YYYY-MM-DD'}))
    date_vipisky = forms.CharField(required='', label='date out', widget=forms.TextInput(attrs={'placeholder': 'Please use the following format: YYYY-MM-DD'}))

    number_card.widget.attrs.update({'class': 'form-control'})
    number_epic.widget.attrs.update({'class': 'form-control'})
    invalid.widget.attrs.update({'class': 'form-control'})
    lechenie.widget.attrs.update({'class': 'form-control'})
    date_gospit.widget.attrs.update({'class': 'form-control'})
    date_vipisky.widget.attrs.update({'class': 'form-control'})

# class DbDiagnosesForm(forms.Form):
#     number_card = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}), label="card")
#     number_diag = forms.CharField(required='', label="id diagnoses")
#     note = forms.CharField(required='', max_length=100, label="diagnoses note")
#     disease = forms.ModelChoiceField (queryset = Disease.objects.all(), to_field_name="name", label="disease")
#     epicriz = forms.ModelChoiceField (queryset = Epicriz.objects.all(), to_field_name="lechenie", label="epicris")

#     number_card.widget.attrs.update({'class': 'form-control'})
#     number_diag.widget.attrs.update({'class': 'form-control'})
#     note.widget.attrs.update({'class': 'form-control'})
#     disease.widget.attrs.update({'class': 'form-control'})
#     epicriz.widget.attrs.update({'class': 'form-control'})

# class WorkWithRulesForm(forms.Form):
#     c =[("1", "small"), ("2", "big"), ("3", "larger")]
#     symptom1 = forms.ModelChoiceField (queryset = Question.objects.all(), to_field_name="question", label="question")
#     # conviction1 = forms.IntegerField(label="conviction",  max_value = 100, min_value = 0)
#     conviction1 = forms.ChoiceField(choices=c, label="Choices") 
#     symptom2 = forms.ModelChoiceField (queryset = Question.objects.all(), to_field_name="question", label="question")
#     # conviction2 = forms.IntegerField(label="conviction",  max_value = 100, min_value = 0)
#     conviction2 = forms.ChoiceField(choices=c, label="Choices") 
#     symptom3 = forms.ModelChoiceField (queryset = Question.objects.all(), to_field_name="question", label="question")
#     # conviction3 = forms.IntegerField(label="conviction",  max_value = 100, min_value = 0)
#     conviction3 = forms.ChoiceField(choices=c, label="Choices") 
#     symptom4 = forms.ModelChoiceField (queryset = Question.objects.all(), to_field_name="question", label="question")
#     # conviction4 = forms.IntegerField(label="conviction",  max_value = 100, min_value = 0)
#     conviction4 = forms.ChoiceField(choices=c, label="Choices") 
#     diagnose_result = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
#     conviction_result = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))


#     symptom1.widget.attrs.update({'class': 'form-control'})   
#     conviction1.widget.attrs.update({'class': 'form-control'})
#     symptom2.widget.attrs.update({'class': 'form-control'})   
#     conviction2.widget.attrs.update({'class': 'form-control'})
#     symptom3.widget.attrs.update({'class': 'form-control'})   
#     conviction3.widget.attrs.update({'class': 'form-control'})
#     symptom4.widget.attrs.update({'class': 'form-control'})   
#     conviction4.widget.attrs.update({'class': 'form-control'})
#     diagnose_result.widget.attrs.update({'class': 'form-control'})   
#     conviction_result.widget.attrs.update({'class': 'form-control'})

# class DBSymptomsForm(forms.Form):
#     pravila_id = forms.CharField(required='')
#     diagnos = forms.ModelChoiceField (queryset = Disease.objects.all(), to_field_name="name", label="Diagnos")
#     question = forms.ModelChoiceField (queryset = Question.objects.all(), to_field_name="question", label="question")
#     conviction = forms.IntegerField(label="conviction",  max_value = 100, min_value = 0)

#     pravila_id.widget.attrs.update({'class': 'form-control'})
#     diagnos.widget.attrs.update({'class': 'form-control'})
#     question.widget.attrs.update({'class': 'form-control'})
#     conviction.widget.attrs.update({'class': 'form-control'})


class DiagnosesForm(forms.Form):
    idRowDiag = forms.IntegerField(required='', label="")
    idDiag = forms.IntegerField(required='', label="")
    nameDiag = forms.CharField(required='', max_length=1000, label="name diagnos")
    descriptionDiag = forms.CharField(required='',max_length=5000, widget=forms.Textarea, label="description diagnos")
    nameDiag.widget.attrs.update({'class': 'form-control'})
    descriptionDiag.widget.attrs.update({'class': 'form-control'})

class SymptomesForm(forms.Form):
    idRowSym= forms.IntegerField(required='', label="")
    idSym = forms.IntegerField(required='', label="")
    nameSym = forms.CharField(required='', max_length=1000, label="name symptom")
    descriptionSym = forms.CharField(required='',max_length=5000, widget=forms.Textarea, label="description symptom")
    nameSym.widget.attrs.update({'class': 'form-control'})
    descriptionSym.widget.attrs.update({'class': 'form-control'})

class PatientsForm(forms.Form):
    idRowPatient= forms.IntegerField(required='', label="")
    idPatient = forms.IntegerField(required='', label="")
    number_card = forms.CharField(required='', max_length=50, label="number card")
    FIO = forms.CharField(required='', max_length=100, label="First last middle name")
    date_birth = forms.CharField(required='', label='birthday', widget=forms.TextInput(attrs={'placeholder': 'Please use the following format: YYYY-MM-DD'}))
    sex = forms.CharField(required='', max_length=50, label="sex")
    address = forms.CharField(required='', max_length=100, label="adress")
    phone = forms.CharField(required='', max_length=50, label="phons")

    number_card.widget.attrs.update({'class': 'form-control'})
    FIO.widget.attrs.update({'class': 'form-control'})
    date_birth.widget.attrs.update({'class': 'form-control'})
    sex.widget.attrs.update({'class': 'form-control'})
    address.widget.attrs.update({'class': 'form-control'})
    phone.widget.attrs.update({'class': 'form-control'})

class UserForm(forms.Form):
    FIO = forms.CharField(required='', max_length=50, label="FIO")
    email = forms.CharField(required='', max_length=100, label="email")
    password = forms.CharField(required='', max_length=100, label="password")
    social_networks = forms.CharField(required='', max_length=100, label="social_networks")
    position = forms.CharField(required='', max_length=100, label="position")
    department = forms.CharField(required='', max_length=100, label="department")

    FIO.widget.attrs.update({'class': 'form-control'})
    email.widget.attrs.update({'class': 'form-control'})
    password.widget.attrs.update({'class': 'form-control'})
    social_networks.widget.attrs.update({'class': 'form-control'})
    position.widget.attrs.update({'class': 'form-control'})
    department.widget.attrs.update({'class': 'form-control'})

class SyndromesForm(forms.Form):
    idDiagSyn = forms.ModelChoiceField(queryset=Diagnos.objects.all(), to_field_name="id", label="diagnos")
    idFreqSyn = forms.ModelChoiceField(queryset=Frequency.objects.all(), to_field_name="id", label="frequency")


    idDiagSyn.widget.attrs.update({'class': 'form-control'})
    idFreqSyn.widget.attrs.update({'class': 'form-control'})

class SyndromForm(forms.Form):
    idRule = forms.IntegerField(required='', label="")
    idDiagSyn = forms.ModelChoiceField(queryset=Diagnos.objects.all(), to_field_name="id", label="diagnos")
    idFreqSyn = forms.ModelChoiceField(queryset=Frequency.objects.all(), to_field_name="id", label="frequency")


    idDiagSyn.widget.attrs.update({'class': 'form-control'})
    idFreqSyn.widget.attrs.update({'class': 'form-control'})

class RuleSymptomForm(forms.Form):
    idSymRow= forms.IntegerField(required='', label="")
    idSymId= forms.IntegerField(required='', label="")
    idSRuleRule = forms.IntegerField(required='', label="")
    idSymRule = forms.ModelChoiceField(queryset=Symptom.objects.all(), to_field_name="id", label="symptom")
    idConvRule = forms.ModelChoiceField(queryset=Conviction.objects.all(), to_field_name="id", label="conviction")

    idSymRule.widget.attrs.update({'class': 'form-control'})
    idConvRule.widget.attrs.update({'class': 'form-control'})

class DoctorSymptomForm(forms.Form):
    idSymRow= forms.IntegerField(required='', label="")
    idSymId= forms.IntegerField(required='', label="")
    logDoc = forms.CharField(required='', label="")
    idSym = forms.ModelChoiceField(queryset=Symptom.objects.all(), to_field_name="id", label="symptom")
    idConv = forms.ModelChoiceField(queryset=Conviction.objects.all(), to_field_name="id", label="conviction")
    note = forms.CharField(required='',max_length=1000, widget=forms.Textarea(attrs={'rows': 2, 'cols': 40}), label="description symptom")

    idSym.widget.attrs.update({'class': 'form-control'})
    idConv.widget.attrs.update({'class': 'form-control'})
    note.widget.attrs.update({'class': 'form-control'})

class uDoctorSymptomForm(forms.Form):
    uqidSymRow= forms.IntegerField(required='', label="")
    uqidSymId= forms.IntegerField(required='', label="")
    uqlogDoc = forms.CharField(required='', label="")
    uqidSym = forms.ModelChoiceField(queryset=Symptom.objects.all(), to_field_name="id", label="symptoms")
    uqidConv = forms.ModelChoiceField(queryset=Conviction.objects.all(), to_field_name="id", label="convictions")
    uqnote = forms.CharField(required='',max_length=1000, widget=forms.Textarea(attrs={'rows': 2, 'cols': 40}), label="description symptoms")

    uqidSym.widget.attrs.update({'class': 'form-control'})
    uqidConv.widget.attrs.update({'class': 'form-control'})
    uqnote.widget.attrs.update({'class': 'form-control'})


