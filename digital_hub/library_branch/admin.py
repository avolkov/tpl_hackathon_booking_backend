from django.contrib import admin

# Register your models here.

from library_branch.models import (
    Branch,
    Calendar,
    CalendarRelation,
    Event,
    Rule,
)


from library_branch.forms import EventAdminForm


class CalendarInline(admin.TabularInline):
    model = Calendar


class CalendarAdminOptions(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ['name']
    fieldsets = (
        (None, {
            'fields': [
                ('name', 'slug'),
                ('required_good_standing', ),
                ('required_3d_cert')
            ]
        }),
    )


class CalendarRelationAdmin(admin.ModelAdmin):
    list_display = ('calendar', 'content_object')
    list_filter = ('inheritable',)
    fieldsets = (
        (None, {
            'fields': [
                'calendar',
                ('content_type', 'object_id', 'distinction',),
                'inheritable',
            ]
        }),
    )


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start', 'end')
    list_filter = ('start',)
    ordering = ('-start',)
    date_hierarchy = 'start'
    search_fields = ('title', 'description')
    fieldsets = (
        (None, {
            'fields': [
                ('title', ),
                ('description',),
                ('start', 'end'),
                ('creator', 'calendar'),
                ('rule', 'end_recurring_period'),
            ]
        }),
    )
    form = EventAdminForm


class RuleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('frequency',)
    search_fields = ('name', 'description')


class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', )
    fields = ('name', )
    inlines = (CalendarInline, )


admin.site.register(Branch, BranchAdmin)
admin.site.register(Calendar, CalendarAdminOptions)
admin.site.register(Event, EventAdmin)
admin.site.register(Rule, RuleAdmin)
admin.site.register(CalendarRelation, CalendarRelationAdmin)
