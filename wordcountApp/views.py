from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def result(request):
    text = request.GET['TextInput']
    words = text.split()
    counted_words = {}

    for word in words:
        if word in counted_words:
            counted_words[word] += 1
        else:
            counted_words[word] = 1

    return render(request, "result.html",
                  {'FullText': text, 'FullWords': len(words), 'CountWords': counted_words.items()})
