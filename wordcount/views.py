#from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render(request, 'homepage.html')

def result(request):
    result = request.GET['fulltext']
    #print(result)
    wordlist = result.split()
    worddict ={}
    for word in wordlist:
        if word in worddict:
            worddict[word] +=1
        else:
            worddict[word] =1
    sortedworddict = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'result.html', {'result':result, 'wordlist':len(wordlist), 'worddict':sortedworddict})