from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q, Count
from ..models import Question

def index(request):
    return render(request, 'pybo/index.html')

def profile(request):
    return render(request, 'pybo/profile.html')

def board(request):
    # 질문 목록
    # 127.0.0.1:8000/pybo/board/?page=1
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')       # 검색어 전달
    so = request.GET.get('so', 'recent')   # 정렬 기본 기준

    # 정렬
    if so == 'recommend':
        question_list = Question.objects.annotate(
            num_voter=Count('voter')).order_by('-num_voter', '-create_date')  #num_voter는 임시필드
    elif so == 'popular':
        question_list = Question.objects.annotate(
            num_answer=Count('answer')).order_by('-num_answer', '-create_date')  #num_answer는 임시필드
    else:
        question_list = Question.objects.order_by('-create_date')

    # 조회
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |        # 제목 검색 *"i"contains는 대소문자 다 가능
            Q(content__icontains=kw) |        # 내용 검색
            Q(author__username__icontains=kw) |       # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw)       # 답변 글쓴이 검색
        ).distinct()  # 중복제거
    # 페이징 처리 -페이지당 10개씩 보여줌
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'page': page, 'kw': kw, 'so': so}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    #question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context ={'question' : question}
    return render(request, 'pybo/question_detail.html', context)