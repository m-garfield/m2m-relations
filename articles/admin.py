from django.contrib import admin
from django.core.exceptions import ValidationError
from .models import Article, Scope
from django.forms import BaseInlineFormSet


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        print(self.forms)
        quantity_tag = 0
        for form in self.forms:
            if 'is_main' in form.cleaned_data:
                if form.cleaned_data['is_main'] is True:
                    quantity_tag += 1
        if not quantity_tag == 1:
            raise ValidationError('Должен быть один и только один главный Тэг')
        return super().clean()


class RelationshipInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]
