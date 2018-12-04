from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import qasession, question, answer, comment
from .forms import addsessForm, addquesForm, addAnswerForm, addCmForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from account.decorators import ad_required, teacher_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
@login_required
def list(request):
    list = qasession.objects.all().order_by('-create_at')



    


    return  render(request, 'sessions/list.html', {'list':list})

@login_required
@teacher_required
def add(request):
    form = addsessForm()
    if request.method == 'POST':
        form = addsessForm(request.POST)
        teacher = request.POST['teacher']
        user = User.objects.get(username=teacher)
        if form.is_valid():
            form.save(user.id)
            return redirect('/list')
    return render(request, 'sessions/addsess.html', {'form': form})

@login_required
def showSession(request, sid):
    form = addquesForm()
    qa = qasession.objects.get(id=sid)
    qao = qasession.objects.filter(id=sid)
    quesl = question.objects.all()
    ques = quesl.filter(qa_id=sid)
    if request.method == 'POST' and 'btnclose' in request.POST:
        qao.update(status=1)
        return redirect('/session/' + str(sid))
    if request.method == 'POST' and 'btnopen' in request.POST:
        qao.update(status=0)
        return redirect('/session/' + str(sid))
    if request.method == 'POST' and 'btndelete' in request.POST:
        qao.delete()
        return redirect('/list')
    if qa.status == 0:
        if request.method == 'POST' and 'btn1' in request.POST:
            form = addquesForm(request.POST)
            owner = request.POST['owner']
            user = User.objects.get(username=owner)
            if form.is_valid():
                form.save(user.id, sid)
                return redirect('/session/' + str(sid))
    return render(request, 'sessions/session.html', {'qa': qa, 'sid': sid, 'ques': ques, 'form': form})

@login_required
def showQuestion(request, id):
    form = addAnswerForm()
    form2 = addCmForm()
    ques = question.objects.get(id=id)
    cmt = comment.objects.all()
    ansl = answer.objects.all()
    ans = ansl.filter(ques_id=id)
    if request.method == 'POST'and "oid" in request.POST:
        form = addAnswerForm(request.POST)
        uid = request.POST['oid']
        if form.is_valid():
            form.save(uid, id)
            return redirect('/question/' + str(id))
    if request.method == 'POST'and "uid" in request.POST:
        form2 = addCmForm(request.POST)
        uid = request.POST['uid']
        aid = request.POST['aid']
        if form2.is_valid():
            form2.save(uid, aid)
            return redirect('/question/' + str(id))
    return render(request, 'sessions/question.html', {'ques': ques, 'id': id, 'cmt': cmt, 'ans': ans, 'form': form, 'form2': form2})

@login_required
def myquestions(request):
    ques = question.objects.all()

    return  render(request, 'sessions/myquestions.html', {'ques':ques})
