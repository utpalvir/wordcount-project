from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request, 'home.html')
def aboutme(request):
    return render(request,'aboutme.html')
def eggs(request):
    return HttpResponse("Eggs are great")
def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddictionary={}
    sorted
    for word in wordlist:
        if word in worddictionary:
            #increase the count of the word
            worddictionary[word]+=1
        else:
            worddictionary[word]=1

    sortedWords = sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)
    return render(request, 'count.html',{'fulltext':fulltext,'count':len(wordlist),'worddictionary':worddictionary.items(),'sortedWords':sortedWords})