from django.shortcuts import render


def home (request):
    return render(request,"home.html")
def article (request,article_id):

    articles =[
    {

    'id':1,
    'title': 'Article 1',
    'content':'Lorem ipsum dolor sit amet consectetur adipiscing elit. Praesent mauris lacus laoreet id dolor id sollicitudin laoreet tortor. Aliquam non lorem sit amet odio placerat aliquet.'
    },
    {

    'id':2,
    'title': 'Article 2',
    'content':'Donec dictum metus in malesuada aliquam purus nisi sodales nisl quis congue orci ipsum ut nulla. Vestibulum ac enim commodo aliquam sapien sit amet egestas lectus. Phasellus consequat velit libero'
    },
    {

    'id':3,
    'title': 'Article 3',
    'content':'Nullam arcu massa molestie eget porttitor sed congue vel nibh. Aenean commodo eros vitae pharetra elementum.'
    }]
    context = {
    'article': articles[article_id-1]
    }
    return render(request,"article.html",context=context)
