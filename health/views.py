from django.shortcuts import render
from django.http import HttpResponseRedirect
import csv
from . import database
import threading
from .forms import RegForm
from django.template import loader
from django.http import HttpResponse
# Create your views here



class LoadDatabase(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.db_class = database.Database()

		self.get_thread_data()

	def get_thread_data(self):
		return self.db_class.get_data()




def home(request):


	context = {}

	if request.method == "POST":
		context['first_name'] = request.POST.get('first_name', False)
		context['last_name']  = request.POST.get('last_name', False)
		context['gender']     = request.POST.get('gender', False)

		return HttpResponseRedirect('/symptom')

	return render(request, 'health/index.html', context)



def symptom(request):

	# load_database = LoadDatabase()
	# load_database.start()
	# db = load_database.get_thread_data()

	# print (db['RASH'][1:])

	context = {}
	name = request.session['temp']
	context['name'] = name
	print name
	if request.method == "POST":
		load_database = LoadDatabase()
		load_database.start()
		db = load_database.get_thread_data()

		result = db[request.POST.get('search_symptom', False)][1:]
		print result
		context['results'] = result
		
		return render(request, 'health/symptom.html',context)
	return render(request, 'health/symptom.html',context)
		# return HttpResponseRedirect('/symptom')



	return render(request, 'health/symptom.html', context)

def register(request):

	if request.method == 'POST':
		ans = request.POST.get('First_Name')
		ans1 = request.POST.get('Last_Name')
		request.session['temp'] = ans
		form = RegForm(request.POST)
		print form
		if form.is_valid():
			print "Hello"
			form.save()
			return HttpResponseRedirect('/symptom')

	else:
		form = RegForm()
	return render(request,'health/index.html')