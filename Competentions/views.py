from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from . import models
from . import forms
import json

from django.views.generic.base import View
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.

class RegisterFormView(FormView):
	form_class = UserCreationForm

	success_url = "/"

	template_name = "main/register.html"

	def form_valid(self, form):
		form.save()

		return super(RegisterFormView, self).form_valid(form)

class LoginFormView(FormView):
	print('login view')
	form_class = AuthenticationForm

	template_name = "main/login.html"

	success_url = "/"

	def form_valid(self, form):
		self.user = form.get_user()

		login(self.request, self.user)
		return super(LoginFormView, self).form_valid(form)

class LogoutView(View):
	def get(self, request):
		logout(request)
		return HttpResponseRedirect("/")

def addCustomCompetentionListAjax(request):
	customCompetentionListTitle = request.POST.get('customCompetentionListTitle', None)
	newCustomCompetentionList = models.CustomCompetentionList.objects.create(user=request.user, title=customCompetentionListTitle)
	return HttpResponse("added")

def addCustomCompetentionList(request):
	listTitle = request.POST.get('newListTitle', None)
	newCustomCompetentionList = models.CustomCompetentionList.objects.create(user=request.user, title=listTitle)
	return HttpResponse("added")

def deleteCustomCompetentionListAjax(request):
	listTitle = request.POST.get('listTitle', None)
	models.CustomCompetentionList.objects.filter(user=request.user, title=listTitle).delete()
	return HttpResponse("deleted")

def addCompetentionToCustomCompetentionList(request):
	customCompetentionListTitle = request.POST.get('customCompetentionListTitle', None)
	competentionType = request.POST.get('competentionType', None)
	competentionTitle = request.POST.get('competentionTitle', None)

	currentCompetentionList = models.CustomCompetentionList.objects.filter(title=customCompetentionListTitle)[0]

	comp = ""
	if competentionType == "WorkAction":
		comp = models.WorkAction.objects.filter(title=competentionTitle)[0]
		currentCompetentionList.workActions.add(comp)
	elif competentionType == "NeccessarySkill":
		comp = models.NeccessarySkill.objects.filter(title=competentionTitle)[0]
		currentCompetentionList.neccessarySkills.add(comp)
	elif competentionType == "NeccessaryKnowledge":
		comp = models.NeccessaryKnowledge.objects.filter(title=competentionTitle)[0]
		currentCompetentionList.neccessaryKnowledges.add(comp)

	return HttpResponse("added")




def updateCustomCompetentionListAjax(request):
	customCompetentionTitle = request.POST.get('customCompetentionTitle', None)
	workActions = request.POST.get('workActions', None)
	neccessarySkills = request.POST.get('neccessarySkills', None)
	neccessaryKnowledge = request.POST.get('neccessaryKnowledge', None)
	print(customCompetentionTitle)
	print(workActions)
	print(neccessarySkills)
	print(neccessaryKnowledge)
	return "updated"

def test(request):
	print('#'*80)
	t = models.CommonWorkFunction.objects.filter(title='Разработка требований и проектирование программного обеспечения')[0]
	#print(models.WorkFunction.objects['Формализация и алгоритмизация поставленных задач'])
	print(t.workfunction_set.all())
	print('#'*80)
	return render(request, 'Competentions/test.html')

def test2(request):
	t = models.Standart.objects.filter(title='Программист')[0]
	return render(request, 'Competentions/test2.html', {'standart' : t})

def test3(request):
	allCompetentions = {
		'Трудовые функции' : set(),
		'Необходимые умения' : set(),
		'Необходимые знания' : set()
	}

	standart = models.Standart.objects.filter(title='Программист')[0]

	commonWorkFunctions = standart.commonworkfunction_set.all()
	for commonWorkFunction in commonWorkFunctions:
		#commonWorkFunction = commonWorkFunctions[commonWorkFunctionName]

		workFunctions = commonWorkFunction.workfunction_set.all()
		for workFunction in workFunctions:
			#workFunction = workFunctions[workFunctionName]

			for workAction in workFunction.workActions.all():
				allCompetentions['Трудовые функции'].add(workAction.title)

			for neccessarySkill in workFunction.neccessarySkills.all():
				allCompetentions['Необходимые умения'].add(neccessarySkill.title)

			for neccessaryKnowledge in workFunction.neccessaryKnowledges.all():
				allCompetentions['Необходимые знания'].add(neccessaryKnowledge.title)
				'''
	for comp in allCompetentions:
		print()
		print('#'*80)
		print(allCompetentions[comp])
		'''
	return render(request, 'Competentions/test3.html', {'allCompetentions' : allCompetentions})

def userCompetentions(request):
	standarts = models.Standart.objects.all()
	return render(request, 'Competentions/userCompetentions.html', {'standarts' : standarts})

def educationalStandartsView(request):
	educationalStandarts = models.EducationalStandart.objects.all()
	return render(request, 'Competentions/educationalStandarts.html', {'educationalStandarts' : educationalStandarts})

def mainPage(request):
	return render(request, 'main/mainPage.html')

def test5(request):
	return render(request, 'Competentions/test5.html')

def getStandartAjax(request):
	standartTitle = request.POST.get('standartTitle', None)
	t = models.Standart.objects.filter(title=standartTitle)[0]
	return render(request, 'Competentions/leftColumn.html', {'standart' : t})

def getEducationalStandartAjax(request):
	educationalStandartTitle = request.POST.get('educationalStandartTitle', None)
	educationalStandart = models.EducationalStandart.objects.filter(title=educationalStandartTitle)[0]

	comps = educationalStandart.educationalStandartCompetentions.all()
	groups = set()
	for comp in comps:
		groups.add(comp.group)

	return render(request, 'Competentions/educationalStandartColumn.html', {'educationalStandart' : educationalStandart, 'educationalStandartGroups' : groups})

def getSimpleViewStandartAjax(request):

	standartTitle = request.POST.get('standartTitle', None)
	standart = models.Standart.objects.filter(title=standartTitle)[0]

	allCompetentions = {
		'Трудовые действия' : set(),
		'Необходимые умения' : set(),
		'Необходимые знания' : set()
	}

	commonWorkFunctions = standart.commonworkfunction_set.all()
	for commonWorkFunction in commonWorkFunctions:
		#commonWorkFunction = commonWorkFunctions[commonWorkFunctionName]

		workFunctions = commonWorkFunction.workfunction_set.all()
		for workFunction in workFunctions:
			#workFunction = workFunctions[workFunctionName]

			for workAction in workFunction.workActions.all():
				allCompetentions['Трудовые действия'].add(workAction.title)

			for neccessarySkill in workFunction.neccessarySkills.all():
				allCompetentions['Необходимые умения'].add(neccessarySkill.title)

			for neccessaryKnowledge in workFunction.neccessaryKnowledges.all():
				allCompetentions['Необходимые знания'].add(neccessaryKnowledge.title)
				'''
	for comp in allCompetentions:
		print()
		print('#'*80)
		print(allCompetentions[comp])
		'''
	return render(request, 'Competentions/simpleViewStandart.html', {'allCompetentions' : allCompetentions})

def getCustomCompetentionListAjax(request):
	customCompetentionListTitle = request.POST.get('customCompetentionListTitle', None)
	t = models.CustomCompetentionList.objects.filter(title=customCompetentionListTitle)[0]
	return render(request, 'Competentions/customCompetentionListTemplate.html', {'customCompetentionList' : t})


def addStandart(request):
	if request.method == 'POST':
		form = forms.StandartImportForm(request.POST, request.FILES)
		if form.is_valid():
			#print(request.FILES.getlist('standartJSON'))
			files = request.FILES.getlist('standartJSON')
			i = 1
			for file in files:
				print('Обработка файла: ' + str(i) + ' из ' + str(len(files)))
				JsonToDatabase(file)
			print('Обработка файлов завершена')
			#JsonToDatabase(request.FILES['standartJSON'])
			return HttpResponseRedirect('')
	else:
		form = forms.StandartImportForm()

	return render(request, 'Competentions/getStandart.html', {'form' : form})

def JsonToDatabase(f):
	raw = f.read().decode('utf8')
	standart = json.loads(raw)

	standartModel = models.Standart(title=standart['Наименование'])
	standartModel.save()

	commonWorkFunctions = standart['Обобщенные трудовые функции']
	for commonWorkFunctionName in commonWorkFunctions:
		commonWorkFunction = commonWorkFunctions[commonWorkFunctionName]
		qualificationLevel = int(commonWorkFunction['Уровень квалификации'])

		commonWorkFunctionModel = models.CommonWorkFunction(title=commonWorkFunctionName, standart=standartModel, qualificationLevel=qualificationLevel)
		commonWorkFunctionModel.save()

		for positionTitle in commonWorkFunction['Возможные наименования должностей']:
			positionTitleModel, created = models.PositionTitle.objects.get_or_create(title=positionTitle)
			positionTitleModel.save()
			commonWorkFunctionModel.positionTitles.add(positionTitleModel)

		for educationRequirement in commonWorkFunction['Требования к образованию и обучению']:
			if str(educationRequirement) not in "-–":
				educationRequirementModel, created = models.EducationRequirement.objects.get_or_create(title=educationRequirement)
				educationRequirementModel.save()
				commonWorkFunctionModel.educationRequirements.add(educationRequirementModel)


		for workRequirement in commonWorkFunction['Требования к опыту практической работы']:
			if str(workRequirement) not in "-–":
				workRequirementModel, created = models.WorkRequirement.objects.get_or_create(title=workRequirement)
				workRequirementModel.save()
				commonWorkFunctionModel.workRequirements.add(workRequirementModel)

		for accessRequirement in commonWorkFunction['Особые условия допуска к работе']:
			if str(accessRequirement) not in "-–":
				accessRequirementModel, created = models.AccessRequirement.objects.get_or_create(title=accessRequirement)
				accessRequirementModel.save()
				commonWorkFunctionModel.accessRequirements.add(accessRequirementModel)

		workFunctions = commonWorkFunction['Трудовые функции']
		for workFunctionName in workFunctions:
			workFunction = workFunctions[workFunctionName]

			workFunctionModel = models.WorkFunction(title=workFunctionName, commonWorkFunction=commonWorkFunctionModel)
			workFunctionModel.save()

			for workAction in workFunction['Трудовые действия']:
				workActionModel, created = models.WorkAction.objects.get_or_create(title=workAction)
				workActionModel.save()
				workFunctionModel.workActions.add(workActionModel)

			for neccessarySkill in workFunction['Необходимые умения']:
				neccessarySkillModel, created = models.NeccessarySkill.objects.get_or_create(title=neccessarySkill)
				neccessarySkillModel.save()
				workFunctionModel.neccessarySkills.add(neccessarySkillModel)

			for neccessaryKnowledge in workFunction['Необходимые знания']:
				neccessaryKnowledgeModel, created = models.NeccessaryKnowledge.objects.get_or_create(title=neccessaryKnowledge)
				neccessaryKnowledgeModel.save()
				workFunctionModel.neccessaryKnowledges.add(neccessaryKnowledgeModel)








