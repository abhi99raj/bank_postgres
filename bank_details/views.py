from django.shortcuts import render
from .models import Branches
from django.core.paginator import Paginator

def bankdetails(request):
	alldata = Branches.objects.all()
	paginator = Paginator(alldata, 2, orphans=0)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	return render(request,'bank_details/detail.html',{'page_obj':page_obj})
