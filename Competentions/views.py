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

# Функции для отображения страниц авторизации/регистрации/выхода
#***************************************************************
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
#***************************************************************



#Отображение страниц
#***************************************************************
# Отображение страницы профессиональных компетенций
def professionalStandartsView(request):
  standarts = models.Standart.objects.all()
  return render(request, 'Competentions/professionalStandarts.html', {'standarts' : standarts})

# Отображение страницы образовательных стандартов
def educationalStandartsView(request):
  educationalStandarts = models.EducationalStandart.objects.all()
  return render(request, 'Competentions/educationalStandarts.html', {'educationalStandarts' : educationalStandarts})

def mainPage(request):
  return render(request, 'main/mainPage.html')
#***************************************************************



#Отображение наборов компетенций
#***************************************************************
# Отображение профессионального стандарта
def getProfessionalStandartAjax(request):
  standartTitle = request.POST.get('standartTitle', None)
  t = models.Standart.objects.filter(title=standartTitle)[0]
  return render(request, 'Competentions/professionalStandart.html', {'standart' : t})

# Отображение образовательного стандарта
def getEducationalStandartAjax(request):
  educationalStandartTitle = request.POST.get('educationalStandartTitle', None)
  educationalStandart = models.EducationalStandart.objects.filter(title=educationalStandartTitle)[0]

  # Отображение групп, к которым принадлежат компетенции образовательного стандарта
  comps = educationalStandart.educationalStandartCompetentions.all()
  groups = set()
  for comp in comps:
    groups.add(comp.group)

  return render(request, 'Competentions/educationalStandartColumn.html', {'educationalStandart' : educationalStandart, 'educationalStandartGroups' : groups})

# Функция для отображения профессионального стандарта в упрощенном виде
# (только компетенции профессионального стандарта)
def getSimpleViewProfessionalStandartAjax(request):

  standartTitle = request.POST.get('standartTitle', None)
  standart = models.Standart.objects.filter(title=standartTitle)[0]

  # Множества, в которые собираются все компетенции по профессиональному стандарту
  # Множества использованы для исключения повторов
  allCompetentions = {
    'Трудовые действия' : set(),
    'Необходимые умения' : set(),
    'Необходимые знания' : set()
  }

  # Цикл по всем рабочим функциям внутри профессионального стандарты,
  # в котором компетенции добавляются в соответствующие множества
  commonWorkFunctions = standart.commonworkfunction_set.all()
  for commonWorkFunction in commonWorkFunctions:

    workFunctions = commonWorkFunction.workfunction_set.all()
    for workFunction in workFunctions:

      for workAction in workFunction.workActions.all():
        allCompetentions['Трудовые действия'].add(workAction.title)

      for neccessarySkill in workFunction.neccessarySkills.all():
        allCompetentions['Необходимые умения'].add(neccessarySkill.title)

      for neccessaryKnowledge in workFunction.neccessaryKnowledges.all():
        allCompetentions['Необходимые знания'].add(neccessaryKnowledge.title)
  return render(request, 'Competentions/simpleViewStandart.html', {'allCompetentions' : allCompetentions})

# Отобразить набор пользовательских компетенций
def getCustomCompetentionListAjax(request):
  customCompetentionListTitle = request.POST.get('customCompetentionListTitle', None)
  t = models.CustomCompetentionList.objects.filter(title=customCompetentionListTitle)[0]
  return render(request, 'Competentions/customCompetentionListTemplate.html', {'customCompetentionList' : t})
#***************************************************************



#Добавление и удаление набора компетенций
#***************************************************************
# Функция для создания нового пользовательского списка компетенций
def addCustomCompetentionListAjax(request):
  listTitle = request.POST.get('newListTitle', None)
  newCustomCompetentionList = models.CustomCompetentionList.objects.create(user=request.user, title=listTitle)
  return HttpResponse("added")

# Функция для удаления пользовательского списка компетенций по имени
def deleteCustomCompetentionListAjax(request):
  listTitle = request.POST.get('listTitle', None)
  models.CustomCompetentionList.objects.filter(user=request.user, title=listTitle).delete()
  return HttpResponse("deleted")

# Функция для добавления компетенции к пользовательскому списку компетенций
def addCompetentionToCustomCompetentionList(request):
  # Название пользовательского набора компетенций
  customCompetentionListTitle = request.POST.get('customCompetentionListTitle', None)
  competentionType = request.POST.get('competentionType', None) # Тип компетенции
  competentionTitle = request.POST.get('competentionTitle', None) # Название компетенции

  currentCompetentionList = models.CustomCompetentionList.objects.filter(title=customCompetentionListTitle)[0]

  # Добавление компетенции в соответствующий список пользовательского набора
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
#***************************************************************




# Добавление стандарта из Json файла
#********************************************************************************
def addStandart(request):
	if request.method == 'POST':
		form = forms.StandartImportForm(request.POST, request.FILES)
		if form.is_valid():
			files = request.FILES.getlist('standartJSON')
			i = 1
			for file in files:
				print('Обработка файла: ' + str(i) + ' из ' + str(len(files)))
				JsonToDatabase(file)
			print('Обработка файлов завершена')
			return HttpResponseRedirect('')
	else:
		form = forms.StandartImportForm()

	return render(request, 'Competentions/getStandart.html', {'form' : form})

# Функция для добавления профессионального стандарта в формате JSON в базу данных
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

#********************************************************************************






