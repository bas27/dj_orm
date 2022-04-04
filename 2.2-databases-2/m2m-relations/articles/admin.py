from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag


class TagInlineFormset(BaseInlineFormSet):
    def clean(self):
        real_forms = [f for f in self.forms if not f.cleaned_data['DELETE']]
        tag_ids = set([form.cleaned_data['tag'].id for form in real_forms])
        if len(tag_ids) != len(self.forms):
            raise ValidationError('Есть двойники строк')
        
        # for i in sel
        # article_ids = []
        # print(forms_main)
        
        # for form in self.forms:
        #            #    # В form.cleaned_data будет словарь с данными
        # #     # каждой отдельной формы, которые вы можете проверить
        #     print(form.cleaned_data['is_main'])
        #     # вызовом исключения ValidationError можно указать админке о наличие ошибки
        #     # таким образом объект не будет сохранен,
        #     # а пользователю выведется соответствующее сообщение об ошибке
                # raise ValidationError('Основным может быть только один раздел, проверьте отметки!')
        return super().clean()  # вызываем базовый код переопределяемого метода
class TagInline(admin.TabularInline):
    model = Tag.articles.through
    extra = 0
    formset = TagInlineFormset
    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Статьи'


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_at', 'image']
    inlines = [TagInline,]
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',]
    inlines = [TagInline,]
    exclude = ('articles',)