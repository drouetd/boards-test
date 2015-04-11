from django.shortcuts import render

from boards.models import Organization, Person, Relationship

def index(request):
	org_list = Organization.objects.all()
	context = {'org_list': org_list}
	return render(request, 'boards/index.html', context)

def org_staff(request, org_id):
	staff_list = Person.objects.filter(organization__id = org_id)
	context = {'staff_list': staff_list, 'org_name': Organization.objects.get(pk=org_id).name}
	return render(request, 'boards/staff.html', context)

def member_of(request, person_id):
	person = Person.objects.get(pk=person_id)
	relationships = Relationship.objects.filter(person__pk=person_id)
	context = {'person': person,'relationships': relationships}
	return render(request, 'boards/membership.html', context)

def ajah_staff(request):
	staff_list = Person.objects.filter(organization__name = 'Ajah')
	context = {'staff_list': staff_list}
	return render(request, 'boards/ajah.html', context)