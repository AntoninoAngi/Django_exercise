from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.template.loader import render_to_string
from django.db.models import Q
import operator
from functools import reduce

from .models import Car

def car_upload(request):
	template = 'index.html'

	if request.method == 'GET':

		if request.is_ajax():
			context={}
			query_search = request.GET.get('q')

			if query_search:

				parts = query_search.split()
				i = len(parts)

				# I assumed that you could search for both make, model and make+model, as shown in pdf
				if (i > 1):
					for j in range(1, i): 
						qset = reduce(operator.__and__, [Q(make__istartswith=parts[0]) & Q(model__istartswith=parts[j])])
				else:
					qset = reduce(operator.__or__, [Q(make__istartswith=parts[0]) | Q(model__istartswith=parts[0])])

				cars = Car.objects.filter(qset).distinct()[0:50]
			else:
				cars = Car.objects.all()

			context["cars"] = cars
			html = render_to_string(template_name="cartable.html", context = context)
			data_dict = {"html_passed": html}

			return JsonResponse(data=data_dict, safe=False)
		return render(request, template)

	if request.method == 'POST':
		context = {}
		json_file = request.FILES['file']
		context["cars"] = json.load(json_file)
		context["cars"].sort(key=lambda x: x.get('make'))
		for car in context["cars"]:
			Car.objects.create(model_year=car['model_year'], make=car['make'], model=car['model'], rejection_percentage=car['rejection_percentage'], reason_1=car['reason_1'], reason_2=car['reason_2'], reason_3=car['reason_3'])
		return render(request, template, context)

	return render(request, "index.html", context=context)

	