from django.shortcuts import render

# Create your views here.

def User_defined_filter(request):
    d={'data':'''Mahendra Singh Dhoni,commonly known as MS Dhoni, 
                is a former Indian cricketer and captain of the Indian 
                national team in limited-overs formats from 2007 to 2017 
                and in Test cricket from 2008 to 2014, who plays as a Wicket-keeper-Batsman.'''}
    
    return render(request, 'usdfilters.html', d)
