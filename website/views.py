from django.shortcuts import render,redirect
from .models import Question,Response
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from .forms import RegUserForm,Loginform,NewQuestionForm,NewResponseForm,NewReplyForm
# Create your views here.
def homepg(request):
    questions=Question.objects.all().order_by('-created_at')
    context={
        'questions':questions
    }
    return render(request,'homepg.html',context)
def registerpg(request):
    form=RegUserForm()
    if request.method=="POST":
       form = RegUserForm()

    if request.method == 'POST':
        try:
            form = RegUserForm(request.POST)
            if form.is_valid():
                user=form.save()
                login(request,user)
                return redirect('index')
               
        except Exception as e:
            print(e)
            raise
    context={
       'form':form
   } 
   
    return render(request, 'register.html',context)
def loginpg(request):
    form = Loginform()

    if request.method == 'POST':
        try:
            form = Loginform(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('index')
        except Exception as e:
            print(e)
            raise

    context = {'form': form}
    return render(request, 'login.html', context)
@login_required(login_url='register')    
def logoutpg(request):
    logout(request)
    return redirect('login')
@login_required(login_url='register')    
def newquestPage(request):
    form = NewQuestionForm()

    if request.method == 'POST':
        try:
            form = NewQuestionForm(request.POST)
            if form.is_valid():
                question = form.save(commit=False)
                question.author = request.user
                question.save()
        except Exception as e:
            print(e)
            raise

    context = {'form': form}
    
    return render(request,'new_question.html',context)    
def questPage(request, id):
    response_form = NewResponseForm()
    reply_form = NewReplyForm()

    if request.method == 'POST':
        try:
            response_form = NewResponseForm(request.POST)
            if response_form.is_valid():
                response = response_form.save(commit=False)
                response.user = request.user
                response.question = Question(id=id)
                response.save()
                return redirect('/question/'+str(id)+'#'+str(response.id))
        except Exception as e:
            print(e)
            raise

    question = Question.objects.get(id=id)
    context = {
        'question': question,
        'response_form': response_form,
        'reply_form': reply_form,
    }
    print(question)
    return render(request, 'question.html', context)    
@login_required(login_url='register')
def replyPage(request):
    if request.method == 'POST':
        try:
            form = NewReplyForm(request.POST)
            if form.is_valid():
                question_id = request.POST.get('question')
                parent_id = request.POST.get('parent')
                reply = form.save(commit=False)
                reply.user = request.user
                reply.question = Question(id=question_id)
                reply.parent = Response(id=parent_id)
                reply.save()
                return redirect('/question/'+str(question_id)+'#'+str(reply.id))
        except Exception as e:
            print(e)
            raise

    return redirect('index')    