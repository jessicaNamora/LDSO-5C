from django.shortcuts import render

from newsletter.models import Dream
from newsletter.models import TeamMember
from newsletter.models import SignUp

def about(request):
	return render(request, "about.html", {})

def dreams(request):
	dreams = TeamMember.objects.filter(personid=request.user.id)
	context = {
		'dreams' : dreams,
	}
	return render(request, "dreams.html", context)