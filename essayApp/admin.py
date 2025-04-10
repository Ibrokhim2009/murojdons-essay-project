from django.contrib import admin
from .models import (
    Podcast, Tag, Essay, Paragraph, QuestionForEssay,
    Book, BookThemes, ContactMessage
)

# --- Paragraph and Question in Essay ---
class ParagraphInline(admin.TabularInline):
    model = Paragraph
    extra = 1
    max_num = 20

class QuestionInline(admin.TabularInline):
    model = QuestionForEssay
    extra = 1
    max_num = 20

class EssayAdmin(admin.ModelAdmin):
    inlines = [ParagraphInline, QuestionInline]

# --- Themes in Book ---
class ThemeInline(admin.TabularInline):
    model = BookThemes
    extra = 1
    max_num = 20

class BookAdmin(admin.ModelAdmin):
    inlines = [ThemeInline]

# --- ContactMessage Admin ---
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message', 'sent_at']
    readonly_fields = ['name', 'user', 'email', 'message', 'sent_at']

    def has_change_permission(self, request, obj=None):
        # Только просмотр, без редактирования
        if obj:
            return False
        return super().has_change_permission(request, obj)

# --- Register other models ---
admin.site.register(Podcast)
admin.site.register(Tag)
admin.site.register(Essay, EssayAdmin)
admin.site.register(Book, BookAdmin)
