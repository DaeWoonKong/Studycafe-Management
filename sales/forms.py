from django import forms
from sales.models import Seat


class SeatForm(forms.ModelForm):
    class Meta:
        model = Seat
        fields = ['scode', 'scondition', 'unitprice', 'discountrate', 'imgfile']
        labels = {
            'scode': '좌석코드', 'scondition': '좌석상태', 'unitprice': '시간당 대여료', 'discountrate': '할인율', 'imgfile': '이미지'
        }
        # widget 항목 삭제