from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, UpdateView, DeleteView
from task_app.models.task import Task
from task_app.forms import TaskForm
import datetime
from datetime import timedelta
from django.utils.timezone import utc

now = datetime.datetime.utcnow().replace(tzinfo=utc)

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context


class DetailView(TemplateView):
    template_name: str = 'task_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        return context


class AddView(TemplateView):
    template_name: str = 'add_task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = TaskForm()
        context['form'] = form
        return context

    
    def post(self, request, *args, **kwargs):
        form = TaskForm(self.request.POST)
        if form.is_valid():
            task = Task.objects.create(**form.cleaned_data)
            return redirect('index_view')
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'update_task.html'
    success_url = '/'


class DeleteTask(DeleteView):
    model = Task
    template_name: str = 'confirm_delete.html'
    success_url = '/'
