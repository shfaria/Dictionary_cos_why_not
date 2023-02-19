from django.shortcuts import render, redirect
from PyDictionary import PyDictionary

# dictionaryApp

def home(request):

    if request.method == 'POST':
        word = request.POST['search']
        dictionary = PyDictionary()
        meanings = dictionary.meaning(word)
        print(meanings)
        synonyms = dictionary.synonym(word)
        antonyms = dictionary.antonym(word)
        context = {
            'word': word,
            'meanings':meanings,
            'synonyms':synonyms,
            'antonoyms':antonyms
        }
        # return redirect('search')
    else:
        context = {}
    return render(request, 'dictionaryApp/home.html', context)

def search(request):
    
    word = request.GET.get('search')
    
    dictionary = PyDictionary()
    
    meanings = dictionary.meaning(word)
    
    synonyms = dictionary.synonym(word)
    antonyms = dictionary.antonym(word)
    
    context = {
            'word': word,
            'meanings':meanings,
            'synonyms':synonyms,
            'antonoyms':antonyms
        }
    return render(request, 'dictionary/search.html', context)