from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile, FoodSearch, Food, UserMetric
from .forms import AddFood, EditFood
import requests
from django.shortcuts import render
from api.serializers import FoodSerializer
import datetime
import calendar


@login_required
def logs(request):
    profile = Profile.objects.get(user=request.user)
    date = request.POST.get('date')
    if date is None:
        if request.session.get('date') is not None:
            date = request.session.get('date')
        else:
            date = str(datetime.date.today())

    user_metrics = track_calories(request, profile, date)

    if date:
        selected_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        food_search = FoodSearch.objects.create(user=profile, created_at=selected_date)
        saved_foods = food_search.get_saved_foods() if food_search else []
        request.session['date'] = date
        food_search.created_at = date
        food_search.save()
        macronutrients = calculate_macronutrients(request, profile, date, food_search)

    else:
        food_search = FoodSearch.objects.create(user=profile)
        saved_foods = food_search.get_saved_foods() if food_search else []

    return render(request, 'food/logs.html', {'section': 'logs', 'profile': profile,
                                              'saved_foods': saved_foods, 'date': date,
                                              'user_metrics': user_metrics, 'macronutrients': macronutrients})


def fetch_food_api(request, query):
    data = []
    api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
    headers = {'X-Api-Key': 'fUbkmWkTmNpCxcHSYDNZczgyYdrZP3qCJiVZ3oFl'}
    response = requests.get(api_url, headers=headers)
    if response.status_code == requests.codes.ok:
        data = response.json()
    return response, data


@login_required
def add_food(request):
    profile = Profile.objects.get(user=request.user)
    date = request.session.get('date')
    if request.method == 'POST':
        query = request.POST.get('query')
        response, data = fetch_food_api(request, query)
        if isinstance(data, list):
            if len(data) > 0:
                for items in data:
                    items['user'] = request.user.profile.pk
                    items['created_at'] = date
                    serializer = FoodSerializer(data=items)
                    if serializer.is_valid():
                        serializer.save()
                        messages.success(request, 'Food successfully added!')

                    else:
                        errors = serializer.errors
                        messages.error(request, errors)
                        return render(request, 'food/add_food.html')
            else:
                messages.error(request, "No data found for the given query.")
                return render(request, 'food/add_food.html')

            return redirect('logs')

        else:
            error_message = "Error: {} {}".format(response.status_code, response.text)
            messages.error(request, error_message)
            return render(request, 'food/add_food.html')
    else:
        return render(request, 'food/add_food.html', {'profile': profile})


@login_required
def edit_logs(request):
    if request.method == 'POST':
        food_id = int(float(request.POST.get('food_id')))
        food = get_object_or_404(Food, id=food_id)
        if request.POST.get('Delete'):
            food.delete()
            messages.success(request, 'Food successfully deleted!')
        else:
            serving_size_g = str(int(float(request.POST.get('serving_size_g'))))
            food_name = food.name
            query = serving_size_g + 'g ' + food_name
            response, data = fetch_food_api(request, query)
            if data:
                data[0]['user'] = request.user.profile.pk
                serializer = FoodSerializer(food, data=data[0])
                if serializer.is_valid():
                    serializer.save()
                    messages.success(request, 'Food successfully edited!')
                else:
                    messages.error(request, serializer.errors)

            else:
                messages.error(request, "No data found for the given query.")
            return redirect('logs')

    profile = Profile.objects.get(user=request.user)
    date = request.session.get('date')
    food_search = FoodSearch.objects.create(user=profile, created_at=date)
    saved_foods = food_search.get_saved_foods() if food_search else []
    return render(request, 'food/edit_logs.html', {'saved_foods': saved_foods, 'profile': profile})


@login_required
def track_calories(request, profile, date):
    food_search = FoodSearch.objects.create(user=profile, created_at=date)
    saved_foods = food_search.get_saved_foods() if food_search else []

    if UserMetric.objects.filter(user=profile, created_at=date).exists():
        user_metrics = UserMetric.objects.get(user=profile, created_at=date)
    else:
        user_metrics = UserMetric.objects.create(user=profile, created_at=date)

    total_calories_consumed = 0
    for food in saved_foods:
        total_calories_consumed += food.calories
    user_metrics.calories_consumed = total_calories_consumed
    user_metrics.save()
    return user_metrics


@login_required
def monthly_metrics(request):
    profile = Profile.objects.get(user=request.user)
    date = datetime.date.today()
    month, year = date.month, date.year
    total_days = calendar.monthrange(year, month)[1]
    monthly_caloric_goal = profile.calorie * total_days
    monthly_calories_consumed = 0

    for days in range(1, total_days + 1):
        if UserMetric.objects.filter(user=profile, created_at=str(date)[0:8] + str(days)).exists():
            user_metrics = UserMetric.objects.get(user=profile, created_at=str(date)[0:8] + str(days))
            monthly_calories_consumed += user_metrics.calories_consumed

    return monthly_caloric_goal, monthly_calories_consumed


@login_required
def weekly_metrics(request):
    profile = Profile.objects.get(user=request.user)
    date = datetime.date.today()
    month, year = date.month, date.year
    weeks = calendar.monthcalendar(year, month)
    weekly_calories_consumed = 0
    current_week = 0
    for week in weeks:
        for days in week:
            if str(days) == str(date)[9:]:
                current_week = week

    for days in current_week:
        if days == 0:
            continue
        else:
            if len(str(days)) == 1:
                search_date = str(date)[0:8] + '0' + str(days)
            else:
                search_date = str(date)[0:8] + str(days)
            if UserMetric.objects.filter(user=profile, created_at=search_date).exists():
                user_metrics = UserMetric.objects.get(user=profile, created_at=search_date)
                weekly_calories_consumed += user_metrics.calories_consumed

    weekly_caloric_goal = profile.calorie * len(current_week)
    print(weekly_caloric_goal, weekly_calories_consumed)
    return weekly_caloric_goal, weekly_calories_consumed


@login_required
def calculate_macronutrients(request, profile, date, food_search):
    total_carbs, total_proteins, total_fats = 0, 0, 0
    for foods in food_search.get_saved_foods():
        total_carbs += foods.carbohydrates_total_g
        total_proteins += foods.protein_g
        total_fats += foods.fat_total_g

    return total_carbs, total_proteins, total_fats
