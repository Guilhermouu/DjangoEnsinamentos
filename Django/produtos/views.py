from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def ver_produto(request):
 if request.method =="GET":
    return render(request, 'ver_produto.html', {'nome':'caio'})
 elif request.method == "POST":
    return HttpResponse('MUITO FODA')
def inserir_produto(request):
    return HttpResponse("produto")