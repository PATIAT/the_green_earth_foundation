from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import TeamMember
from .forms import TeamMemberForm


# Create your views here.
def team_members(request):
    """
    View to render the team members page
    """
    members = TeamMember.objects.all()
    return render(request, 'team/team_members.html', {'members': members})


def team_member_detail(request, pk):
    """
    View to render individual team members pages
    """
    member = get_object_or_404(TeamMember, pk=pk)
    return render(request, 'team/team_member_detail.html', {'member': member})


def add_team_member(request):
    """
    View for the addition of team members
    """
    if request.method == 'POST':
        form = TeamMemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('team:team_members')
    else:
        form = TeamMemberForm()
    return render(request, 'team/add_team_member.html', {'form': form, 'url_name': 'team:add_team_member'})


def edit_team_member(request, pk):
    """
    View for the amendment of team members
    """
    member = get_object_or_404(TeamMember, pk=pk)
    if request.method == 'POST':
        form = TeamMemberForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            return redirect('team:team_members')
    else:
        form = TeamMemberForm(instance=member)
    return render(request, 'team/edit_team_member.html', {'form': form, 'member': member})


def delete_team_member(request, pk):
    """
    View for the deletion of team members
    """
    member = get_object_or_404(TeamMember, pk=pk)
    if request.method == 'POST':
        member.delete()
        return redirect('team:team_members')
    return render(request, 'team/delete_team_member.html', {'member': member})
