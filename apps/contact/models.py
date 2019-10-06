from django.db import models
from django.utils.safestring import mark_safe
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('タイトル', max_length=100)
    text = MarkdownxField('本文')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'contacts'
        verbose_name_plural = '全体連絡'
        verbose_name = '全体連絡'

    def __str__(self):
        return self.title

    def html_text(self):
        # markdownをhtmlに変換する
        return mark_safe(markdownify(self.text))
