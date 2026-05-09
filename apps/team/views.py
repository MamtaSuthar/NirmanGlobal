from django.shortcuts import render
from apps.projects.models import TeamMember

def home(request):
    team_members = TeamMember.objects.filter(is_active=True)

    return render(request, 'home.html', {
        'team_members': team_members
    })