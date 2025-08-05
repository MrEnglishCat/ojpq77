import json
import os

from django.conf import settings
from django.shortcuts import render
from mimesis import Datetime, Text

from dwnjsn.forms import JsonUploadForm
from dwnjsn.models import JSNUploadModel


# Create your views here.


def upload_jsn(request):
    if request.method == 'POST':
        form = JsonUploadForm(request.POST, request.FILES)

        if form.is_valid():
            json_data = form.cleaned_data['json_data']
            JSNUploadModel.objects.bulk_create(map(lambda item: JSNUploadModel(name=item["name"], date=item["date"]), json_data))

            success_message = 'Файл успешно загружен!'
        else:
            success_message = None

        return render(request, 'upload.html', {'form': form, 'success_message': success_message})


    elif request.method == 'GET':
        form = JsonUploadForm()


        # Для тестов добавлены строки 36 - 40 - что бы при обращении к
        # форме параллельно создавался произвольный объект с тестовыми данными в БД
        text = Text(locale="ru").text(quantity=1)
        if len(text) > 50:
            text = f"{text[:47]}..."
        JSNUploadModel.objects.create(name=text)

        return render(request, 'upload.html', {'form': form})


def view_jsn(request):
    if request.method == 'GET':
        data = JSNUploadModel.objects.all()

        for item in data:
            item.date = item.date.strftime("%Y-%m-%d_%H:%M")

        return render(request, "result_table.html", {"data":data})
