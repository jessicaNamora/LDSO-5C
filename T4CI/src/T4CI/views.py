from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from newsletter.models import Dream
from newsletter.models import Task
from newsletter.models import TeamMember
from newsletter.models import SignUp


def about(request):
	return render(request, "about.html", {})

def dream(request, dream_id):
	if request.user.is_authenticated():
		auth = Task.objects.raw("SELECT * FROM newsletter_teammember WHERE newsletter_teammember.dreamid = %s AND newsletter_teammember.personid = %s", [dream_id, request.user.id])

		if(len(list(auth)) < 1):
			return redirect('/mydreams')

		projects = Dream.objects.filter(id=dream_id)
		tasks = Task.objects.raw("SELECT * FROM newsletter_task, newsletter_teammember WHERE newsletter_task.dreamid = newsletter_teammember.dreamid AND newsletter_task.dreamid = %s AND newsletter_teammember.personid = %s", [dream_id, request.user.id])
	
		if(len(list(tasks)) < 1):
			tasks = None

		if(projects):
			project = projects[0]
		else:
			project = None

		context = {
			'dream' : project,
			'tasks' : tasks
		}
		return render(request, "dream.html", context)
	else:
		return redirect('/')
	
def addtask(request, dream_id):
	taskname = request.POST['taskName']
	taskstatus = request.POST['taskStatus']
	task = Task.objects.addtask(taskname=taskname,taskstatus=taskstatus,dreamid=dream_id)

	return HttpResponseRedirect(reverse('dream', args=(dream_id,)))

def edittask(request, dream_id):
	taskname = request.POST['taskName']
	taskstatus = request.POST['taskStatus']
	task_id = request.POST['edittaskid']
	Task.objects.edittask(taskname=taskname,taskstatus=taskstatus,task_id=task_id)

	return HttpResponseRedirect(reverse('dream', args=(dream_id,)))


def deletetask(request, dream_id):
	task_id = request.POST['deletetaskid']
	Task.objects.deletetask(task_id=task_id)

	return HttpResponseRedirect(reverse('dream', args=(dream_id,)))

def team(request, dream_id):
	projects = Dream.objects.filter(id=dream_id)
	members = TeamMember.objects.raw("SELECT * FROM newsletter_teammember, auth_user WHERE newsletter_teammember.personid = auth_user.id AND dreamid = %s", [dream_id])
	context = {
		'dream' : projects,
		'team' : members
	}
	return render(request, "team.html", context)

def deleteteammember(request, dream_id):
	member_id = request.POST['removeTeamMemberId']
	#Team.objects.deleteteammember(member_id=member_id)
	member = TeamMember.objects.get(id=member_id)
	member.delete()
	return HttpResponseRedirect(reverse('team', args=(dream_id,)))

def deletedream(request, dream_id):
	dream_id = request.POST['removeDreamId']
	raw_id = TeamMember.objects.filter(personid=request.user.id, dreamid=dream_id).values('id')
	#raw_id = TeamMember.objects.raw("SELECT id FROM newsletter_teammember WHERE newsletter_teammember.personid = %s AND newsletter_teammember.dreamid = %s", [request.user.id, dream_id])[0]
	raw = TeamMember.objects.get(id=raw_id)
	raw.delete()
	return HttpResponseRedirect(reverse('mydreams'))

def dreams(request):
	#dream1 = Dream.objects.create_dream("Dream3", "Category1", "Theme1", "Description1")
	#dreams1 = TeamMember.objects.add_to_dream_team("aaa", "email", 21, 1, "TL")
	#dreams2 = TeamMember.objects.add_to_dream_team("aaa", "email", 21, 2, "TM")
	if request.user.is_authenticated():
		dreams = TeamMember.objects.filter(id=request.user.id)
		projects = TeamMember.objects.raw("SELECT * FROM newsletter_teammember JOIN newsletter_dream ON newsletter_teammember.dreamid = newsletter_dream.id AND personid = %s", [request.user.id])
		context = {
			'dreams' : projects,
		}
		return render(request, "dreams.html", context)
	else:
		return redirect('/');