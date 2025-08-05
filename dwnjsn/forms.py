import json
from django import forms
from datetime import datetime

class JsonUploadForm(forms.Form):
    json_file = forms.FileField(
        label='Загрузите JSON файл',
        help_text='Файл должен содержать массив объектов с полями "name" (строка до 50 символов) и "date" (в формате YYYY-MM-DD_HH:mm)'
    )

    def clean_json_file(self):
        file = self.cleaned_data.get('json_file')

        if not file:
            raise forms.ValidationError('Файл не загружен.')

        if not file.name.endswith('.json'):
            raise forms.ValidationError('Только JSON-файлы разрешены.')

        try:
            content = file.read().decode('utf-8')
            data = json.loads(content)
        except json.JSONDecodeError as e:
            raise forms.ValidationError(f'Некорректный JSON: {str(e)}')
        except Exception as e:
            raise forms.ValidationError(f'Ошибка при чтении файла: {str(e)}')

        if not isinstance(data, list):
            raise forms.ValidationError('JSON должен содержать массив объектов.')

        for idx, item in enumerate(data):
            if not isinstance(item, dict):
                raise forms.ValidationError(f'Элемент №{idx + 1} не является объектом.')

            name = item.get('name')
            date_str = item.get('date')

            if not isinstance(name, str) or len(name) > 50:
                raise forms.ValidationError(f'Поле "name" в элементе №{idx + 1} должно быть строкой до 50 символов.')

            if not isinstance(date_str, str):
                raise forms.ValidationError(f'Поле "date" в элементе №{idx + 1} должно быть строкой.')

            try:
                datetime.strptime(date_str, '%Y-%m-%d_%H:%M')
            except ValueError:
                raise forms.ValidationError(
                    f'Поле "date" в элементе №{idx + 1} должно быть в формате YYYY-MM-DD_HH:MM. Получено: {date_str}'
                )

        self.cleaned_data['json_data'] = data
        file.seek(0)
        return file