from django.shortcuts import render

from newsletter.models import Dream
from newsletter.models import Task
from newsletter.models import TeamMember
from newsletter.models import SignUp

def about(request):
	return render(request, "about.html", {})

def dream(request, dream_id):
	project = Dream.objects.filter(id=dream_id)
	tasks = Task.objects.raw("SELECT * FROM newsletter_task WHERE dreamid = %s", [dream_id])
	context = {
		'dream' : project[0],
		'tasks' : tasks
	}
	return render(request, "dream.html", context)

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
	dreams = TeamMember.objects.filter(personid=request.user.id)
	projects = TeamMember.objects.raw("SELECT * FROM newsletter_teammember JOIN newsletter_dream ON newsletter_teammember.dreamid = newsletter_dream.id AND personid = %s", [request.user.id])
	context = {
		'dreams' : projects,
	}
	return render(request, "dreams.html", context)