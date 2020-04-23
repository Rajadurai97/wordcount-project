import operator

from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request,'home.html')
    #return HttpResponse('Hello')

def about(request):
    return render(request,'about.html')

#def eggs(request):
#    return HttpResponse('<h1>Eggs are great!</h1>')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()
    worddict={}

    for word in wordlist:
        if word in worddict:
            worddict[word] += 1
            #Increase
        else:
            #Add to the dictionary
            worddict[word] = 1

    sortedwords = sorted(worddict.items(), key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'fulltext':fulltext,'Counts':len(wordlist),'Sortedwords':sortedwords})
