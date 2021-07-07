from django.shortcuts import HttpResponse, render
from .models import Coffee
from .forms import CoffeeForm


# Create your views here.
def index(request):
    # return HttpResponse("<h1>Hellow world!</h1>")  # Http에 응답을 줄 수 있는 함수 사용
    # 어느 경로로 들어왔을 때 index 함수를 실행하는지 설정해주는 부분은 ../webproj/urls.py에 관리

    nums = [1,2,3,4,5]

    return render(request, 'index.html', {"my_list": nums})
'''
def coffee_view(request):
    # .all(), .get(), .filter(), ... 사용 가능
    coffee_all = Coffee.objects.all()  # = SELECT * FROM Coffee
    form = CoffeeForm()

    return render(request, 'coffee.html', {"coffee_list" : coffee_all, "coffee_form" : form})
'''

def coffee_view(request):
    coffee_all = Coffee.objects.all() 
    # 만약 request가 POST라면:
        # POST를 바탕으로 Form을 완성하고
        # Form이 유효하면 -> 저장

    if request.method == "POST":
        form = CoffeeForm(request.POST)  # 완성된 Form. 양식이 채워진 Form
        if form.is_valid():  # 채워진 Form이 유효하다면:
            form.save()  # 이 Form 내용을 Model에 저장

    form = CoffeeForm()
    return render(request, 'coffee.html', {"coffee_list" : coffee_all, "coffee_form" : form})