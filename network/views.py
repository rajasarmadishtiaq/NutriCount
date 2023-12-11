from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Network, NetworkSearch
from account.models import Profile
from django.shortcuts import render
from food.views import logs
from django.contrib.auth.models import User


@login_required
def my_network(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        menteeId = int(float(request.POST.get('menteeId')))
        request.session['menteeId'] = menteeId
        network_profile = Network.objects.get(mentee=menteeId, mentor=profile)
        if request.POST.get('Add'):
            network_profile.request = 1
            network_profile.save()
            messages.success(request, 'Mentee added!')
        elif request.POST.get('Delete'):
            network_profile.delete()
            messages.success(request, 'Mentee rejected!')
        else:
            return redirect('view_mentee_logs')

    mentees_added = []
    mentors_added = []
    mentees_pending = []
    mentors_pending = []

    network_search = NetworkSearch.objects.create(user=profile)
    for i in range(0, 2):
        mentors_search = network_search.get_mentors(request=i) if network_search else []
        mentees_search = network_search.get_mentees(request=i) if network_search else []
        for mentor in mentors_search:
            if i == 0:
                mentors_pending.append(get_object_or_404(Profile, id=mentor.mentor_id))
            else:
                mentors_added.append(get_object_or_404(Profile, id=mentor.mentor_id))
        for mentee in mentees_search:
            if i == 0:
                mentees_pending.append(get_object_or_404(Profile, id=mentee.mentee_id))
            else:
                mentees_added.append(get_object_or_404(Profile, id=mentee.mentee_id))

    return render(request, 'network/my_network.html',
                  {'section': 'network', 'profile': profile,
                   'mentors_added': mentors_added, 'mentees_added': mentees_added,
                   'mentors_pending': mentors_pending, 'mentees_pending': mentees_pending})


@login_required
def add_mentor(request):
    mentee_profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        query = request.POST.get('query')
        if User.objects.filter(username=query).exists():
            user = User.objects.get(username=query)
            mentor_profile = Profile.objects.get(user=user)
        else:
            messages.error(request, 'User does not exist!')
            return redirect('network')

        if mentee_profile == mentor_profile:
            messages.error(request, 'Cannot add yourself as the mentor!')
            return redirect('network')

        if Network.objects.filter(mentee=mentee_profile, mentor=mentor_profile).exists():
            messages.error(request, 'Mentor already added or request pending!')
        else:
            network_object = Network.objects.create(mentee=mentee_profile, mentor=mentor_profile, request=0)
            network_object.save()
            messages.success(request, 'Mentor request sent!')
            return redirect('network')
    return render(request, 'network/add_mentor.html')


@login_required
def remove_mentor_or_mentee(request):
    requesting_user = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        query = request.POST.get('query')

        if User.objects.filter(username=query).exists():
            user = User.objects.get(username=query)
            searched_user = Profile.objects.get(user=user)
        else:
            messages.error(request, 'User does not exist!')
            return redirect('network')

        if requesting_user == searched_user:
            messages.error(request, 'Cannot remove yourself!')
            return redirect('network')

        if Network.objects.filter(mentee=requesting_user, mentor=searched_user).exists():
            network_object = Network.objects.get(mentee=requesting_user, mentor=searched_user)
            network_object.delete()
            messages.success(request, 'Mentor successfully removed!')
            return redirect('network')

        if Network.objects.filter(mentee=searched_user, mentor=requesting_user).exists():
            messages.success(request, 'Mentee successfully removed!')
            network_object = Network.objects.get(mentee=searched_user, mentor=requesting_user)
            network_object.delete()
            return redirect('network')

        else:
            messages.error(request, 'Mentor/mentee not in your network!')
            return redirect('network')

    return render(request, 'network/remove_mentor.html')


@login_required
def view_mentee_logs(request):
    menteeId = request.session.get('menteeId')
    profile = get_object_or_404(Profile, id=menteeId)
    return logs(request, profile=profile, profile_flag=True)
