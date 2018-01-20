from django.http import Http404
from django.shortcuts import render
from .models import Board, Topic, Msg
from django.contrib.auth.models import User

def index(request):
    board_list = Board.objects.all()

    return render(request, 'msgboard/index.html', {
        'board_list': board_list, 
    })

class TopicView(Topic):
    username = ''

def topics(request, board_id):
    try:
        board = Board.objects.get(pk=board_id)
        topic_list = Topic.objects.filter(boardId=board_id)

        topic_list_view = []
        i = 0
        for topic in topic_list:
            topic_list_view.append(TopicView(topic_list[i]))
            topic_list_view[i] = topic
            topic_list_view[i].username = topic.userId # not sure why this works... but it does i guess?
            i+=1

    except Board.DoesNotExist:
        raise Http404("Board doesn't exist")
        
    return render(request, 'msgboard/topics.html', {
        'board':board,
        'topic_list': topic_list_view,
})
