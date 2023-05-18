from django.shortcuts import render, redirect

def main(request):
	if request.user.is_authenticated:
		return render(request, 'base.html')
	else:
		return redirect('/accounts/login')
