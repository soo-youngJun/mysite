from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from django.utils import timezone
from .forms import QuestionForm, AnswerForm

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

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.create_date = timezone.now()
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)

def question_create(request):
    # 질문 등록
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():   # 폼이 유효한지 검사
            question = form.save(commit=False)  # 임시저장
            question.create_date = timezone.now()
            question.save()  # 진짜 저장
            return redirect('pybo:index')
    else:  # request.method == 'GET'
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)