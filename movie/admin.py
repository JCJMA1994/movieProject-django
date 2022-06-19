from django.contrib import admin

from .models import Movie, Director

# Register your models here.

class MovieInLine(admin.StackedInline):
    model = Movie
    extra = 1


class DirectorAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{
            'fields': ('name', 'lastname', 'biography')
        }),
        ('Date',{
            'fields': (
                'date_birth', 'date_death'
            ),
            'classes': ('collapse')
        })
    ]
    inlines = [MovieInLine]


admin.site.register(Director, DirectorAdmin)