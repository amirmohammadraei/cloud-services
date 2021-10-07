from django.views.generic import FormView
from .forms import *
import requests
import json
from core.models import Comment
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages



def check_toxic_comment(message):
    url = 'http://max-toxic-comment-classifier.codait-prod-41208c73af8fca213512856c7a09db52-0000.us-east.containers.appdomain.cloud/model/predict'
    headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
    data = {}
    data['text'] = [f'{message}']
    response = requests.post(url, headers=headers, data=json.dumps(data)).json()['results'][0]['predictions']['toxic']
    return response


class IndexView(FormView):
    template_name = "index.html"
    form_class = CommentForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            username = request.POST.get('username')
            comment = request.POST.get('comment')
            photo = request.POST.get('photo')
            response = check_toxic_comment(comment)
            is_toxic = True if response > 0.5 else False
            Comment.objects.create(username=username, comment=comment, photo=photo, is_toxic=is_toxic)
            messages.error(self.request, 'Sorry, Your message is toxic!') if is_toxic is True else messages.success(self.request, 'Your message will be added to the post.')
            return redirect(reverse('index'))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photo1'] = Comment.objects.filter(is_toxic=False, photo=1)
        context['photo2'] = Comment.objects.filter(is_toxic=False, photo=2)
        context['photo3'] = Comment.objects.filter(is_toxic=False, photo=3)
        context['photo4'] = Comment.objects.filter(is_toxic=False, photo=4)
        context['photo5'] = Comment.objects.filter(is_toxic=False, photo=5)
        return context
                