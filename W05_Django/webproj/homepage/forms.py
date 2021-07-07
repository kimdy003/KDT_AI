from django import forms
from .models import Coffee  # Model 호출


class CoffeeForm(forms.ModelForm):  # ModelForm을 상속받는 CoffeeForm 생성
    # form을 만들기 위해 어떤 클래스를 사용하는지 지정해주는 class meta
    class Meta:
        model = Coffee
        fields = ('name', 'price', 'is_ice')
