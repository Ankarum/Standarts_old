from django.contrib import admin
from .models import Standart, CommonWorkFunction, PositionTitle, EducationRequirement
from .models import WorkRequirement, AccessRequirement, WorkFunction
from .models import WorkAction, NeccessarySkill, NeccessaryKnowledge, CustomCompetentionList

from .models import EducationalStandartCompetentionGroup, EducationalStandartCompetention

from .models import CustomCompetention, EducationalStandart

from .forms import StandartImportForm

# Register your models here.
admin.site.register(Standart)
admin.site.register(CommonWorkFunction)
admin.site.register(PositionTitle)
admin.site.register(EducationRequirement)
admin.site.register(WorkRequirement)
admin.site.register(AccessRequirement)
admin.site.register(WorkFunction)
admin.site.register(WorkAction)
admin.site.register(NeccessarySkill)
admin.site.register(NeccessaryKnowledge)
admin.site.register(CustomCompetentionList)
admin.site.register(CustomCompetention)
admin.site.register(EducationalStandart)
admin.site.register(EducationalStandartCompetentionGroup)
admin.site.register(EducationalStandartCompetention)

class StandartImportAdmin(admin.ModelAdmin):
	form = StandartImportForm

#admin.site.register(StandartImportAdmin)
