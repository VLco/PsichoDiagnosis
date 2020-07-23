from django.db import models


class PatientRecord(models.Model):
    NumberRecord = models.CharField(max_length=200, verbose_name='number record')
    FIO = models.CharField(max_length=200, verbose_name='FIO')
    Birthday = models.DateField(default = "1999-01-01", null=True)
    Sex = models.CharField(max_length=200, verbose_name='sex')
    Adress = models.CharField(max_length=200, verbose_name='adress')
    Phone = models.CharField(max_length=50, verbose_name='phone')

    class Meta():
        verbose_name = 'patient'
        verbose_name_plural = 'patients'


class Doctor(models.Model):
    Patient = models.ManyToManyField(PatientRecord, through='PatientList')
    login = models.CharField(max_length=200, verbose_name='login')
    email = models.CharField(max_length=200, verbose_name='email')
    password = models.CharField(max_length=50, verbose_name='password')
    FIO = models.CharField(max_length=50, verbose_name='last first middle name', default="")
    SocialNetwork = models.CharField(max_length=50, verbose_name='SocialNetwork', default="")
    Postion = models.CharField(max_length=50, verbose_name='position', default="")
    Department = models.CharField(max_length=50, verbose_name='department', default="")

    def __str__(self):
        return self.login

    class Meta():
        verbose_name = 'doctor'
        verbose_name_plural = 'doctors'





class PatientList(models.Model):
    Doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    PatientRecord = models.ForeignKey(PatientRecord, on_delete=models.CASCADE)


class Treatment(models.Model):
    Record = models.ForeignKey(PatientRecord, on_delete=models.CASCADE)
    Doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Name = models.CharField(max_length=200, verbose_name='name')
    Note = models.CharField(max_length=5000, verbose_name='note')

    class Meta():
        verbose_name = 'treatment'
        verbose_name_plural = 'treatments'


class Epicrisis(models.Model):
    Treatment = models.OneToOneField(Treatment,on_delete=models.CASCADE)
    Referral = models.CharField(max_length=1000, verbose_name='referral')
    Therapy = models.CharField(max_length=50000, verbose_name='therapy')
    Disability = models.CharField(max_length=1000, verbose_name='disability')
    Hospitalization = models.DateField(default = "1999-01-01", null=True)
    HospitalDischarge = models.DateField(default="1999-01-01", null=True)
    IsOver = models.IntegerField()

    class Meta():
        verbose_name = 'epicrisis'
        verbose_name_plural = 'epicrises'


class Diagnosis(models.Model):
    Treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)
    Doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Name = models.CharField(max_length=1000, verbose_name='name')
    StartDiagnosis = models.DateField(default = "1999-01-01", null=True)
    Note = models.CharField(max_length=50000, verbose_name='note')

    class Meta():
        verbose_name = 'diagnosis'
        verbose_name_plural = 'diagnostics'


class Diagnos(models.Model):
    Name = models.CharField(max_length=1000, verbose_name='name')
    Description = models.CharField(max_length=50000, verbose_name='description')

    class Meta():
        verbose_name = 'diagnos'
        verbose_name_plural = 'diagnoses'


class Form(models.Model):
    Diagnosis = models.ForeignKey(Diagnosis, on_delete=models.CASCADE)
    Diagnos = models.ForeignKey(Diagnos, on_delete=models.CASCADE)
    Name = models.CharField(max_length=1000, verbose_name='name')
    DateForm = models.DateField(default = "1999-01-01", null=True)
    Note = models.CharField(max_length=50000, verbose_name='note')
    Conviction = models.IntegerField()

    class Meta():
        verbose_name = 'form'
        verbose_name_plural = 'forms'


class Conviction(models.Model):
    Name = models.CharField(max_length=1000, verbose_name='name')
    Position = models.IntegerField()

    class Meta():
        verbose_name = 'conviction'
        verbose_name_plural = 'convictions'

class Frequency(models.Model):
    Name = models.CharField(max_length=1000, verbose_name='name')
    Coef = models.FloatField()

    class Meta():
        verbose_name = 'frequency'
        verbose_name_plural = 'frequency'

class Rule(models.Model):
    Diagnos = models.ForeignKey(Diagnos, on_delete=models.CASCADE)
    Frequency = models.ForeignKey(Frequency, on_delete=models.CASCADE)

    class Meta():
        verbose_name = 'rule'
        verbose_name_plural = 'rules'

class Symptom(models.Model):
    Name = models.CharField(max_length=1000, verbose_name='name')
    Description = models.CharField(max_length=50000, verbose_name='description')

    class Meta():
        verbose_name = 'symptom'
        verbose_name_plural = 'symptoms'

class RuleSymptom(models.Model):
    Rule = models.OneToOneField(Rule, on_delete=models.CASCADE)
    Symptom = models.ForeignKey(Symptom, on_delete=models.CASCADE)
    Conviction = models.ForeignKey(Conviction, on_delete=models.CASCADE)

    class Meta():
        verbose_name = 'rule symptom'
        verbose_name_plural = 'rules symptom'




class SelectedSymptoms(models.Model):
    Form = models.ForeignKey(Form, on_delete=models.CASCADE)
    Symptom = models.ForeignKey(Symptom, on_delete=models.CASCADE)
    Conviction = models.ForeignKey(Conviction, on_delete=models.CASCADE)
    Note = models.CharField(max_length=50000, verbose_name='note')

    class Meta():
        verbose_name = 'selected symptom'
        verbose_name_plural = 'selected symptoms'

class Anamesis(models.Model):
    Treatment = models.OneToOneField(Treatment, on_delete=models.CASCADE)
    Diagnos = models.ForeignKey(Diagnos, on_delete=models.CASCADE)

    class Meta():
        verbose_name = 'Anamesis'
        verbose_name_plural = 'Anamesises'


