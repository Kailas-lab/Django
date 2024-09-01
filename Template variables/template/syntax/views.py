from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# views.py
from django.shortcuts import render, get_object_or_404
from .models import Member  # Replace with your actual model import

def all_members(request):
    members = Member.objects.all()  # Retrieve all members from the database
    context = {
        'mymembers': members
    }
    return render(request, 'all_members.html', context)

def member_details(request, member_id):
    member = get_object_or_404(Member, id=member_id)  # Retrieve a specific member by ID
    context = {
        'mymember': member
    }
    return render(request, 'details.html', context)


def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())



def testing(request):
  template = loader.get_template('template.html')
  context = {
    'cars': [
      {
        'brand': 'Ford',
        'model': 'Mustang',
        'year': '1964',
      },
      {
        'brand': 'Ford',
        'model': 'Bronco',
        'year': '1970',
      },
      {
        'brand': 'Volvo',
        'model': 'P1800',
        'year': '1964',
      }]
    }
  return HttpResponse(template.render(context, request)) 







