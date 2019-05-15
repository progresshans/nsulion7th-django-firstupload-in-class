from django.shortcuts import render, redirect, get_object_or_404
from .models import Board

# Create your views here.
def index(request):
    boards = Board.objects
    return render(request, 'index.html', {'boards' : boards})

def new(request):
    return render(request, 'new.html')
    
def create(request):
    board = Board()
    board.title = request.GET['title']
    board.text = request.GET['content']
    board.save()
    return redirect('/')
    
def read(request, board_id):
    read = get_object_or_404(Board, pk=board_id)
    return render(request, 'read.html', {'read':read})
    
def delete(request, board_id):
    board_target = Board.objects.get(id=board_id)
    board_target.delete()
    return redirect('/')
    
def edit(request, board_id):
    board_target = Board.objects.get(id=board_id)
    return render(request, 'edit.html', {'board_target':board_target})
    
def update(request, board_id):
    board = Board.objects.get(id=board_id)
    board.title = request.GET['title']
    board.text = request.GET['content']
    board.save()
    return redirect('/')