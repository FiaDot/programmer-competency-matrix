from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response


def main(request):
#    posts = Post.objects.all().order_by("-created")
   
#    return render_to_response("survay.html", dict(posts=posts, user=request.user))        
    return 1


def post(request, pk):
    return 1
    


def statistics(request):
    return 1