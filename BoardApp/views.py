from django.db.models import Count, F
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Topic, Board, User
from .forms import NewTopicForm
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView

def Board_View(request) :
    context = {'all_board' : Board().get_all_board()}
    return render(request, 'index.html', context)

def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    topics = board.topics.order_by('-last_update').annotate(replies=Count('post'))
    return render(request, 'Topic.html', {'board': board, 'topics': topics})

def topic_posts(request, pk) :
    topic = get_object_or_404(Topic, pk=pk)
    posts = topic.posts.all()
    return render(request, 'Post.html', {'topic':topic ,'posts': posts})

def new_topic(request, pk) :
    board = get_object_or_404(Board, pk=pk)
    if request.method == 'POST' :
        subject = request.POST['subject']
        message = request.POST['message']
        user = User.objects.first()  # get the currently logged in user
        topic = Topic.objects.create(topic_subject=subject, board=board, topic_stater=user)
        post = Post.objects.create(message=message, topic=topic, created_by=user)
        return redirect('board_topics', pk=board.pk)
    return render(request, 'new_topic.html', {'board':board })











# class BoardListView(ListView):
#     model = Board
#     template_name = 'index.html'
#     context_object_name = "all_board"
#
#     def get_queryset(self):
#         return Board.objects.prefetch_related() \
#             .annotate(post_count=Count('topic__post', distinct=True)) \
#             .annotate(topic_count=Count('topic', distinct=True))
#
#     def get_last(self):
#         return Post.objects.filter(topic__board=self).order_by('-updated_at').first()
#
#     def get_context_data(self, *args, object_list=None, **kwargs):
#         context = super(BoardListView, self).get_context_data(*args, **kwargs)
#         context['all_board'] = self.get_queryset()
#         return context

#
# class BoardDetailView(DetailView):
#     model = Board
