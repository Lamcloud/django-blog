from django.http.response import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import loader
from blogging.models import Post

def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args: \n"
        body += "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")

# def list_view(request):
#     published = Post.objects.exclude(published_date__exact=None)
#     posts = published.order_by('-published_date')  # most recent post first
#     template = loader.get_template('blogging/list.html')
#     context = {'posts': posts}  # it's a dictionary
#     body = template.render(context)
#     return HttpResponse(body, content_type="text/html")

def list_view(request):
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by('-published_date')  # most recent post first
    context = {'posts': posts}  # it's a dictionary
    return render(request, 'blogging/list.html', context)

def detail_view(request, post_id):
    publisehd = Post.objects.exclude(published_date__exact=None)
    try:
        post = publisehd.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404
    context = {'post': post}
    return render(request, 'blogging/detail.html', context)