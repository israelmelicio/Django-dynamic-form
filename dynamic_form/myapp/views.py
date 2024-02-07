from django.shortcuts import render
# from .models import OccurrenceCategory

def form(request):
    # category = OccurrenceCategory.objects.get(id=category_id)
    # tasks_schema = category.tasksSchema
    tasks_schema = "{}"
    with open('schema.json') as f:
        tasks_schema = f.read()
    return render(request, 'form.html', {'tasks_schema': tasks_schema})
