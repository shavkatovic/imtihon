from django.shortcuts import render, redirect
from django.urls import reverse
from apps import forms
from apps.models import User, Service, Blog, Skill, Comment, Portfolio
from config.settings import TELEGRAM_BOT_TOKEN
from httpx import post, get
from django.views.generic import DetailView, TemplateView
from django.views import View

def send_message(chat_id, message):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    params = {
        'chat_id': chat_id,
        'text': message
    }
    response = get(url, params=params)
    print(response.text, response.status_code)


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.kwargs.get('pk')
        context['user'] = User.objects.filter(id=user_id).first()
        context['servis'] = Service.objects.filter(user_id=user_id).all()
        context['blog'] = Blog.objects.filter(user_id=user_id).all()
        context['skill'] = Skill.objects.filter(user_id=user_id).all()
        context['port'] = Portfolio.objects.filter(user_id=user_id).all()
        return context

class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = 'portfolio.html'
    context_object_name = 'port'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        portfolio = self.object
        user = portfolio.user
        context['user'] = user
        return context

def blog(request, pk):
    bloga = Blog.objects.filter(id=pk).first()
    data = User.objects.filter(id=bloga.user_id_id).first()
    c_view = Comment.objects.filter(post_id__id=pk).all()
    if request.POST:
        comment = forms.CommentsForm(request.POST)
        if comment.is_valid():
            comment.save()
        return redirect(reverse('blog', args=(bloga.pk,)))
    return render(request, 'blog.html', {'user': data, 'blog': bloga, 'c_view': c_view})


class SignUpView(View):
    def get(self, request):
        return render(request, 'signup.html')
    
    def post(self, request):
        data = forms.UserModelForm(request.POST, files=request.FILES)
        if data.is_valid():
            data.save()
            return redirect(reverse('login'))
        return render(request, 'signup.html')


def login(request):
    data = request.POST
    if request.POST:
        username = data.get('username')
        password = data.get('password')
        a = User.objects.filter(username=username, password=password).first()
        if a:
            return redirect(reverse('index', args=(a.pk,)))
    return render(request, 'login.html')


class UpdateServisView(View):
    def get(self, request, pk):
        a = User.objects.filter(id=pk).first()
        return render(request, 'update_servis.html', {'user': a})
    
    def post(self, request, pk):
        data = request.POST
        a = User.objects.filter(id=pk).first()
        if data:
            user_id = data.get('user_id')
            s = forms.ServisModelForm(data)
            if s.is_valid():
                s.save()
                return redirect(reverse('index', args=(a.pk,)))
        return render(request, 'update_servis.html', {'user': a})


class UpdateAnketaView(View):
    def get(self, request, pk):
        a = User.objects.filter(id=pk).first()
        return render(request, 'update_anketa.html', {'user': a})
    
    def post(self, request, pk):
        a = User.objects.filter(id=pk).first()
        if request.POST:
            data = forms.UserUpdateForm(request.POST, instance=a)
            if data.is_valid():
                data.save()
                return redirect(reverse('index', args=(a.pk,)))
        return render(request, 'update_anketa.html', {'user': a})







class UpdateBlogView(View):
    def get(self, request, pk):
        a = User.objects.filter(id=pk).first()
        return render(request, 'update_blog.html', {'user': a})
    
    def post(self, request, pk):
        a = User.objects.filter(id=pk).first()
        if request.POST:
            data = forms.BlogModelForm(request.POST, request.FILES)
            if data.is_valid():
                data.save()
                return redirect(reverse('index', args=(a.pk,)))
        return render(request, 'update_blog.html', {'user': a})

# @login_required
class UpdateSkillView(View):
    def get(self, request, pk):
        a = User.objects.filter(id=pk).first()
        return render(request, 'update_skill.html', {'user': a})
    
    def post(self, request, pk):
        a = User.objects.filter(id=pk).first()
        if request.POST:
            data = forms.AddSkillForm(request.POST)
            if data.is_valid():
                skill = data.save(commit=False)
                skill.user = a
                skill.save()
                return redirect(reverse('index', args=(a.pk,)))
        return render(request, 'update_skill.html', {'user': a})

class UpdatePortfolioView(View):
    def get(self, request, pk):
        a = User.objects.filter(id=pk).first()
        return render(request, 'update_portfolio.html', {'user': a})
    
    def post(self, request, pk):
        a = User.objects.filter(id=pk).first()
        if request.POST:
            data = forms.PortfolioModelForm(request.POST, request.FILES)
            if data.is_valid():
                portfolio = data.save(commit=False)
                portfolio.user = a
                portfolio.save()
                return redirect(reverse('index', args=(a.pk,)))
        return render(request, 'update_portfolio.html', {'user': a})

def contact_form(request, pk):
    data = request.POST
    a = User.objects.filter(id=pk).first()
    if data:
        form = forms.ContactForm(data)
        if form.is_valid():
            data = form.cleaned_data
            m = f'''📥 New mail\n📩 From: {data['email']}\n👱 Name: {data['name']}\n📄 Message: {data['message']}'''
            send_message(1038185913, m)
        # return redirect(reverse(''))
    return render(request, 'index.html', {'user': a})
