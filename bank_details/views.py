from django.shortcuts import render
from .models import Branches
from django.core.paginator import Paginator
from django.db.models import Q

def bankdetails(request):
	alldata = Branches.objects.all()
	paginator = Paginator(alldata, 2, orphans=0)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request,'bank_details/detail.html',{'page_obj':page_obj})


def search(request):
	query = request.GET['query']
	q1 = (Q(ifsc__icontains=query)|Q(bank_name__icontains=query)|Q(bank_id__icontains=query)|Q(branch__icontains=query)|Q(address__icontains=query)|Q(city__icontains=query)|Q(district__icontains=query)|Q(state__icontains=query))
	searchdata = Branches.objects.filter(q1)
	paginator = Paginator(searchdata, 2, orphans=0)
	page_number = request.GET.get('page')
	page_obj1 = paginator.get_page(page_number)
	return render(request,'bank_details/search.html',{'page_obj1':page_obj1})

def filter(request):
	filterdata = Branches.objects.all()
	query = request.GET['city']
	fildata = Branches.objects.filter(city__icontains=query)
	paginator = Paginator(fildata, 2, orphans=0)
	page_number = request.GET.get('page')
	page_obj2 = paginator.get_page(page_number)
	return render(request,'bank_details/filter.html',{'page_obj2':page_obj2, 'filterdata':filterdata})
