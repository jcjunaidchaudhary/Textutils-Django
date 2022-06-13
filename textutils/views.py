from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.GET.get('text','default')

    removepunc= request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    charcount=request.GET.get('charcount','off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Change Uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif newlineremover=="on":
        analyzed=""
        for char in djtext:
            if char !='\n':
                analyzed=analyzed+char
        params = {'purpose': 'Remove new line', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif extraspaceremover=="on":
        analyzed=""
        for index,char in enumerate(djtext):
            if not (djtext[index]==' ' and djtext[index+1]==' '):
                analyzed=analyzed+char
        params = {'purpose': 'Remove space', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif charcount == "on":
        total=0
        for char in djtext:
            if char != " ":
                total+=1
        sum=(f"number of characters is {total}")
        params = {'purpose': 'Count Characters', 'analyzed_text': sum}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse('Error')

# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("capitalize first")
#
#
# def spaceremove(request):
#     return HttpResponse("space remover <a href='/'>back</a>")
#
# def charcount(request):
#     return HttpResponse("charcount ")