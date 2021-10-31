from django.contrib import admin
from apps.game.models import GameBoard, Category, Question

# Register your models here.
admin.site.register(GameBoard, admin.ModelAdmin)
admin.site.register(Category, admin.ModelAdmin)
admin.site.register(Question, admin.ModelAdmin)
