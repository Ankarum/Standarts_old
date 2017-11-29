from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from . import models
from . import forms
import json

# Create your views here.

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

def test4(request):
	'''
	t = models.Standart.objects.filter(title='Программист')[0]
	return render(request, 'Competentions/test4.html', {'standart' : t})
	'''
	t = models.Standart.objects.all()
	return render(request, 'Competentions/test4.html', {'standarts' : t})

def getStandartAjax(request):
	standartTitle = request.POST.get('standartTitle', None)
	t = models.Standart.objects.filter(title=standartTitle)[0]
	return render(request, 'Competentions/leftColumn.html', {'standart' : t})


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








