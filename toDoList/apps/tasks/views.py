from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Task
from .utils import is_authorized


@is_authorized
def index(request):
    task_list = Task.objects.order_by('-create_datetime')[:10]

    if request.method == 'GET':
        return render(request, 'tasks/list.html', {'task_list': task_list})

    elif request.method == 'POST':
        new_task = Task.objects.create(task_text=request.POST['task_text'], create_datetime=datetime.now())
        new_task.save()

        return HttpResponseRedirect(reverse('index'))
