from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

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

def team(request, dream_id):
	members = TeamMember.objects.raw("SELECT * FROM newsletter_teammember, auth_user WHERE newsletter_teammember.personid = auth_user.id AND dreamid = %s", [dream_id])
	context = {
		'dream' : dream_id,
		'team' : members
	}
	return render(request, "team.html", context)

def dreams(request):
	#dream1 = Dream.objects.create_dream("Dream3", "Category1", "Theme1", "Description1")
	#dreams1 = TeamMember.objects.add_to_dream_team("aaa", "email", 21, 1, "TL")
	#dreams2 = TeamMember.objects.add_to_dream_team("aaa", "email", 21, 2, "TM")
	if request.user.is_authenticated():
		dreams = TeamMember.objects.filter(personid=request.user.id)
		projects = TeamMember.objects.raw("SELECT * FROM newsletter_teammember JOIN newsletter_dream ON newsletter_teammember.dreamid = newsletter_dream.id AND personid = %s", [request.user.id])
		context = {
			'dreams' : projects,
		}
		return render(request, "dreams.html", context)
	else:
		return redirect('/');