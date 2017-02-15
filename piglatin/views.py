from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')

def translate(request):
	original=request.GET['mytext']
	translate=''
	for word in original.split():
		if word[0] in ['a','e','i','o','u']:
			#vowel
			translate+=word
			translate+=' yay '
		else:
			#const
			translate+=word[1:]
			translate+=word[0]
			translate+='ay'
			translate+=' const '
	#return HttpResponse("Your on the translate page  !{} sadasds{} ".format(original,translate))
	return render(request, 'translate.html',{'original':original, 'translate':translate})

def signup(request):
	return render(request, 'signup.html')

