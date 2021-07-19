from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from django.contrib.auth.decorators import login_required

def index(request):
    question_list = Question.objects.order_by('-create_date')  # "-" 기호 넣으면 내림차순
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)
    #return HttpResponse("welcome!! pybo에 오신것을 환영합니다.")

def detail(request, question_id):
    #question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id) # pk : primary key
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)


@login_required(login_url='common:login')
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user   # 인증된 사용자, 글쓴이 추가
            answer.question = question
            answer.create_date = timezone.now()
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)


@login_required(login_url='common:login')
def question_create(request):
    # 질문 등록
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():   # 폼이 유효한지 검사
            question = form.save(commit=False)  # 임시저장
            question.author = request.user  # 인증된 사용자, 글쓴이 추가
            question.create_date = timezone.now()
            question.save()  # 진짜 저장
            return redirect('pybo:index')
    else:  # request.method == 'GET'
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)


def jqtest(request):
    return render(request, 'pybo/jqtest.html')

def imgtest(request):
    return render(request, 'pybo/imgtest.html')

def market(request):
    return render(request, 'pybo/market.html')

def components(request):
    return render(request, 'pybo/boot_components.html')