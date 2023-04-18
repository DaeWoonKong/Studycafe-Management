from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import Seat
from .forms import SeatForm
from django.utils import timezone

def index(request):
    """
    sales 목록 출력
    """
    # 입력 인자
    page = request.GET.get('page', 1)  # 페이지

    # 조회
    seat_list = Seat.objects.order_by('scode')

    # 페이징 처리
    paginator = Paginator(seat_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'seat_list': page_obj}
    return render(request, 'sales/seat_list.html', context)

def detail(request, seat_id):
    """
    sales 내용 출력
    """
    seat = get_object_or_404(Seat, pk=seat_id)
    context = {'seat': seat}
    return render(request, 'sales/seat_detail.html', context)

@login_required(login_url='common:login')
def seat_create(request):
    """
    sales 제품 등록
    """
    if request.method == 'POST':
        form = SeatForm(request.POST, request.FILES)
        if form.is_valid():
            seat = form.save(commit=False)
            seat.save()
            return redirect('sales:index')
    else:
        form = SeatForm()
    context = {'form': form}
    return render(request, 'sales/seat_form.html', context)

@login_required(login_url='common:login')
def seat_modify(request, seat_id):
    """
    sales 질문 수정
    """
    seat = get_object_or_404(Seat, pk=seat_id)
    if request.user != seat.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('sales:detail', seat_id=seat.id)

    if request.method == "POST":
        form = SeatForm(request.POST, instance=seat)
        if form.is_valid():
            seat = form.save(commit=False)
            seat.author = request.user
            seat.modify_date = timezone.now()  # 수정일시 저장
            seat.save()
            return redirect('sales:detail', seat_id=seat.id)
    else:
        form = SeatForm(instance=seat)
    context = {'form': form}
    return render(request, 'sales/seat_form.html', context)

@login_required(login_url='common:login')
def seat_delete(request, seat_id):
    """
    sales 질문 삭제
    """
    seat = get_object_or_404(Seat, pk=seat_id)
    if request.user != seat.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('sales:detail', seat_id=seat.id)
    seat.delete()
    return redirect('sales:index')