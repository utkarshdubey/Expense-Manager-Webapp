from django.shortcuts import render
from .models import ExpenseList
from django.db.models import Sum
from django.http import HttpResponseRedirect


def Index(request):
    lists = ExpenseList.objects.all()
    total = ExpenseList.objects.all().aggregate(Sum('amount'))
    if not lists:
        total = "0"
    return render(request, 'index.html', {'lists': lists, 'total': total})

def addItem(request):
    new_item = ExpenseList(amount = request.POST['amount'], title = request.POST['title'])
    new_item.save()
    return HttpResponseRedirect('/app/')

def deleteItem(request, item):
    to_delete = ExpenseList.objects.get(id=item)
    to_delete.delete()
    return HttpResponseRedirect('/app/')
