from django.shortcuts import render

from newsletter.models import Dream
from newsletter.models import TeamMember
from newsletter.models import SignUp

def about(request):
	return render(request, "about.html", {})

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