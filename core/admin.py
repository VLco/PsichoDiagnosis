from django.contrib import admin
# from .models import Diagnos
# from .models import Epicriz
# from .models import Disease
# from .models import Answer
# from .models import Question
# from .models import Ancket
# from .models import Patient
# from .models import User
# from .models import PravilaRule
# from .models import Rule

from .models import Rule
from .models import Frequency
from .models import Conviction
from .models import RuleSymptom
from .models import SelectedSymptomsDoctor

# # Register your models here.
admin.site.register(Rule)
admin.site.register(Frequency)
admin.site.register(Conviction)
admin.site.register(RuleSymptom)
admin.site.register(SelectedSymptomsDoctor)
# admin.site.register(Answer)
# admin.site.register(Ancket)
# admin.site.register(Patient)
# admin.site.register(User)
# admin.site.register(PravilaRule)
# admin.site.register(Rule)