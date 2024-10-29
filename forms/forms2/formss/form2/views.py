from django.shortcuts import render
from .forms import SimpleForm

def simple_form_view(request):
    if request.method == 'POST':
        form = SimpleForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            # Process the data (e.g., print or save it)
            print(f"Name: {name}, Email: {email}, Age: {age}")
            return render(request, 'success.html', {'name': name})
    else:
        form = SimpleForm()  # Create an empty form instance

    # Render the form template for both GET and invalid POST requests
    return render(request, 'simple_form.html', {'form': form})
