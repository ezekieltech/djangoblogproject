from django.shortcuts import render

# Create your views here.
# Render takes the request parameter first,
#then the template to render,
#then an optional dictionary of variables to pass through to the template.
def index(request):
    return render(request, 'personal/home.html')


#Here, we're rendering the template, and also passing a dictionary.
#We can then reference 'content' within our template by referencing {{ content }}
def contact(request):
    return render(request, 'personal/basic.html',{'content':['If you would like to contact me, please email me.','hskinsley@gmail.com']})
