from django.shortcuts import render

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
},
{

'id':4,
'title': 'Article 4',
'content':'Nullam arcu massa molestie eget porttitor sed congue vel nibh. Aenean commodo eros vitae pharetra elementum.'
},
{

'id':5,
'title': 'Article 5',
'content':'Nullam arcu massa molestie eget porttitor sed congue vel nibh. Aenean commodo eros vitae pharetra elementum.'
},
{
'id':6,
'title': 'Article 6',
'content':'Nullam arcu massa molestie eget porttitor sed congue vel nibh. Aenean commodo eros vitae pharetra elementum.'
},
{

'id':7,
'title': 'Article 7',
'content':'Nullam arcu massa molestie eget porttitor sed congue vel nibh. Aenean commodo eros vitae pharetra elementum.'
},
{

'id':8,
'title': 'Article 8',
'content':'Nullam arcu massa molestie eget porttitor sed congue vel nibh. Aenean commodo eros vitae pharetra elementum.'
}
]
def home (request):
    context= {
    'articles' : articles
    }
    return render(request,"home.html",context=context)
def article (request,article_id):


    context = {
    'article': articles[article_id-1]
    }
    return render(request,"article.html",context=context)
