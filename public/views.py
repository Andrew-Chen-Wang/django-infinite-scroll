from django.shortcuts import render
from django.views.generic import ListView

from public.models import English

from django.core.paginator import Paginator
from django.http import JsonResponse, Http404
from  django.utils.translation import gettext_lazy as _


class Hello(ListView):
    model = English
    paginate_by = 50
    ordering = "name"


all_view = Hello.as_view()


def index(request):
    english_list = English.objects.all().order_by("name")
    paginator = Paginator(english_list, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data= {"data": [[q.id, q.name] for q in page_obj.object_list]}
    # print(data)

    return JsonResponse(data)
