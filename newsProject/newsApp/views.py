from django.shortcuts import render

# Create your views here.

def moviesInfo(request):
    my_dict ={
        "head_msg": "Movies Information",
        "sub_msg1": "Sonali slowly getting cured",
        "sub_msg2": "Bahubali-3 is just planning",
        "sub_msg3": "Salman Khan ready to marriage",
        "photo": "images/sunny.jpg"
    }
    return render(request, 'newsApp/news.html', context=my_dict)

def sportsInfo(request):
    my_dict ={
        "head_msg": "Sports Information",
        "sub_msg1": "Anushka Sharma Firing Like anything",
        "sub_msg2": "Kohli updating in game anything can happened",
        "sub_msg3": "Worst Performance by India-Sehwag",
    }
    return render(request, 'newsApp/news.html', context=my_dict)

def politicsInfo(request):
    my_dict ={
        "head_msg": "Politics Information",
        "sub_msg1": "Achhce Din Aaa gye",
        "sub_msg2": "Rupee Balue now 1$: 85Rs",
        "sub_msg3": "In India Single Paisa Black mony No more",
    }
    return render(request, 'newsApp/news.html', context=my_dict)

def index(request):
    return render(request, 'newsApp/index.html')