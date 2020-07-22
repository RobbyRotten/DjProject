from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound


def index(request):
    return render(request, 'index.html')


def about(request):
    # return HttpResponse("<h2>About Mitteilung</h2>")
    return HttpResponseRedirect('/contacts')


def contacts(request):
    return HttpResponse("<h2>Contacts</h2>")


def users(request, user_id):
    try:
        i = int(user_id)
        return HttpResponse("<h2>User id{}'s page</h2>".format(user_id))
    except ValueError:
        return HttpResponseNotFound("<h2>Unavaiable user id '{}'</h2>".format(user_id))


def groups(request):
    group = request.GET.get('name', 'default')
    rights = request.GET.get('rights', 'view')
    if group != 'default':
        group = ' '.join(n for n in group.split('_'))
        if rights != 'admin':
            return HttpResponse("<h2>Group {} page</h2>".format(group.title()))
        else:
            return HttpResponse("<h2>Group {} admin page</h2>".format(group.title()))
    else:
        return HttpResponseNotFound("<h2>Group not found</h2>")
