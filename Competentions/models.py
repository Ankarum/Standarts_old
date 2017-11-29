from django.db import models

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