from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator
from django.http import Http404

from qa.models import Question


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page, paginator

@require_GET
def main(request, *args, **kwargs):
    qs = Question.objects.new()   
    page, paginator = paginate(request, qs)
    return render(request, 'index.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page
        })


@require_GET
def popular(request, *args, **kwargs):
    qs = Question.objects.popular()
    page, paginator = paginate(request, qs)
    return render(request, 'index.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page
        })


@require_GET
def question_detail(request, *args, **kwargs):
    question_id = kwargs.get('pk', None)
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        raise Http404
    return render(request, 'question.html', {'question': question})


















