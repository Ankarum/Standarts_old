from django.contrib import admin
from .models import Standart, CommonWorkFunction, PositionTitle, EducationRequirement
from .models import WorkRequirement, AccessRequirement, WorkFunction
from .models import WorkAction, NeccessarySkill, NeccessaryKnowledge

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

class StandartImportAdmin(admin.ModelAdmin):
	form = StandartImportForm

#admin.site.register(StandartImportAdmin)
