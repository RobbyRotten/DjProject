from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h2>Main page</h2>")


def about(request):
    return HttpResponse("<h2>About Mitteilung</h2>")


def contacts(request):
    return HttpResponse("<h2>Contacts</h2>")


def users(request, user_id):
    return HttpResponse("<h2>User id{}'s page".format(user_id))
