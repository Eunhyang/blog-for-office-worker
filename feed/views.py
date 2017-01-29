from django.shortcuts import render
from .models import Article, Comment, HashTag
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    category = request.GET.get("category")
    hashtag = request.GET.get("hashtag")

    hashtag_list = HashTag.objects.all()

    if not hashtag and not category:
        article_list = Article.objects.all()
    elif category:
        article_list = Article.objects.filter(category = category)
    else :
        article_list = Article.objects.filter(hashtag__name = hashtag)

    category_list = set([
        (article.category, article.get_category_display())
        for article in article_list
    ])

    ctx = {
        "article_list" : article_list,
        "hashtag_list" : hashtag_list,
        "category_list" : category_list,
    }
    return render(request, "index.html", ctx)

def detail(request, article_id):

    article = Article.objects.get(id = article_id)
    hashtag_list = HashTag.objects.all()
    ctx = {
        "article" : article,
        "hashtag_list" : hashtag_list,
    }

    # if request.method == 'GET' :
    #     pass

    if request.method == 'POST' :
        username = request.POST.get('username')
        comment = request.POST.get('comment')
        Comment.objects.create(
            article = article,
            username = username,
            comment = comment
        )
        return HttpResponseRedirect('/{}/'.format(article_id))

    return render(request, "detail.html", ctx)
# def about(request):
#     pass
