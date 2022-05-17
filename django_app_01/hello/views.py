from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import HelloForm
import openpyxl

wb = openpyxl.load_workbook('energy.xlsx')
type(wb)

sheet = wb.get_sheet_by_name('Sheet1')
nutrient = tuple(sheet['F5':'BE5'])
food_name = tuple(sheet['D8':'D2198'])
food_data = tuple(sheet['F8':'BE2198'])
result = [256]
class HelloView(TemplateView):
    
    def __init__(self):
        self.params = {
            'title':'食材を選ぶことで栄養素を計算します',
            'food_name':food_name,
            'food_data':food_data,
            'nutrient':nutrient,
            'result':result,
            'form':HelloForm()
            }
        
    def get(self,request):
        return render(request,'hello/index.html',self.params)
    
    def post(self,request):
        check= request.POST["food"]
        for i in range(food_name):
            if food_name(i) == check:
               result[i] += food_data[i]
        return render(request, 'hello/index.html',self.params)



