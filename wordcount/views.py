from django.http import HttpResponse
from django.shortcuts import render
import operator
from . import urls


def index(request):
    return render(request, 'index.html')


def count(request):
    data = request.POST.get('fulltextarea', 'default')

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed = ""
    for char in data:
        if char not in punctuations:
            analyzed = analyzed + char

    word_list = analyzed.split()
    list_length = len(word_list)

    worddictionary = {}
    for word in word_list:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    sorted_list = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    params = {'fulltext': data, 'words': list_length, 'Worddictionary': sorted_list}
    return render(request, 'count.html', params)
