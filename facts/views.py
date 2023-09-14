from django.shortcuts import render, redirect
import requests, random
from .models import MathProblem
from .forms import MathProblemForm
from django.http import JsonResponse

def cat_fact(request):
    # Define the URL for fetching a random cat fact.
    cat_fact_url = 'https://catfact.ninja/fact?max_length=140'
    # Define the URL for fetching random cat pictures.
    cat_pic_url = 'https://api.thecatapi.com/v1/images/search'

    try:
        # Send a GET request to fetch a random cat fact and parse the JSON response.
        cat_fact_res = requests.get(cat_fact_url).json()
        # Send GET requests to fetch two random cat pictures and parse their JSON responses.
        cat_pic_res1 = requests.get(cat_pic_url).json()
        cat_pic_res2 = requests.get(cat_pic_url).json()
        # Extract the URLs of the random cat pictures.
        random_cat_image_url1 = cat_pic_res1[0]['url']
        random_cat_image_url2 = cat_pic_res2[0]['url']

    # Handle exceptions, such as network errors, using a RequestException.
    except requests.exceptions.RequestException as e:
        # Create an error message containing the exception details.
        error_message = f"Error: {e}"
        # Render an error page with the error message.
        return render(request, 'cat_app/error.html', {'error_message': error_message})
    
    # Create a context dictionary containing the cat fact and random cat picture URLs.
    context = {
        'cat_fact': cat_fact_res['fact'],
        'cat_pic': random_cat_image_url1,
        'cat_pic2': random_cat_image_url2
    }

    # Render the 'catfacts.html' template with the context data.
    return render(request, 'facts/catfacts.html', context)





def math_gen(request):
    # Clear existing MathProblem objects from the database.
    MathProblem.objects.all().delete()

    # Initialize an empty list to store math problems.
    problems = []

    # Generate 50 random math problems.
    for _ in range(50):
        # Generate random numbers between 0 and 99 for num1 and num2.
        num1 = random.randint(0, 99)
        num2 = random.randint(0, 99)

        # Calculate the correct answer by adding num1 and num2.
        answer = num1 + num2

        # Append the problem (num1, num2, and answer) to the 'problems' list.
        problems.append({'num1': num1, 'num2': num2, 'answer': answer})

    # Create an instance of the MathProblemForm.
    form = MathProblemForm()
    
    # Create a context dictionary containing the 'problems' list and the 'form'.
    context = {
        'problems': problems, 
        'form': form
    }

    # Render the 'math.html' template with the context data.
    return render(request, 'facts/math.html', context)
