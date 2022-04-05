from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag


class TagInlineFormset(BaseInlineFormSet):
    def clean(self):
        real_forms = [f for f in self.forms if not f.cleaned_data['DELETE']]
        tag_ids_del = set([form.cleaned_data['tag'].id for form in real_forms])
        if len(tag_ids_del) != len(self.forms):
            raise ValidationError('Выбраны одноименные разделы')
        main_forms = [f for f in self.forms if f.cleaned_data['is_main']]
        if len(main_forms) == 0:
            raise ValidationError('Выберите основной раздел')
        elif len(main_forms) > 1:
            raise ValidationError('Основным может быть только один раздел, проверьте отметки!')


        return super().clean()  # вызываем базовый код переопределяемого метода
class TagInline(admin.TabularInline):
    model = Tag.articles.through
    extra = 0
    formset = TagInlineFormset
    
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_at', 'image']
    inlines = [TagInline,]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',]
    inlines = [TagInline,]
    exclude = ('articles',)