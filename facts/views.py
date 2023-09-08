from django.shortcuts import render, redirect
import requests, random
from .models import MathProblem
from .forms import MathProblemForm
from django.http import JsonResponse

def cat_fact(request):
    cat_fact_url = 'https://catfact.ninja/fact?max_length=140'
    cat_pic_url= 'https://api.thecatapi.com/v1/images/search'

    try:
        cat_fact_res = requests.get(cat_fact_url).json()
        cat_pic_res1 = requests.get(cat_pic_url).json()
        cat_pic_res2 = requests.get(cat_pic_url).json()
        random_cat_image_url1 = cat_pic_res1[0]['url']
        random_cat_image_url2 = cat_pic_res2[0]['url']

    except requests.exceptions.RequestException as e:
        error_message = f"Error: {e}"
        return render(request, 'cat_app/error.html', {'error_message': error_message})
    
    context={
    'cat_fact' : cat_fact_res['fact'],
    'cat_pic' : random_cat_image_url1,
    'cat_pic2' : random_cat_image_url2
    }

    return render(request, 'facts/catfacts.html', context)

# views.py




def math_gen(request):
    MathProblem.objects.all().delete()  # Clear existing problems
    problems = []
    for _ in range(50):
        num1 = random.randint(0, 99)
        num2 = random.randint(0, 99)
        answer = num1 + num2
        problems.append({'num1': num1, 'num2': num2, 'answer': answer})

    form = MathProblemForm()
    
    context = {
        'problems': problems, 
        'form': form}

    return render(request, 'facts/math.html', context)

