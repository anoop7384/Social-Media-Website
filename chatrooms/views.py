from django.shortcuts import render, redirect
from .models import ChatRoom, Message
from django.utils import timezone

# Create your views here.


def chatroom(request, pk):
    obj = User.objects.get(pk=pk)
    sender_room, screated = ChatRoom.objects.get_or_create(
        sender=request.user, receiver=obj)
    if (request.method == 'POST'):
        text = request.POST.get('textfield')
        receiver_room, rcreated = ChatRoom.objects.get_or_create(
            receiver=request.user, sender=obj)
        sender_message = Message.objects.create(
            sender=request.user, receiver=obj, chatroom=sender_room, content=text, timestamp=timezone.now())
        receiver_message = Message.objects.create(
            sender=request.user, receiver=obj, chatroom=receiver_room, content=text, timestamp=timezone.now())
        sender_message.save()
        receiver_message.save()

    messages = Message.objects.filter(chatroom=sender_room)
    context = {
        'title': 'Chat',
        'account': obj,
        'user': request.user,
        'messages': messages
    }
    return render(request, 'chatroom/chat.html', context)
