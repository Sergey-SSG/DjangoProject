from django import forms
from .models import Product
from django.core.exceptions import ValidationError

FORBIDDEN_WORDS = [
    'казино',
    'криптовалюта',
    'крипта',
    'биржа',
    'дешево',
    'бесплатно',
    'обман',
    'полиция',
    'радар',
]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'image']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название продукта'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание продукта',
                'rows': 5
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите цену'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.label_suffix = ''

    def clean_name(self):
        name = self.cleaned_data['name']
        for word in FORBIDDEN_WORDS:
            if word.lower() in name.lower():
                raise ValidationError(f'Название не должно содержать запрещённое слово: {word}')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description', '')
        for word in FORBIDDEN_WORDS:
            if word.lower() in description.lower():
                raise ValidationError(f'Описание не должно содержать запрещённое слово: {word}')
        return description

    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise ValidationError('Цена не может быть отрицательной')
        return price

    def clean_category(self):
        category = self.cleaned_data.get('category')
        if not category:
            raise ValidationError('Пожалуйста, выберите категорию')
        return category

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if image.content_type not in ['image/jpeg', 'image/png']:
                raise ValidationError('Допустимы только изображения JPEG или PNG')
            if image.size > 5 * 1024 * 1024:
                raise ValidationError('Размер изображения не должен превышать 5 МБ')
        return image