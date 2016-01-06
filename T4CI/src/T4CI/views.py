from django.shortcuts import render
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
import json
import sys

from app.models import Dream
from app.models import Task
from app.models import TeamMember
from app.models import SignUp
from app.models import Messages
from app.models import Gift


def about(request):
	return render(request, "about.html", {})

def dream(request, dream_id):
	if request.user.is_authenticated():
		if (request.user.is_superuser == True):
		 auth = Task.objects.raw("SELECT * FROM app_teammember WHERE app_teammember.dreamid = %s", [dream_id])

		 if(len(list(auth)) < 1):
		 	return redirect('/mydreams')

	 	 projects = Dream.objects.filter(id=dream_id)
		 tasks = Task.objects.raw("SELECT * FROM app_task WHERE app_task.dreamid = %s", [dream_id])
		 members = TeamMember.objects.raw("SELECT * FROM app_teammember, auth_user, app_userprofile WHERE app_teammember.personid = app_userprofile.user_id AND dreamid = %s", [dream_id])

		 if(len(list(tasks)) < 1):
			tasks = None

		 if(projects):
			project = projects[0]
		 else:
			project = None
		else:
		 auth = Task.objects.raw("SELECT * FROM app_teammember WHERE app_teammember.dreamid = %s AND app_teammember.personid = %s", [dream_id, request.user.id])

		 if(len(list(auth)) < 1):
		 	return redirect('/mydreams')

		 projects = Dream.objects.filter(id=dream_id)
		 tasks = Task.objects.raw("SELECT * FROM app_task, app_teammember WHERE app_task.dreamid = app_teammember.dreamid AND app_task.dreamid = %s AND app_teammember.personid = %s", [dream_id, request.user.id])
		 members = TeamMember.objects.raw("SELECT * FROM app_teammember, auth_user, app_userprofile WHERE app_teammember.personid = app_userprofile.user_id AND app_teammember.personid = auth_user.id AND dreamid = %s", [dream_id])

		 if(len(list(tasks)) < 1):
			tasks = None

		 if(projects):
			project = projects[0]
		 else:
			project = None

		context = {
			'auth' : auth[0],
			'dream' : project,
			'tasks' : tasks,
			'team' : members
		}
		return render(request, "dream.html", context)
	else:
		return redirect('/')

def is_int(var):
    try:
        int(var)
        return True
    except ValueError:
        return False

def gettask(request, dream_id):
	auth = TeamMember.objects.raw("SELECT * FROM app_teammember WHERE app_teammember.dreamid = %s AND app_teammember.personid = %s", [dream_id, request.user.id])

	if(len(list(auth)) < 1):
		return HttpResponse('Error0')

	task_id = request.POST.get('edittaskid', 0)
	success = True

	if task_id == None or task_id == '' or task_id == 0 or not is_int(task_id):
		return HttpResponse('Error1')
	else:
		task = Task.objects.gettask(task_id=task_id)
		if task == None:
			return HttpResponse('Error2')

	if success:
		data = json.dumps({
        	'taskname': task.taskname,
        	'taskstatus': task.taskstatus,
        	'responsibleid': task.responsibleid,
    	})
		return HttpResponse(data, content_type='application/json')
	else:
		return HttpResponse('Error')

def addtask(request, dream_id):
	auth = TeamMember.objects.raw("SELECT * FROM app_teammember WHERE app_teammember.dreamid = %s AND app_teammember.personid = %s", [dream_id, request.user.id])

	if(len(list(auth)) < 1):
		return redirect('/mydreams')

	taskname = request.POST['taskName']
	taskstatus = request.POST['taskStatus']
	responsibleid = request.POST.get('responsibleId',0)
	success = True

	if taskname == None or taskname == '':
		success = False
		messages.error(request, 'Dream description was left blank.')

	if taskstatus == None or taskstatus == '' or not taskstatus in ['done', 'current', 'todo']:
		success = False
		messages.error(request, 'Task status has an invalid value.')

	if not is_int(responsibleid):
		success = False
		messages.error(request, 'The member assigned does not exist.')
	elif not responsibleid == "0":
		responsible = TeamMember.objects.raw("SELECT * FROM app_teammember, auth_user, app_userprofile WHERE app_teammember.personid = app_userprofile.user_id AND app_teammember.personid = auth_user.id AND dreamid = %s AND app_teammember.personid = %s", [dream_id, responsibleid])
		if(len(list(responsible)) < 1):
			success = False
			messages.error(request, 'The member assigned does not exist.')

	if success:
		task = Task.objects.addtask(taskname=taskname,taskstatus=taskstatus,dreamid=dream_id,responsibleid=responsibleid)

	return HttpResponseRedirect(reverse('dream', args=(dream_id,)))

def edittask(request, dream_id):
	auth = TeamMember.objects.raw("SELECT * FROM app_teammember WHERE app_teammember.dreamid = %s AND app_teammember.personid = %s", [dream_id, request.user.id])

	if(len(list(auth)) < 1):
		return redirect('/mydreams')

	taskname = request.POST['taskNameNew']
	taskstatus = request.POST['taskStatusNew']
	task_id = request.POST['edittaskid']
	responsibleid = request.POST.get('responsibleIdNew', 0)

	success = True

	if taskname == None or taskname == '':
		success = False
		messages.error(request, 'Task name was left blank.')

	if taskstatus == None or taskstatus == '' or not taskstatus in ['done', 'current', 'todo']:
		success = False
		messages.error(request, 'Task status has an invalid value.')

	if task_id == None or task_id == '' or task_id == 0 or not is_int(task_id):
		success = False
		messages.error(request, 'The task does not exist.')

	if not is_int(responsibleid):
		success = False
		messages.error(request, 'The member assigned does not exist.')
	elif not responsibleid == "0":
		responsible = TeamMember.objects.raw("SELECT * FROM app_teammember, auth_user, app_userprofile WHERE app_teammember.personid = app_userprofile.user_id AND app_teammember.personid = auth_user.id AND dreamid = %s AND app_teammember.personid = %s", [dream_id, responsibleid])
		if(len(list(responsible)) < 1):
			success = False
			messages.error(request, 'The member assigned does not exist.')

	if success:
		Task.objects.edittask(taskname=taskname,taskstatus=taskstatus,task_id=task_id, responsibleid=responsibleid)

	return HttpResponseRedirect(reverse('dream', args=(dream_id,)))


def deletetask(request, dream_id):
	auth = TeamMember.objects.raw("SELECT * FROM app_teammember WHERE app_teammember.dreamid = %s AND app_teammember.personid = %s", [dream_id, request.user.id])

	if(len(list(auth)) < 1):
		return redirect('/mydreams')

	task_id = request.POST['deletetaskid']
	Task.objects.deletetask(task_id=task_id)

	return HttpResponseRedirect(reverse('dream', args=(dream_id,)))

def finishtask(request, dream_id):
	auth = TeamMember.objects.raw("SELECT * FROM app_teammember WHERE app_teammember.dreamid = %s AND app_teammember.personid = %s", [dream_id, request.user.id])

	if(len(list(auth)) < 1):
		return redirect('/mydreams')

	task_id = request.POST['finishtaskid']
	responsible = Task.objects.filter(id=task_id).values('responsibleid')
	Task.objects.finishtask(task_id=task_id)
	if(responsible[0]['responsibleid'] == 0):
		Task.objects.defineresponsible(task_id=task_id, personid=request.user.id)

	return HttpResponseRedirect(reverse('dream', args=(dream_id,)))

def starttask(request, dream_id):
	auth = TeamMember.objects.raw("SELECT * FROM app_teammember WHERE app_teammember.dreamid = %s AND app_teammember.personid = %s", [dream_id, request.user.id])

	if(len(list(auth)) < 1):
		return redirect('/mydreams')

	task_id = request.POST['starttaskid']
	responsible = Task.objects.filter(id=task_id).values('responsibleid')
	Task.objects.starttask(task_id=task_id)
	if(responsible[0]['responsibleid'] == 0):
		Task.objects.defineresponsible(task_id=task_id, personid=request.user.id)
	return HttpResponseRedirect(reverse('dream', args=(dream_id,)))

	
def changeRole(request, id, dream_id):
	role_id = request.POST['campo']

	person = TeamMember.objects.changeRole(id=id, role_id=role_id)

	message = Messages.objects.addmessage(messageType=3,receiver=person.personid,dreamid=dream_id,extra=person.get_position_display())

	return HttpResponseRedirect(reverse('team', args=(dream_id,)))

def team(request, dream_id):
	if request.user.is_authenticated():
		if (request.user.is_superuser == True):
		 auth = TeamMember.objects.raw("SELECT * FROM app_teammember WHERE app_teammember.dreamid = %s", [dream_id])

		 if(len(list(auth)) < 1):
			 return redirect('/mydreams')

		 projects = Dream.objects.filter(id=dream_id)
		 members = TeamMember.objects.raw("SELECT * FROM app_teammember, auth_user WHERE app_teammember.personid = auth_user.id AND dreamid = %s", [dream_id])

		else:
		 auth = TeamMember.objects.raw("SELECT * FROM app_teammember WHERE app_teammember.dreamid = %s AND app_teammember.personid = %s", [dream_id, request.user.id])

		 if(len(list(auth)) < 1):
			return redirect('/mydreams')

		 projects = Dream.objects.filter(id=dream_id)
		 members = TeamMember.objects.raw("SELECT * FROM app_teammember, auth_user WHERE app_teammember.personid = auth_user.id AND dreamid = %s", [dream_id])

		context = {
			'dream' : projects,
			'team' : members,
			'auth' : auth[0]
		}
		return render(request, "team.html", context)
	else:
		return redirect('/')

def addteammember(request, dream_id):
	auth = TeamMember.objects.raw("SELECT * FROM app_teammember WHERE app_teammember.dreamid = %s AND app_teammember.personid = %s", [dream_id, request.user.id])

	if(len(list(auth)) < 1 or auth[0].position == 'TM'):
		return redirect('/mydreams')

	memberEmail = request.POST['memberEmail']
	memberRole = request.POST['memberRole']

	person = TeamMember.objects.raw("SELECT * FROM app_teammember, auth_user WHERE app_teammember.personid = auth_user.id AND auth_user.email = %s AND app_teammember.dreamid!=%s", [memberEmail,dream_id])
	if(len(list(person)) > 0):
		TeamMember.objects.addteammember(personid=person[0].personid,dreamid=dream_id,position=memberRole, active=0)

	return HttpResponseRedirect(reverse('team', args=(dream_id,)))

def deleteteammember(request, dream_id):
	auth = TeamMember.objects.raw("SELECT * FROM app_teammember WHERE app_teammember.dreamid = %s AND app_teammember.personid = %s", [dream_id, request.user.id])

	if(len(list(auth)) < 1 or auth[0].position != 'TL'):
		return redirect('/mydreams')
		
	member_id = request.POST['removeTeamMemberId']
	member = TeamMember.objects.get(id=member_id)
	member.delete()
	return HttpResponseRedirect(reverse('team', args=(dream_id,)))
	
def createdream(request, user_id):
    dreamname = request.POST['dreamName']
    dreamdescription = request.POST['dreamDescription']
    dream = Dream.objects.createDream(name=dreamname,description=dreamdescription)

    memberRole= 'TL'
    TeamMember.objects.addteammember(personid=user_id,dreamid=dream.id,position=memberRole,active=1)
    return HttpResponseRedirect(reverse('overview'))

def deletedream(request, dream_id):
	dream_id = request.POST['removeDreamId']
	raw_id = TeamMember.objects.filter(personid=request.user.id, dreamid=dream_id).values('id')
	raw = TeamMember.objects.get(id=raw_id)
	raw.delete()
	return HttpResponseRedirect(reverse('mydreams'))

def dreams(request):
	if request.user.is_authenticated():
		if (request.user.is_superuser == True):
		 dreams = TeamMember.objects
		 projects = TeamMember.objects.raw("SELECT * FROM  app_dream")		 
		else:
		 dreams = TeamMember.objects.filter(id=request.user.id)
		 projects = TeamMember.objects.raw("SELECT * FROM app_teammember JOIN app_dream ON app_teammember.dreamid = app_dream.id AND personid = %s", [request.user.id])

		if(len(list(projects)) < 1):
			projects = None
			
		context = {
			'dreams' : projects,
		}
		return render(request, "dreams.html", context)
	else:
		return redirect('/')

def overview(request):
    if request.user.is_authenticated():
		tasksCurrent = Task.objects.raw("SELECT * FROM app_task, app_dream WHERE app_task.dreamid = app_dream.id AND app_task.responsibleid=%s AND app_task.taskstatus=%s ORDER BY app_task.dreamid", [request.user.id,"current"])

		tasksTodo = Task.objects.raw("SELECT * FROM app_task, app_dream WHERE app_task.dreamid = app_dream.id AND app_task.responsibleid=%s AND app_task.taskstatus=%s ORDER BY app_task.dreamid", [request.user.id,"todo"])

		tasksDone = Task.objects.raw("SELECT * FROM app_task, app_dream WHERE app_task.dreamid = app_dream.id AND app_task.responsibleid=%s AND app_task.taskstatus=%s ORDER BY app_task.dreamid, app_task.dateFinished DESC", [request.user.id,"done"])

		if(len(list(tasksCurrent)) < 1):
			tasksCurrent = None

		if(len(list(tasksTodo)) < 1):
			tasksTodo = None

		if(len(list(tasksDone)) < 1):
			tasksDone = None
		
		context = {
            'user' : request.user,
            'tasksCurrent' : tasksCurrent,
            'tasksTodo' : tasksTodo,
            'tasksDone' : tasksDone
        }
		return render(request, "overview.html", context)
    else:
    	return redirect('/')
		
def requestmessages(request):
	invites = TeamMember.objects.raw("SELECT * FROM app_teammember JOIN app_dream ON app_teammember.dreamid = app_dream.id AND app_teammember.active= %s AND app_teammember.personid = %s", ["0",request.user.id])

	changedRoles = Messages.objects.raw("SELECT app_messages.id as id, app_dream.name as name, app_messages.extra as role FROM app_messages, app_dream WHERE app_messages.dreamid=app_dream.id AND app_messages.messageType=%s AND app_messages.receiver=%s AND app_messages.seen=%s", ["3", request.user.id,"0"])

	answers = Messages.objects.raw("SELECT app_messages.id as id, app_messages.messageType as type, app_messages.extra as invited, app_dream.name as dreamName FROM app_messages, app_teammember, app_dream WHERE app_messages.dreamid = app_teammember.dreamid AND app_dream.id=app_messages.dreamid AND (app_messages.messageType= %s OR  app_messages.messageType= %s) AND app_teammember.personid = %s AND app_messages.extra<>%s AND app_messages.seen=%s", ["1", "2",request.user.id, request.user.username,"0"])
	if(len(list(invites)) < 1):
			invites = None
	if(len(list(answers)) < 1):
			answers = None
	if(len(list(changedRoles)) < 1):
			changedRoles = None
	context = {
			'invites' : invites,
			'answers' : answers,
			'changedRoles' : changedRoles
		}
	return render(request, "messages.html", context)

def acceptinvite(request):
	dreamid= request.POST['acceptdreamid']
	invite = TeamMember.objects.filter(personid=request.user.id, dreamid=dreamid)

	if(len(list(invite)) < 1):
		return redirect('/messages')

	message = Messages.objects.addAnswer(messageType=2,dreamid=dreamid,extra=request.user.username)
	changed = TeamMember.objects.becomeActive(personid=request.user.id, dreamid=dreamid)
	return HttpResponseRedirect(reverse('requestmessages'))

def rejectinvite(request):
	dreamid= request.POST['rejectdreamid']
	invite = TeamMember.objects.filter(personid=request.user.id, dreamid=dreamid)

	if(len(list(invite)) < 1):
		return redirect('/messages')

	message = Messages.objects.addAnswer(messageType=1,dreamid=dreamid,extra=request.user.username)
	invite.delete()
	return HttpResponseRedirect(reverse('requestmessages'))

def seenmessage(request):
	id= request.POST['seenmessageid']
	message = Messages.objects.filter(id=id)

	if(len(list(message)) < 1):
		return redirect('/messages')

	message = Messages.objects.seenMessage(id=id)

	return HttpResponseRedirect(reverse('requestmessages'))
	
def addgift(request):
	gift = request.POST['gift']
	Gift.objects.addgift(request.user.id,gift)
	return HttpResponseRedirect(reverse('profile'))


def removegift(request, gift_id):
	gift = Gift.objects.get(id=gift_id)
	gift.delete()
	return HttpResponseRedirect(reverse('profile'))
