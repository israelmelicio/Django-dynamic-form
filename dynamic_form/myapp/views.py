from django.shortcuts import render
from .forms import MyForm


def form(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # Process the data, redirect, or do something else
            return render(request, 'myapp/form_success.html')
    else:
        form = MyForm()

    return render(request, 'myapp/form.html', {'form': form})
