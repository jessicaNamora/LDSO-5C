from django.db import models
import datetime
from django.conf import settings

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from registration.signals import user_registered

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
	def createDream(self,name,description):
		dream = self.create(name=name, description=description)
		return dream

class Dream(models.Model):
	name = models.CharField(max_length=120, blank=True, null=True)
	category = models.CharField(max_length=120, blank=True, null=True)
	theme = models.CharField(max_length=120, blank=True, null=True)
	description = models.CharField(max_length=300, blank=True, null=True)
	dateCreated = models.DateTimeField(default=datetime.date.today, blank=True)

	objects = DreamManager()

	def __unicode__(self):
		return self.name

# Dreams - Team
class DreamTeamManager(models.Manager):
	def addteammember(self, personid, dreamid, position):
		member = self.create(personid=personid,dreamid=dreamid,position=position)
		return member
	
	def becomeActive(self, personid, dreamid):
		raw = TeamMember.objects.get(personid=personid, dreamid=dreamid)
		raw.active = 1
		raw.save()
		return raw

	def changeRole(self, id, role_id):
		raw = TeamMember.objects.get(id=id)
		raw.position = role_id
		raw.save()
		return raw

class TeamMember(models.Model):
	INACTIVE = 0
	TEAMLEADER = 'TL'
	TEAMMEMBER = 'TM'
	TEAMCOMMUNICATOR = 'TC'
	TEAM=(
    	(TEAMLEADER, 'Team Leader'),
    	(TEAMMEMBER, "Team Member"),
    	(TEAMCOMMUNICATOR, "Team Communicator"),
    )
	personid = models.PositiveIntegerField(default=0, blank=True, null=True)
	dreamid = models.PositiveIntegerField(default=0, blank=True, null=True)
	position = models.CharField(max_length=2, choices=TEAM, default=TEAMMEMBER)

	active = models.BooleanField(default=INACTIVE)

	objects = DreamTeamManager()

	def __unicode__(self):
		return self.name

# Messages
class MessagesManager(models.Manager):
	def seenMessage(self, id):
		raw = Messages.objects.get(id=id)
		raw.seen = 1
		raw.save()
		return raw

	def addInvite(self, messageType,dreamid):
		message = self.create(messageType=messageType,dreamid=dreamid)
		return message
	def addAnswer(self, messageType,dreamid, extra):
		message = self.create(messageType=messageType,dreamid=dreamid, extra=extra)
		return message
	def addmessage(self, messageType, receiver, dreamid,extra):
		message = self.create(messageType=messageType,receiver=receiver,dreamid=dreamid,extra=extra)
		return message

class Messages(models.Model):
	INVITATION = 0
	DECLINEDINVITE = 1
	ACCEPTEDINVITE = 2
	ROLE = 3
	GENERAL = 4

	NOTSEEN=0
	
	OPTIONS=((INVITATION,'Invitation'),(DECLINEDINVITE, 'Declined'),(ACCEPTEDINVITE,'Accepted'), (ROLE,'Role Change'))

	messageType = models.PositiveIntegerField(default=4, choices=OPTIONS)
	receiver = models.PositiveIntegerField(blank=True, null=True)
	dreamid = models.PositiveIntegerField(default=0, blank=True, null=True)
	extra = models.CharField(max_length=150, blank=True, null=True)
	seen =  models.BooleanField(default=NOTSEEN)
	
	objects = MessagesManager()

	def __unicode__(self):
		return self
		
# Gifts
class GiftManager(models.Manager):
	def addgift(self, userid, giftname):
		gift = self.create(user=userid,gift=giftname)
		return gift

class Gift(models.Model):
	user = models.PositiveIntegerField(default=0, null=True, blank=True)
	gift = models.CharField(max_length=30, null=True, blank=True)

	objects = GiftManager()

	def __unicode__(self):
		return self
		
# Tasks
class TaskManager(models.Manager):
	def addtask(self, taskname, taskstatus, dreamid, responsibleid):
		task = self.create(taskname=taskname,taskstatus=taskstatus,dreamid=dreamid, responsibleid=responsibleid)
		return task

	def edittask(self,taskname,taskstatus,task_id,responsibleid):
		task = Task.objects.get(id=task_id)
		task.taskname = taskname
		task.taskstatus = taskstatus
		task.responsibleid = responsibleid
		task.save()
		return task

	def deletetask(self, task_id):
		task = Task.objects.get(id=task_id)
		task.delete()
		return

	def finishtask(self, task_id):
		now = datetime.datetime.now()
		task = Task.objects.get(id=task_id)
		if task.taskstatus == 'current':
			task.taskstatus = 'done'
			task.dateFinished = now
			task.save()
		return task

	def starttask(self, task_id):
		task = Task.objects.get(id=task_id)
		if task.taskstatus == 'todo':
			task.taskstatus = 'current'
			task.save()
		return task

	def gettask(self, task_id):
		task = Task.objects.get(id=task_id)
		return task

class Task(models.Model):
	taskname = models.CharField(max_length=120, blank=True, null=True)
	taskstatus = models.CharField(max_length=120, blank=True, null=True)
	dreamid = models.PositiveIntegerField(default=0, null=True, blank=True)
	responsibleid = models.PositiveIntegerField(default=0, null=True, blank=True)
	dateCreated = models.DateTimeField(default=datetime.date.today, blank=True)
	dateFinished = models.DateTimeField(default=datetime.date.today, blank=True)

	objects = TaskManager()

	def __unicode__(self):
		return self

class UserProfile(models.Model):
#   user = models.ForeignKey(User, unique=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    locality = models.CharField(max_length=30, null=True, blank=True)
    phone_number = models.PositiveIntegerField(null=True, blank=True)
    description = models.CharField(max_length=150, null=True, blank=True)
    avatar = models.FileField(upload_to="profile_pic", null=True, blank=True) 



def assure_user_profile_exists(pk):
        """
        This might not be working. To be judged later
        """
        user = User.objects.get(pk=pk)
        try:
            # fails if it doesn't exist
            userprofile = user.userprofile
        except UserProfile.DoesNotExist, e:
            userprofile = UserProfile(user=user)
            userprofile.save()
        return

def create_user_profile(**kwargs):
        UserProfile.objects.get_or_create(user=kwargs['user'])

user_registered.connect(create_user_profile)

