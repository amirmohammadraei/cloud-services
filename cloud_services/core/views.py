from django.views.generic import FormView
from .forms import *
import requests
import json
from core.models import Comment
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from django.conf import settings
import environ


env = environ.Env()
environ.Env.read_env(os.path.join(settings.BASE_DIR, '.env'))


api_key_text_to_speech = env('API_KEY_TEXT_TO_SPEECH')
url_text_to_speech = env('URL_TEXT_TO_SPEECH')


def check_toxic_comment(message):
    url = 'http://max-toxic-comment-classifier.codait-prod-41208c73af8fca213512856c7a09db52-0000.us-east.containers.appdomain.cloud/model/predict'
    headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
    data = {}
    data['text'] = [f'{message}']
    response = requests.post(url, headers=headers, data=json.dumps(data)).json()['results'][0]['predictions']['toxic']
    return response


def text_to_speech1(text, filename):
    authenticator = IAMAuthenticator(api_key_text_to_speech)
    text_to_speech = TextToSpeechV1(authenticator=authenticator)

    text_to_speech.set_service_url(url_text_to_speech)

    with open(f'{os.path.abspath(os.path.dirname(__file__))}/static/media/{filename}.mp3', 'wb') as audio_file:
        audio_file.write(text_to_speech.synthesize(text, voice='en-US_AllisonV3Voice',accept='audio/mpeg').get_result().content)


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
            comment_obj = Comment.objects.create(username=username, comment=comment, photo=photo, is_toxic=is_toxic)
            if is_toxic is False:
                audio_name = f'{comment_obj.id}-photo{photo}'
                text_to_speech1(comment, audio_name)
                comment_obj.music = f'{audio_name}.mp3'
                comment_obj.save()
            messages.error(self.request, 'Sorry, Your message is toxic!') if is_toxic is True else messages.success(self.request, 'Your message will be added to the post.')
            return redirect(reverse('index'))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photo1'] = Comment.objects.filter(is_toxic=False, photo=1)
        context['story1'] = Story.objects.filter(photo=1)
        context['photo2'] = Comment.objects.filter(is_toxic=False, photo=2)
        context['story2'] = Story.objects.filter(photo=2)
        context['photo3'] = Comment.objects.filter(is_toxic=False, photo=3)
        context['story3'] = Story.objects.filter(photo=3)
        context['photo4'] = Comment.objects.filter(is_toxic=False, photo=4)
        context['story4'] = Story.objects.filter(photo=4)
        context['photo5'] = Comment.objects.filter(is_toxic=False, photo=5)
        context['story5'] = Story.objects.filter(photo=5)
        return context
