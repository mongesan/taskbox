from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.utils import timezone

from main.models import Task
from main.forms import TaskForm


def index(request):
    """index"""
    form = TaskForm(instance=Task())
    tasks = Task.objects.all().order_by('-id')
    paginate_by = 10
    return render(request,
                  'main/index.html',
                  {'form': form,
                   'time': timezone.now,
                   'tasks': tasks})


# class ListIndex(ListView):
#     """index/Listed"""
#     context_object_name = 'tasks'
#     template_name = 'main/index.html'
#     paginate_by = 5
#
#     def get(self, request, *args, **kwargs):
#         tasks = Task.objects.all().order_by('-id')
#         self.object_list = tasks
#         context = self.get_context_data(object_list=self.object_list)
#         return self.render_to_response(context)


def task_add(request, task_id):
    """タスクの追加"""
    # print(task_id)
    task = Task()
    tasks = Task.objects
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            if tasks.filter(id=task_id).exists():
                messages.info(request, '1件のタスクを編集しました。')
                tasks.filter(id=task_id).delete()
            else:
                messages.info(request, '1件のタスクを追加しました。')
            task = form.save(commit=False)
            task.id = task_id
            task.save()
            form = TaskForm()
            return redirect('main:index')


def task_delete(request, task_id):
    if request.META.get('HTTP_REFERER'):
        task = get_object_or_404(Task, pk=task_id)
        task.delete()
        messages.info(request, '1件のタスクを削除しました。')

    return redirect('main:index')


def task_finish(request, task_id):
    if request.META.get('HTTP_REFERER'):
        task = get_object_or_404(Task, pk=task_id)
        task.delete()
        messages.success(request, '👏🎉タスクを完了しました！おめでとう！🎉👏')

    return redirect('main:index')


def task_stat_plus(request, task_id):
    """タスクの進捗増加"""
    # return HttpResponse('+')
    task = get_object_or_404(Task, pk=task_id)
    if task.stat < task.stat_max and request.META.get('HTTP_REFERER', ''):
        task.stat += 1
        task.save()
    return redirect('main:index')


def task_stat_minus(request, task_id):
    """タスクの進捗増加"""
    # return HttpResponse('-')
    task = get_object_or_404(Task, pk=task_id)
    if task.stat > 0 and request.META.get('HTTP_REFERER', ''):
        task.stat -= 1
        task.save()
    return redirect('main:index')
