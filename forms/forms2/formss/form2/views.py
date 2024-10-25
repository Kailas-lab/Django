# views.py
from django.shortcuts import render
from django.views import View
from .forms import SimpleForm

class SimpleFormView(View):
    def get(self, request):
        # Handle GET request (display the form)
        form = SimpleForm()  # Create an empty form instance
        return render(request, 'simple_form.html', {'form': form})

    def post(self, request):
        # Handle POST request (form submission)
        form = SimpleForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            # Process the data (e.g., print or save it)
            print(f"Name: {name}, Email: {email}, Age: {age}")
            return render(request, 'success.html', {'name': name})
        
        # If form is not valid, re-display the form with errors
        return render(request, 'simple_form.html', {'form': form})
