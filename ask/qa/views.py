from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout

from qa.models import Question
from qa.forms import AskForm, AnswerForm, SignupForm, LoginForm


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


def question_detail(request, *args, **kwargs):
    question_id = kwargs.get('pk', None)
    try:
        question = Question.objects.get(id=question_id)
        form = AnswerForm(initial={'question': question})
    except Question.DoesNotExist:
        raise Http404    
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save()
            answer.question = question
            answer.save()
            if request.user.is_authenticated:
                answer.author = request.user
                answer.save()            
        url = reverse('question_detail', args=[question.id])
        form = AnswerForm(initial={'question': question})
        # return render(request, 'question.html', {'question': question, 'form': form})
    return render(request, 'question.html', {'question': question, 'form': form})



def ask(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            form._user = request.user
            post = form.save()
            url = post.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'ask.html', {'form': form})


def signup(request, *args, **kwargs):
    if request.method == "POST":
        # logout(request)
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return HttpResponseRedirect('/')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def login_ask(request, *args, **kwargs):
    if request.method == "POST":
        # logout(request) 
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            print(username, password)
            login(request, user)
            url = reverse('main')
            return HttpResponseRedirect(url)
        request.session['sessionid'] = None
        return HttpResponseRedirect('/login/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})



















