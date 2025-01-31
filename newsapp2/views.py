from django.shortcuts import render,redirect
from django.urls import reverse
from django.views.generic.edit import FormMixin
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic import FormView
from .forms import ContactForm
from .models import NewsPost, Comment
from .forms import SearchForm
from.forms import CommentForm
from django.views.generic import UpdateView
from django.db.models import Q
from django.core.mail import EmailMessage
from django.contrib import messages
from django.urls import reverse_lazy

# Create your views here.
class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'orderby_records'
    queryset = NewsPost.objects.order_by('-posted_at')
    paginate_by=10
class NewsDetailView(FormMixin, DetailView):
    template_name = 'news_detail.html'
    model = NewsPost
    form_class = CommentForm
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['comments'] = post.comments.all().order_by('-created_at')
        context['comment_form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.get_object()
        comment.user = self.request.user
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('newsapp2:news_detail', kwargs={'pk': self.object.pk})
class SkinCareView(TemplateView):
    template_name = 'skincare.html'

class CoordinationListView(ListView):
    template_name = 'coordination_list.html'
    model = NewsPost
    context_object_name = 'coordination_records'
    queryset = NewsPost.objects.filter(category='今日のコーデ').order_by('-posted_at')
    paginate_by=10

class HorrorListView(ListView):
    template_name = 'horror_list.html'
    model = NewsPost
    context_object_name = 'horror_records'
    queryset = NewsPost.objects.filter(category='怖い話').order_by('-posted_at')
    paginate_by=10

class LifehackListView(ListView):
    template_name = 'lifehack_list.html'
    model = NewsPost
    context_object_name = 'lifehack_records'
    queryset = NewsPost.objects.filter(category='ライフハック').order_by('-posted_at')
    paginate_by=10

class SkinCareListView(ListView):
    template_name = 'skincare_list.html'
    model = NewsPost
    context_object_name = 'skincare_records'
    queryset = NewsPost.objects.filter(category='スキンケア・コスメ').order_by('-posted_at')
    paginate_by=10

class SweetsListView(ListView):
    template_name = 'sweets_list.html'
    model = NewsPost
    context_object_name = 'sweets_records'
    queryset = NewsPost.objects.filter(category='人気のスイーツ').order_by('-posted_at')
    paginate_by=10

class ZooListView(ListView):
    template_name = 'zoo_list.html'
    model = NewsPost
    context_object_name = 'zoo_records'
    queryset = NewsPost.objects.filter(category='可愛い動物').order_by('-posted_at')
    paginate_by=10

class SearchResultsView(ListView):
    model = NewsPost
    template_name = 'search_results.html'
    context_object_name = 'results'

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            return NewsPost.objects.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            )
        return NewsPost.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchForm(self.request.GET)
        return context

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('newsapp2:contact')

    def form_valid(self, form):
        name=form.cleaned_data['name']
        email=form.cleaned_data['email']
        title=form.cleaned_data['title']
        message=form.cleaned_data['message']
        subject = 'お問い合わせ : {}'.format(title)
        message = \
        '送信者名 : {0}\nメールアドレス : {1}\n タイトル : {2}\n メッセージ : {3}'.format(name,email,title,message)
        from_email = 'fko2447057@stu.o-hara.ac.jp'
        to_list = ['fko2447057@stu.o-hara.ac.jp']
        message=EmailMessage(subject=subject,
                            body=message,
                            from_email=from_email,
                            to=to_list,
                            )
        message.send()
        messages.success(
            self.request,'お問い合わせメールは正常に送信されました！')
        return super().form_valid(form)