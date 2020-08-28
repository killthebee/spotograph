from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def show_page(request):
    template = loader.get_template('index.html')
    context = {}
    render_page = template.render(context, request)
    return HttpResponse(render_page)