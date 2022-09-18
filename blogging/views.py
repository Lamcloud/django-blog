from django.http.response import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import loader
from blogging.models import Post

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# def stub_view(request, *args, **kwargs):
#     body = "Stub View\n\n"
#     if args:
#         body += "Args: \n"
#         body += "\n".join(["\t%s" % a for a in args])
#     if kwargs:
#         body += "Kwargs:\n"
#         body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
#     return HttpResponse(body, content_type="text/plain")

# def list_view(request):
#     published = Post.objects.exclude(published_date__exact=None)
#     posts = published.order_by('-published_date')  # most recent post first
#     template = loader.get_template('blogging/list.html')
#     context = {'posts': posts}  # it's a dictionary
#     body = template.render(context)
#     return HttpResponse(body, content_type="text/html")

# def list_view(request):
#     published = Post.objects.exclude(published_date__exact=None)
#     posts = published.order_by('-published_date')  # most recent post first
#     context = {'posts': posts}  # it's a dictionary
#     return render(request, 'blogging/list.html', context)


class BlogListView(ListView):  # assignment 08 will be for blogging
    model = Post
    template_name = "blogging/list.html"  # optional
    queryset = Post.objects.exclude(published_date__exact=None).order_by(
        "-published_date"
    )


#
# def detail_view(request, post_id):
#     publisehd = Post.objects.exclude(published_date__exact=None)
#     try:
#         post = publisehd.get(pk=post_id)
#     except Post.DoesNotExist:
#         raise Http404
#     context = {'post': post}
#     return render(request, 'blogging/detail.html', context)


class BlogDetailView(DetailView):
    model = Post
    template_name = "blogging/detail.html"  # optional
    queryset = Post.objects.exclude(published_date__exact=None)
