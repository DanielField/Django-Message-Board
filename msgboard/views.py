from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import Board, Topic, Msg
from django.contrib.auth.models import User

def index(request):
    board_list = Board.objects.all()

    return render(request, 'msgboard/index.html', {
        'board_list': board_list, 
    })

# Not proud of this code
class TopicView(Topic):
    username = ''
class MsgView(Msg):
    username = ''

def topics(request, board_id):
    try:
        board = Board.objects.get(pk=board_id)
        topic_list = Topic.objects.filter(board=board_id)

        # not sure why this works... but it does i guess?
        topic_list_view = []
        i = 0
        for topic in topic_list:
            topic_list_view.append(TopicView(topic_list[i]))
            topic_list_view[i] = topic
            topic_list_view[i].username = topic.user 
            i+=1
        #################################################

    except Board.DoesNotExist:
        raise Http404("Board doesn't exist")
        
    return render(request, 'msgboard/topics.html', {
        'board':board,
        'topic_list': topic_list,
    })

def add_topic(request, board_id):
    current_board = get_object_or_404(Board, pk=board_id)
    try:
        title = request.POST['topic_title']
        msg = request.POST['initial_msg']
    except:
        return render(request, 'msgboard/oops.html')
    else:
        topic = Topic(name=title, board=current_board, user=request.user, isLocked=False)
        topic.save()
        msg = Msg(user=request.user, Topic=topic, text=msg)
        msg.save()

        return redirect('msgboard:topics', board_id)

def messages(request, board_id, topic_id):
    try:
        board = Board.objects.get(pk=board_id)
        topic = Topic.objects.get(pk=topic_id)
        msg_list = Msg.objects.filter(Topic=topic_id)

        # not sure why this works... but it does i guess?
        msg_list_view = []
        i = 0
        for msg in msg_list:
            msg_list_view.append(MsgView(msg_list[i]))
            msg_list_view[i] = msg
            msg_list_view[i].username = msg.user
            i+=1
        #################################################

    except Msg.DoesNotExist:
        return render(request, 'msgboard/oops.html')
        
    return render(request, 'msgboard/messages.html', {
        'board':board,
        'msg_list': msg_list_view,
        'topic': topic,
})

def add_msg(request, board_id, topic_id):
    current_topic = get_object_or_404(Topic, pk=topic_id)
    try:
        reply = request.POST['reply']
    except:
        return render(request, 'msgboard/oops.html')
    else:
        msg = Msg(user=request.user, Topic=current_topic, text=reply)
        msg.save()

        return redirect('msgboard:messages', board_id, topic_id)