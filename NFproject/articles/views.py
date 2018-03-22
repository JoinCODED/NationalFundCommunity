from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import PermissionDenied
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from .models import Article, Category, Comments
from .forms import ArticleForm, CommentsForm
from django.db.models import Q
from django.http import JsonResponse ,HttpResponseRedirect
from django.views.generic import (ListView,
                                  CreateView,
                                  DetailView,
                                  UpdateView,
                                  DeleteView)
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        UserPassesTestMixin)

from urllib.parse import quote


# def add(request):
#     if request.user.is_authenticated:
#         if request.method == "POST":
#             form = ArticleForm(request.POST, request.FILES)
#             if form.is_valid():
#                 new_article = form.save()
#                 new_article.author = request.user
#                 new_article.save()
#                 return redirect(new_article)
#         form = ArticleForm()
#         context = {"form": form}
#         return render(request, "add_article.html", context)
#     else:
#         raise PermissionDenied

class AddArticle (LoginRequiredMixin,CreateView):
    model = Article
    form_class = ArticleForm

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# def add_comment(request,article_slug):
#     if request.user.is_authenticated:
#         if request.method == "POST":
#             _article =Article.objects.get(slug=article_slug)
#             form = CommentsForm(request.POST, request.FILES)
#             if form.is_valid():
#                 new_comment = form.save()
#                 new_comment.user = request.user
#                 new_comment.article = _article
#                 new_comment.save()
#                 return HttpResponseRedirect('')
#         # form = CommentsForm()
#         # context = {"form": form}
#         # return render(request, "home.html", context)
#     else:
#         raise PermissionDenied

# def update(request, article_slug):
#     article = Article.objects.get(slug=article_slug)
#     if article.author == request.user:
#
#         if request.method == 'POST':
#             form = ArticleForm(request.POST, request.FILES, instance=article)
#             if form.is_valid():
#                 form.save()
#                 return redirect(article)
#         else:
#             form = ArticleForm(instance=article)
#             context = {
#                 "article": article,
#                 "form": form
#             }
#             return render(request, "update_article.html", context)
#     else:
#         raise PermissionDenied


class UpdateArticle(UserPassesTestMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    raise_exception = True

    def test_func(self):
        return self.request.user == self.get_object().author


class DeleteArticle(UserPassesTestMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('articles:index')
    raise_exception = True

    def test_func(self):
        return self.request.user == self.get_object().author


class ArticleView(ListView):
    model = Article
    context_object_name = 'articles'

    def get_queryset(self):
        article_list = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            article_list = article_list.filter(Q(title__icontains=query) |
                                         Q(content__icontains=query) |
                                         Q(author_name__icontains=query)).distinct()
        return article_list



def article(request, article_slug):
    _article = get_object_or_404(Article, slug=article_slug)
    context = {}
    context['showUpdateBtn'] = _article.author == request.user
    context['article'] = _article
    is_fan = request.user in _article.fans.all()
    context['is_fan'] = is_fan
    context['article_categories'] = _article.category.all()
    context["share_string"]= quote(_article.title)

    if request.method == "POST":
        if request.user.is_authenticated:
            form = CommentsForm(request.POST, request.FILES)
            if form.is_valid():
                new_comment = form.save(commit=False)
                new_comment.user = request.user
                new_comment.article = _article
                new_comment.save()
                return redirect('articles:article',article_slug)
        else:
            return redirect('login')
    form = CommentsForm()
    context["form"]= form

    context['comments'] = _article.comments_set.all().order_by('-date')

    return render(request, "article.html", context=context)

def comment(request,article_slug):
    _article = get_object_or_404(Article, slug=article_slug)
    data = dict()
    if request.method == "POST":
        if request.user.is_authenticated:
            data['is_authenticated'] = True
            form = CommentsForm(request.POST)
            
            if form.is_valid():
               
                new_comment = form.save(commit=False)
                new_comment.user = request.user
                new_comment.article = _article
                new_comment.save()
                data['form_is_valid'] = True
                comments = _article.comments_set.all().order_by('-date')
                data['html_comment_list'] = render_to_string('show_comments.html', {
                'comments': comments
            })
            else:
                data['form_is_valid'] = False
        else:
            data['is_authenticated'] = False
        return JsonResponse(data)

# class ArticleDetail(DetailView):
#     model = Article
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         _article = context.get('article')
#         context['showUpdateBtn'] = _article.author == self.request.user
#         is_fan = self.request.user in _article.fans.all()
#         context['is_fan'] = is_fan
#         context['article_categories'] = _article.category.all()
#         context["share_string"]= quote(_article.title)
#         form = CommentsForm()
#         context['form']=form
#         return context


def favorite(request, article_slug):
    data = dict()
    data['is_authenticated'] = True
    if not request.user.is_authenticated:
        data['is_authenticated'] = False
        return redirect('login')
    _article = get_object_or_404(Article, slug=article_slug)
    if request.user in _article.fans.all():
        _article.fans.remove(request.user)
    else:
        _article.fans.add(request.user)
    data['fans_number'] = _article.fans_number
    return JsonResponse(data)


def category(request, category_slug):
    _category = get_object_or_404(Category, slug=category_slug)
    context = {}
    context['category'] = _category
    context['categoriesOfArticles'] = _category.categoriesOfArticles.all()
    return render(request, 'category.html', context=context)
