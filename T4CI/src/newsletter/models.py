from django.db import models

# Create your models here.

# Users
class SignUp(models.Model):
	email = models.EmailField()
	full_name = models.CharField(max_length=120, blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self): #Python 3.3 is __str__
		return self.email

# Dreams
class DreamManager(models.Manager):
	def create_dream(self, name, category, theme, description):
		dream = self.create(name=name, category=category, theme=theme, description=description) 
		return dream

class Dream(models.Model):
	name = models.CharField(max_length=120, blank=True, null=True)
	category = models.CharField(max_length=120, blank=True, null=True)
	theme = models.CharField(max_length=120, blank=True, null=True)
	description = models.CharField(max_length=300, blank=True, null=True)

	objects = DreamManager()

	def __unicode__(self):
		return self.name

# Dreams - Team
class DreamTeamManager(models.Manager):
	def add_to_dream_team(self, name, email, personid, dreamid, position):
		person = self.create(name=name, personid=personid, dreamid=dreamid, position=position) 
		return person

class TeamMember(models.Model):
	TEAMLEADER = 'TL'
	TEAMMEMBER = 'TM'
	TEAM=(
    	(TEAMLEADER, 'Team Leader'),
    	(TEAMMEMBER, "Team Member"),
    )
	#name = models.CharField(max_length=120, blank=True, null=True)
	personid = models.PositiveIntegerField(default=0, blank=True, null=True)
	#person = models.ForeignKey(SignUp, blank=True, null=True)
	dreamid = models.PositiveIntegerField(default=0, blank=True, null=True)
	#dream = models.ForeignKey(Dream, blank=True, null=True)
	position = models.CharField(max_length=2, choices=TEAM, default=TEAMMEMBER)

	objects = DreamTeamManager()

	def __unicode__(self):
		return self.name

# Tasks
class Task(models.Model):
	taskname = models.CharField(max_length=120, blank=True, null=True)
	taskstatus = models.CharField(max_length=120, blank=True, null=True)
	def __unicode__(self):
		return self