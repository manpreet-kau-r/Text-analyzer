## I have created this

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index1.html')

def analyse(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlinerem=request.POST.get('newlinerem','off')
    remspace=request.POST.get('remspace','off')
    charcount=request.POST.get('charcount','off')

    purpose=""
    analysed=djtext

    if removepunc=='on':

        punctuations='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        purpose+="Remove punctuations "
        temp=""

        for char in analysed:
            if char not in punctuations:
                temp+=char
        analysed=temp

    if fullcaps=='on':
        purpose+="Capitalise "
        analysed=analysed.upper()
    
    if newlinerem=='on':

        purpose+="New line remove "
        temp=""
        for char in analysed:
            if char!='\n' and char!='\r':
                temp+=char
        analysed=temp

    if remspace=='on':

        purpose+="Remove extra space "
        temp=""

        for index,char in enumerate(analysed):
            if not (analysed[index]==" " and analysed[index+1]==" "):
                temp+=char
        analysed=temp

    if charcount=='on':

        purpose+="Count character "
        analysed+="   Character count : "+ str(len(analysed))
        
    params={'purpose':purpose,'analysed_text':analysed}
    return render(request,'analyse1.html',params)



