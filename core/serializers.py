from rest_framework import serializers

from .models import PatientRecord
from .models import Doctor
from .models import PatientList
from .models import Treatment
from .models import Epicrisis
from .models import Diagnosis
from .models import Diagnos
from .models import Form
from .models import Conviction
from .models import Frequency
from .models import Rule
from .models import Symptom
from .models import RuleSymptom
from .models import SelectedSymptoms
from .models import SelectedSymptomsDoctor
from .models import Anamesis

#####
class PatientRecordSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    NumberRecord = serializers.CharField(max_length=200)
    FIO = serializers.CharField(max_length=200)
    Birthday = serializers.DateField(default = "1999-01-01")
    Sex = serializers.CharField(max_length=200, required=False)
    Adress = serializers.CharField(max_length=200, required=False)
    Phone = serializers.CharField(max_length=50, required=False)

    def create(self, validated_data):
        return PatientRecord.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.NumberRecord = validated_data.get('NumberRecord', instance.NumberRecord)
        instance.FIO = validated_data.get('FIO', instance.FIO)
        instance.Birthday = validated_data.get('Birthday', instance.Birthday)
        instance.Sex = validated_data.get('Sex', instance.Sex)
        instance.Adress = validated_data.get('Adress', instance.Adress)
        instance.Phone = validated_data.get('Phone', instance.Phone)
        instance.save()
        return instance

#####
class DoctorSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    login = serializers.CharField(max_length=200, required=False)
    email = serializers.CharField(max_length=200, required=False)
    password = serializers.CharField(max_length=50, required=False)
    FIO = serializers.CharField(max_length=50, required=False)
    SocialNetwork = serializers.CharField(max_length=50, required=False)
    Position = serializers.CharField(max_length=50, required=False)
    Department = serializers.CharField(max_length=50, required=False)
    
    def update(self, instance, validated_data):
        instance.login = validated_data.get('login', instance.login)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.FIO = validated_data.get('FIO', instance.FIO)
        instance.SocialNetwork = validated_data.get('SocialNetwork', instance.SocialNetwork)
        instance.Position = validated_data.get('Position', instance.Position)
        instance.save()
        return instance


#####
class GetPatientListSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    Doctor = DoctorSerializer()
    PatientRecord = PatientRecordSerializer()

class SetPatientListSerializer(serializers.Serializer):
    Doctor = serializers.IntegerField(source='Doctor.id')
    PatientRecord = serializers.IntegerField(source='PatientRecord.id')

    def create(self, validated_data):
        doctor = validated_data.pop('Doctor')
        patientRecord = validated_data.pop('PatientRecord')
        patientList = PatientList.objects.create(Doctor=Doctor.objects.get(id=doctor['id']), PatientRecord=PatientRecord.objects.get(id=patientRecord['id']) ,**validated_data)
        return patientList
    
    def update(self, instance, validated_data):
        instance.Doctor = Doctor.objects.get(id=validated_data.get('Doctor', instance.Doctor)['id'])
        instance.PatientRecord = PatientRecord.objects.get(id=validated_data.get('PatientRecord', instance.PatientRecord)['id'])
        instance.save()
        return instance

#####
class GetTreatmentSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    Record = PatientRecordSerializer()
    Doctor = DoctorSerializer()
    Name = serializers.CharField(max_length=200, required=False)
    Note = serializers.CharField(max_length=5000, required=False)

class SetTreatmentSerializer(serializers.Serializer):
    Record = serializers.IntegerField(source='PatientRecord.id')
    Doctor = serializers.IntegerField(source='Doctor.id')
    Name = serializers.CharField(max_length=200, required=False)
    Note = serializers.CharField(max_length=5000, required=False)

    def create(self, validated_data):
        record = validated_data.pop('PatientRecord')
        doctor = validated_data.pop('Doctor')
        treatment = Treatment.objects.create(Record=PatientRecord.objects.get(id=record['id']), Doctor=Doctor.objects.get(id=doctor['id']),**validated_data)
        return treatment
    
    def update(self, instance, validated_data):
        instance.Record = PatientRecord.objects.get(id=validated_data.get('PatientRecord', instance.Record)['id'])
        instance.Doctor = Doctor.objects.get(id=validated_data.get('Doctor', instance.Doctor)['id'])
        instance.Name = validated_data.get('Name', instance.Name)
        instance.Note = validated_data.get('Note', instance.Note)
        instance.save()
        return instance

#####
class GetEpicrisisSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    Treatment = GetTreatmentSerializer()
    Referral = serializers.CharField(max_length=1000, required=False)
    Therapy = serializers.CharField(max_length=50000, required=False)
    Disability = serializers.CharField(max_length=1000, required=False)
    Hospitalization = serializers.DateField(required=False)
    HospitalDischarge = serializers.DateField(required=False)
    IsOver = serializers.IntegerField(default=0, required=False)

class SetEpicrisisSerializer(serializers.Serializer):
    Treatment = serializers.IntegerField(source='Treatment.id')
    Referral = serializers.CharField(max_length=1000, required=False)
    Therapy = serializers.CharField(max_length=50000, required=False)
    Disability = serializers.CharField(max_length=1000, required=False)
    Hospitalization = serializers.DateField(required=False)
    HospitalDischarge = serializers.DateField(required=False)
    IsOver = serializers.IntegerField(default=0,required=False)

    def create(self, validated_data):
        treatment = validated_data.pop('Treatment')
        epicrisis = Epicrisis.objects.create(Treatment=Treatment.objects.get(id=treatment['id']),**validated_data)
        return epicrisis
    
    def update(self, instance, validated_data):
        instance.Treatment = Treatment.objects.get(id=validated_data.get('Treatment', instance.Treatment)['id'])
        
        instance.Referral = validated_data.get('Referral', instance.Referral)
        instance.Therapy = validated_data.get('Therapy', instance.Therapy)
        instance.Disability = validated_data.get('Disability', instance.Disability)
        instance.Hospitalization = validated_data.get('Hospitalization', instance.Hospitalization)
        instance.HospitalDischarge = validated_data.get('HospitalDischarge', instance.HospitalDischarge)
        instance.IsOver = validated_data.get('IsOver', instance.IsOver)

        instance.save()
        return instance

#####
class GetDiagnosisSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    Treatment = GetTreatmentSerializer()
    Doctor = DoctorSerializer()

    Name = serializers.CharField(max_length=1000, required=False)
    StartDiagnosis = serializers.DateField(required=False)
    Note = serializers.CharField(max_length=50000, required=False)

class SetDiagnosisSerializer(serializers.Serializer):
    Treatment = serializers.IntegerField(source='Treatment.id')
    Doctor = serializers.IntegerField(source='Doctor.id')

    Name = serializers.CharField(max_length=1000, required=False)
    StartDiagnosis = serializers.DateField(required=False)
    Note = serializers.CharField(max_length=50000, required=False)

    def create(self, validated_data):
        treatment = validated_data.pop('Treatment')
        doctor = validated_data.pop('Doctor')
        diagnosis = Diagnosis.objects.create(Treatment=Treatment.objects.get(id=treatment['id']), Doctor=Doctor.objects.get(id=doctor['id']),**validated_data)
        return diagnosis
    
    def update(self, instance, validated_data):
        instance.Treatment = Treatment.objects.get(id=validated_data.get('Treatment', instance.Treatment)['id'])
        instance.Doctor = Doctor.objects.get(id=validated_data.get('Doctor', instance.Doctor)['id'])
        
        instance.Name = validated_data.get('Name', instance.Name)
        instance.StartDiagnosis = validated_data.get('StartDiagnosis', instance.StartDiagnosis)
        instance.Note = validated_data.get('Note', instance.Note)

        instance.save()
        return instance

#####
class DiagnosSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    Name = serializers.CharField(max_length=1000)
    Description = serializers.CharField(max_length=50000, required=False)


    def create(self, validated_data):
        return Diagnos.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.Name = validated_data.get('Name', instance.Name)
        instance.Description = validated_data.get('Description', instance.Description)
        instance.save()
        return instance


#####
class GetFormSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    Diagnosis = GetDiagnosisSerializer()
    Diagnos = DiagnosSerializer()

    Name = serializers.CharField(max_length=1000, required=False)
    DateForm = serializers.DateField(default = "1999-01-01", required=False)
    Note = serializers.CharField(max_length=50000, required=False)
    Conviction = serializers.IntegerField(default = 0, required=False)

class SetFormSerializer(serializers.Serializer):
    Diagnosis = serializers.IntegerField(source='Diagnosis.id')
    Diagnos = serializers.IntegerField(source='Diagnos.id')

    Name = serializers.CharField(max_length=1000, required=False)
    DateForm = serializers.DateField(default = "1999-01-01", required=False)
    Note = serializers.CharField(max_length=50000, required=False)
    Conviction = serializers.IntegerField(default = 0, required=False)

    def create(self, validated_data):
        diagnosis = validated_data.pop('Diagnosis')
        diagnos = validated_data.pop('Diagnos')
        form = Form.objects.create(Diagnosis=Diagnosis.objects.get(id=diagnosis['id']), Diagnos=Diagnos.objects.get(id=diagnos['id']),**validated_data)
        return form
    
    def update(self, instance, validated_data):
        instance.Diagnosis = Diagnosis.objects.get(id=validated_data.get('Diagnosis', instance.Diagnosis)['id'])
        instance.Diagnos = Diagnos.objects.get(id=validated_data.get('Diagnos', instance.Diagnos)['id'])
        
        instance.Name = validated_data.get('Name', instance.Name)
        instance.DateForm = validated_data.get('DateForm', instance.DateForm)
        instance.Note = validated_data.get('Note', instance.Note)
        instance.Conviction = validated_data.get('Conviction', instance.Conviction)

        instance.save()
        return instance

#####
class ConvictionSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    Name = serializers.CharField(max_length=1000)
    Position = serializers.IntegerField()

#####
class FrequencySerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    Name = serializers.CharField(max_length=1000)
    Coef = serializers.FloatField()



#####
class GetRuleSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    Diagnos = DiagnosSerializer()
    Frequency = FrequencySerializer()

class SetRuleSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    Diagnos = serializers.IntegerField(source='Diagnos.id')
    Frequency = serializers.IntegerField(source='Frequency.id')

    def create(self, validated_data):
        diagnos = validated_data.pop('Diagnos')
        frequency = validated_data.pop('Frequency')
        rule = Rule.objects.create(Diagnos=Diagnos.objects.get(id=diagnos['id']), Frequency=Frequency.objects.get(id=frequency['id']) ,**validated_data)
        return rule
    
    def update(self, instance, validated_data):
        instance.Diagnos = Diagnos.objects.get(id=validated_data.get('Diagnos', instance.Diagnos)['id'])
        instance.Frequency = Frequency.objects.get(id=validated_data.get('Frequency', instance.Frequency)['id'])
        instance.save()
        return instance


#####
class SymptomSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    Name = serializers.CharField(max_length=1000)
    Description = serializers.CharField(max_length=50000, required=False)


    def create(self, validated_data):
        return Symptom.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.Name = validated_data.get('Name', instance.Name)
        instance.Description = validated_data.get('Description', instance.Description)
        instance.save()
        return instance


#####
class GetRuleSymptomSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    Rule = GetRuleSerializer()
    Symptom = SymptomSerializer()
    Conviction = ConvictionSerializer()

class SetRuleSymptomSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    Rule = serializers.IntegerField(source='Rule.id')
    Symptom = serializers.IntegerField(source='Symptom.id')
    Conviction = serializers.IntegerField(source='Conviction.id')

    def create(self, validated_data):
        rule = validated_data.pop('Rule')
        symptom = validated_data.pop('Symptom')
        conviction = validated_data.pop('Conviction')
        ruleSymptom = RuleSymptom.objects.create(Rule=Rule.objects.get(id=rule['id']), Symptom=Symptom.objects.get(id=symptom['id']), Conviction=Conviction.objects.get(id=conviction['id'])  ,**validated_data)
        return ruleSymptom
    
    def update(self, instance, validated_data):
        instance.Rule = Rule.objects.get(id=validated_data.get('Rule', instance.Rule)['id'])
        instance.Symptom = Symptom.objects.get(id=validated_data.get('Symptom', instance.Symptom)['id'])
        instance.Conviction = Conviction.objects.get(id=validated_data.get('Conviction', instance.Conviction)['id'])
        
        instance.save()
        return instance

#####
class GetSelectedSymptomsSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    Form = GetFormSerializer()
    Symptom = SymptomSerializer()
    Conviction = ConvictionSerializer()
    Note = serializers.CharField(max_length=50000, required=False)

class SetSelectedSymptomsSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    Form = serializers.IntegerField(source='Form.id')
    Symptom = serializers.IntegerField(source='Symptom.id')
    Conviction = serializers.IntegerField(source='Conviction.id')
    Note = serializers.CharField(max_length=50000, required=False)

    def create(self, validated_data):
        form = validated_data.pop('Form')
        symptom = validated_data.pop('Symptom')
        conviction = validated_data.pop('Conviction')
        selectedSymptoms = SelectedSymptoms.objects.create(Form=Form.objects.get(id=form['id']), Symptom=Symptom.objects.get(id=symptom['id']), Conviction=Conviction.objects.get(id=conviction['id'])  ,**validated_data)
        return selectedSymptoms
    
    def update(self, instance, validated_data):
        instance.Form = Form.objects.get(id=validated_data.get('Form', instance.Form)['id'])
        instance.Symptom = Symptom.objects.get(id=validated_data.get('Symptom', instance.Symptom)['id'])
        instance.Conviction = Conviction.objects.get(id=validated_data.get('Conviction', instance.Conviction)['id'])
        
        instance.Note = validated_data.get('Note', instance.Note)

        instance.save()
        return instance


#####
class GetSelectedSymptomsDoctorSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    Doctor = DoctorSerializer()
    Symptom = SymptomSerializer()
    Conviction = ConvictionSerializer()
    Note = serializers.CharField(max_length=50000, required=False)

class SetSelectedSymptomsDoctorSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    Doctor = serializers.IntegerField(source='Doctor.id')
    Symptom = serializers.IntegerField(source='Symptom.id')
    Conviction = serializers.IntegerField(source='Conviction.id')
    Note = serializers.CharField(max_length=50000, required=False)

    def create(self, validated_data):
        doctor = validated_data.pop('Doctor')
        symptom = validated_data.pop('Symptom')
        conviction = validated_data.pop('Conviction')
        selectedSymptomsDoctor = SelectedSymptomsDoctor.objects.create(Doctor=Doctor.objects.get(id=doctor['id']), Symptom=Symptom.objects.get(id=symptom['id']), Conviction=Conviction.objects.get(id=conviction['id'])  ,**validated_data)
        return selectedSymptomsDoctor
    
    def update(self, instance, validated_data):
        instance.Doctor = Doctor.objects.get(id=validated_data.get('Doctor', instance.Doctor)['id'])
        instance.Symptom = Symptom.objects.get(id=validated_data.get('Symptom', instance.Symptom)['id'])
        instance.Conviction = Conviction.objects.get(id=validated_data.get('Conviction', instance.Conviction)['id'])
        
        instance.Note = validated_data.get('Note', instance.Note)

        instance.save()
        return instance


#####
class GetAnamesisSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    Treatment = GetTreatmentSerializer()
    Diagnos = DiagnosSerializer()
    
class SetAnamesisSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    Treatment = serializers.IntegerField(source='Treatment.id')
    Diagnos = serializers.IntegerField(source='Diagnos.id')

    def create(self, validated_data):
        treatment = validated_data.pop('Treatment')
        diagnos = validated_data.pop('Diagnos')
        anamesis = Anamesis.objects.create(Treatment=Treatment.objects.get(id=treatment['id']), Diagnos=Diagnos.objects.get(id=diagnos['id'])  ,**validated_data)
        return anamesis
    
    def update(self, instance, validated_data):
        instance.Treatment = Treatment.objects.get(id=validated_data.get('Treatment', instance.Treatment)['id'])
        instance.Diagnos = Diagnos.objects.get(id=validated_data.get('Diagnos', instance.Diagnos)['id'])
        
        instance.save()
        return instance