from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hey</h1>")

def topics(request, board_id):
    return HttpResponse("<h2>Board: " + str(board_id) + "</h2>")
