from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Standart(models.Model):
	title = models.CharField(max_length=100)

	def __str__(self):
		return self.title

class PositionTitle(models.Model):
	title = models.CharField(max_length=100)

	def __str__(self):
		return self.title

class EducationRequirement(models.Model):
	title = models.CharField(max_length=100)

	def __str__(self):
		return self.title

class WorkRequirement(models.Model):
	title = models.CharField(max_length=100)

	def __str__(self):
		return self.title

class AccessRequirement(models.Model):
	title = models.CharField(max_length=100)

	def __str__(self):
		return self.title

class CommonWorkFunction(models.Model):
	title = models.CharField(max_length=100)
	standart = models.ForeignKey(Standart)
	qualificationLevel = models.IntegerField()

	positionTitles = models.ManyToManyField(PositionTitle)
	educationRequirements = models.ManyToManyField(EducationRequirement)
	workRequirements = models.ManyToManyField(WorkRequirement)
	accessRequirements = models.ManyToManyField(AccessRequirement)

	def __str__(self):
		return self.title

class WorkAction(models.Model):
	title = models.CharField(max_length=200)

	def __str__(self):
		return self.title
class NeccessarySkill(models.Model):
	title = models.CharField(max_length=200)

	def __str__(self):
		return self.title

class NeccessaryKnowledge(models.Model):
	title = models.CharField(max_length=200)

	def __str__(self):
		return self.title

class WorkFunction(models.Model):
	title = models.CharField(max_length=100)
	commonWorkFunction = models.ForeignKey(CommonWorkFunction, null=True)
	workActions = models.ManyToManyField(WorkAction)
	neccessarySkills = models.ManyToManyField(NeccessarySkill)
	neccessaryKnowledges = models.ManyToManyField(NeccessaryKnowledge)

	def __str__(self):
		return self.title

class EducationalStandartCompetentionGroup(models.Model):
	title = models.CharField(max_length=200)

	def __str__(self):
		return self.title

class EducationalStandartCompetention(models.Model):
	title = models.CharField(max_length=800)

	group = models.ForeignKey(EducationalStandartCompetentionGroup)

	def __str__(self):
		return self.title

class EducationalStandart(models.Model):
	title = models.CharField(max_length=200)

	number = models.CharField(max_length=10, null=True)

	education_type = models.CharField(max_length=40, null=True) 

	educationalStandartCompetentions = models.ManyToManyField(EducationalStandartCompetention)

	def __str__(self):
		return self.title

class CustomCompetention(models.Model):
	title = models.CharField(max_length=300)

	user = models.ForeignKey(User)

	def __str__(self):
		return self.title

class CustomCompetentionList(models.Model):
	title = models.CharField(max_length=100)
	user = models.ForeignKey(User)
	workActions = models.ManyToManyField(WorkAction, blank=True)
	neccessarySkills = models.ManyToManyField(NeccessarySkill, blank=True)
	neccessaryKnowledges = models.ManyToManyField(NeccessaryKnowledge, blank=True)

	generalProfessionalCompetentions = models.ManyToManyField(EducationalStandartCompetention, blank=True)

	customCopetentions = models.ManyToManyField(CustomCompetention, blank=True)

	def __str__(self):
		return self.title

class EducationalProgram(models.Model):
	title = models.CharField(max_length=100)
	user = models.ForeignKey(User)

	competentionLists = models.ManyToManyField(CustomCompetentionList, blank=True)