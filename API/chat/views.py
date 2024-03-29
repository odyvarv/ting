import json

from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound
from django.views.generic import View
from .utils import datetime_to_timestamp

from .models import Channel, Message
from .forms import MessageCreationForm


class MessageView(View):
    def post(self, request, channel_name, *args, **kwargs):
        channel = get_object_or_404(Channel, name=channel_name)

        form = MessageCreationForm(request.POST)

        if not form.is_valid():
            return HttpResponseBadRequest(str(form.errors))

        form.channel = channel
        form.save()

        return HttpResponse(status=204)

    def get(self, request, channel_name, *args, **kwargs):
        lim = request.GET.get('lim', 100)

        channel = get_object_or_404(Channel, name=channel_name)

        messages = Message.objects.values(
            'text', 'username', 'datetime'
        ).filter(channel=channel).order_by('-datetime')[:lim]

        # convert datetime to UTC epoch milliseconds
        for message in messages:
            message['datetime'] = datetime_to_timestamp(message['datetime'])

        messages_json = json.dumps(list(messages))

        return HttpResponse(messages_json, content_type='application/json')


class ChannelView(View):
    def post(self, request, *args, **kwargs):
        channel = Channel(name=request.POST['name'])
        channel.save()

        return HttpResponse(status=204)

    def get(self, request, *args, **kwargs):
        queryset = Channel.objects.values('name')
        channel = get_object_or_404(queryset, name=request.GET['name'])

        return HttpResponse(
            json.dumps(channel),
            content_type='application/json'
        )
