# polling/views.py

from django.shortcuts import render
from django.http import Http404
from polling.models import Poll


#added 9/7/22
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# class ListView():
#     def as_veiw(self):
#         return self.get
#
#     def get(self, request):
#         model_list_name = self.model.__name__.lower() + '_list'
#         context = {model_list_name: self.model.objects.all()}
#         return render(request, self.template_name, context)

class PollListView(ListView):  # assignment 08 will be for blogging
    model = Poll
    template_name = 'polling/list.html'

# above added 9/7/22


def list_view(request):
    context = {'polls': Poll.objects.all()}
    return render(request, 'polling/list.html', context)


#added 9/7/22

class PollDetailView(DetailView):
    model = Poll
    template_name = 'polling/detail.html'

    def post(self, request, *args, **kwargs):  # *args: on website http://127.0.0.1:8000/polling/polls/1, 1 is passed
        poll = self.get_object()

        if request.POST.get("vote") == "Yes":
            poll.score += 1
        else:
            poll.score -= 1
        poll.save()
        context = {"object": poll}
        return render(request, "polling/detail.html", context)


# above added 9/7/22

# def detail_view(request, poll_id):
#     try:
#         poll = Poll.objects.get(pk=poll_id)
#     except Poll.DoesNotExist:
#         raise Http404
#
#     if request.method == "POST":
#         if request.POST.get("vote") == "Yes":
#             poll.score += 1
#         else:
#             poll.score -= 1
#         poll.save()
#
#     context = {'poll': poll}
#     return render(request, 'polling/detail.html', context)
#
