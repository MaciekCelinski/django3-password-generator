from django.shortcuts import render
# from django.http import HttpResponse
import random

# Create your views here.


def home(request):
		# this will automatically look inside the templates folder so we don't need to add it to the path
		# we can add some info to out template in third argument
		# return render(request, 'generator/home.html', {'password': 'huigr3423'})
		return render(request, 'generator/home.html')


def about(request):
		name = request.GET.get('name')
		return render(request, 'generator/about.html', {'name': name})


def password(request):

		characters = list('abcdefghijklmnopqrstuvwxyz')

		if request.GET.get('uppercase'):
				characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

		if request.GET.get('numbers'):
				characters.extend(list('0123456789'))

		if request.GET.get('specials'):
				characters.extend(list('!@#$%^&*?'))

		length = int(request.GET.get('length'))

		the_password = ''

		for x in range(length):
				the_password += random.choice(characters)

		return render(request, 'generator/password.html', {'password': the_password})
