from django.contrib import admin, messages

from questions.models import Question, Category


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    save_on_top = True
    ordering = ['-created']
    filter_vertical = ['categories', 'companies']
    search_fields = ['title', 'text', 'categories__name']
    list_filter = ['level', 'status', 'created']
    actions = ['set_public', 'set_declined']

    @admin.action(description="Опубликовать выбранные вопросы")
    def set_public(self, request, queryset):
        count: int = queryset.update(status=Question.ModerationStatus.PUBLIC)
        self.message_user(request, f"Изменено {count} записей.")

    @admin.action(description="Отклонить публикацию выбранных записей")
    def set_declined(self, request, queryset):
        count: int = queryset.update(status=Question.ModerationStatus.DECLINED)
        self.message_user(request, f"{count} записей сняты с публикации!", messages.WARNING)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    save_on_top = True
    ordering = ['-created']
    list_display = ('name', )
    list_filter = ['name', 'created']
    list_display_links = ('name', )
