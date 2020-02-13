from django.shortcuts import render
from django.http import HttpResponse
from .models import News
from .forms import GetNewsForm
import requests

# Create your views here.

class HomeView():
    def home(request):
        print("Logging message", flush=True)
        all_news = News.objects.all().order_by('-published_at')[:20]
        context = {
            'all_news': all_news,
            'len': len(all_news)
        }
        return render(request, 'news_list/home.html', context)

class GetNewsView():
    articles = []
    def get_news(request):
        message = False
        if request.method == 'GET':
            if 'request' in request.GET:
                form = GetNewsForm(request.GET)
                if form.is_valid():
                    api_key = form.cleaned_data['api_key']
                    source = 'bbc-news'
                    sort_by = 'latest'
                    print([api_key])
                    if api_key != '':
                        url = 'https://newsapi.org/v1/articles?source=%s&sortBy=%s&apiKey=%s'%\
                            (source, sort_by, api_key)
                        try:
                            response = requests.get(url)
                            articles_tmp = response.json()['articles']
                            for art in articles_tmp:
                                GetNewsView.articles.append({
                                    'author': art['author'],
                                    'title': art['title'],
                                    'description': art['description'],
                                    'url': art['url'],
                                    'image_url': art['urlToImage'],
                                    'published_at': art['publishedAt']
                                })
                            message = False
                        except Exception as err:
                            GetNewsView.articles = []
                            message = 'API Key you entered was wrong! Please try again'

            elif 'save' in request.GET:
                for art in GetNewsView.articles:
                    flg = News.objects.filter(title=art['title'], description=art['description']).exists()
                    if not flg:
                        news = News(
                            author = art['author'],
                            title = art['title'],
                            description = art['description'],
                            url = art['url'],
                            image_url = art['image_url'],
                            published_at = art['published_at']
                        )
                        news.save()
                GetNewsView.articles = []

        all_news = GetNewsView.articles
        form = GetNewsForm()
        context = {
            'all_news': all_news,
            'form': form,
            'message': message
        }
        return render(request, 'news_list/get_news.html', context)

class HelpView():
    def help_(request):
        return render(request, 'news_list/help.html')