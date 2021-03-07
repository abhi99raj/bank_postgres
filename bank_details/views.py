from django.shortcuts import render
from .models import Branches
from django.core.paginator import Paginator
from django.db.models import Q
import requests
from django.http import HttpResponse
import json

def filter(request):
	if request.method == 'POST':
		city = request.POST['city']
		url = 'http://127.0.0.1:8000/api/crud2/?city='+str(city)
		r = None
		if url is not None:
			r = requests.get(url)
		alldata=None
		if r is not None:
			alldata = r.json()
		return HttpResponse(json.dumps({'alldata':alldata, 'filter_value':True}))
	
def get_data(request, page=1):
	url = None
	url_for_city = 'http://127.0.0.1:8000/api/crud2/'
	if url_for_city is not None:
		r_for_city = requests.get(url_for_city)
	alldata_for_city = None
	if r_for_city is not None:
		alldata_for_city = r_for_city.json()
		city_list = []
		for item in alldata_for_city:
			city_list.append(item['city'])
	if page:
		url = 'http://127.0.0.1:8000/api/crud/?page='+str(page)
	r = None
	if url is not None:
		r = requests.get(url)
	alldata = None
	if r is not None:
		alldata = r.json()
	results = None
	next_page = None
	privious_page = None
	if alldata is not None:
		results = alldata['results']
		next_page = alldata['next']
		privious_page = alldata['previous']
	get_next_page_number = None
	get_previous_page_number = None
	if alldata is not None and alldata['next'] and next_page is not None:
		get_next_page_number = int(next_page.split("=")[1])
	if alldata is not None and alldata['previous'] and privious_page is not None:
		try:
			get_previous_page_number = int(privious_page.split("=")[1])
		except:
			get_previous_page_number = 1
	context = {'filter_value': False}
	if results is not None and len(results) > 0:
		context['results'] = results
	if alldata is not None:
		context['alldata'] = alldata
	if get_previous_page_number is not None:
		context['get_previous_page_number'] = get_previous_page_number
	if get_next_page_number is not None:
		context['get_next_page_number'] = get_next_page_number
	if city_list is not None and len(city_list) > 0:
		context['alldata_for_city'] = set(city_list)
	return render(request,'bank_details/detail.html',context)