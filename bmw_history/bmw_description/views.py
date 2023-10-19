from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from bmw_description.models import *
import os

def view_homepage(requests):
    data = SeriesDescription.objects.all()
    series_dict = {obj.name: (obj.title, obj.description) for obj in data}

    context = {
        'series_dict': series_dict
    }

    return render(requests, 'bmw_description/index.html', context=context)


def view_series_page(requests):
    data = SeriesDescription.objects.all()
    series_dict = {obj.name: (obj.title, obj.description[:100] + '...') for obj in data}

    context = {
        'series_dict': series_dict
    }
    return render(requests, 'bmw_description/series_list_page.html', context=context)


def series_description_page(requests, series_name: str):
    # page = render_to_string('bmw_description/series_description.html')
    # return HttpResponse(page)

    data = SeriesDescription.objects.all()
    series_dict = {obj.name: (obj.title, obj.description) for obj in data}

    if series_name not in series_dict:
        return render(requests, 'page_not_found.html', status=404)

    content = {
        'series_name': series_name,
        'series_dict': series_dict
    }
    return render(requests, 'bmw_description/series_description.html', context=content)


# def series_number_handler(requests, series_number):
#     if series_number in bmw_series_description:
#         instance = bmw_series_description[series_number]
#         title = instance.title
#         description = instance.description
#         return HttpResponse(wrap_in_tag(title, 'h1') + wrap_in_tag(description, 'p'))
#     elif series_number == 'home':
#         url = reverse('series_name')
#         print(url)
#         return redirect(url)
#     else:
#         return HttpResponseNotFound(f'<h1>Страница по ключевому слову: {series_number} не найдена<h1/>')


def redirect_series_number_handler(requests, series_number):
    series_dict = {
        1: '1series',
        2: '2series',
        3: '3series',
        4: '4series',
        5: '5series'
    }
    if series_number in series_dict:
        url = reverse('series_name_path', args=(series_dict[series_number],))
        return redirect(url)
    else:
        return render(requests, 'page_not_found.html', status=404)


def get_image_names(directory_path):
    image_names = []
    try:
        image_names = os.listdir(directory_path)
    except OSError:
        print(f"Ошибка при получении списка файлов в директории: {directory_path}")
    return image_names


def view_gallery_page(requests):
    image_list = get_image_names(r'C:\Users\uinst\PycharmProjects\django_bmw_history\bmw_history\bmw_description\static\images\gallery')
    data = SeriesDescription.objects.all()
    series_dict = {obj.name: (obj.title, obj.description[:100] + '...') for obj in data}

    context = {
        'images': image_list,
        'series_dict': series_dict
    }
    return render(requests, 'bmw_description/gallery.html', context=context)
