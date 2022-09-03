from django.shortcuts import render
from django.http import HttpResponse
from articles.models import Article
# Create your views here.

def home_view(request):
    articles = list(map(lambda x: (x.title, x.content), Article.objects.get_queryset()))
    tags = list(map(lambda x: f'<hr><h2>{x[0]}</h2><p>{x[1]}</p>', articles))
    html = f"""<h1>Articles:</h1>
            {''.join(tags)}
            """
    return HttpResponse(html)
