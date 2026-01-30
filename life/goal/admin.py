from django.contrib import admin
from  goal.models import Course,Semester,Subject,Resource,contact
admin.site.site_header = "GENX PORTAL"
admin.site.site_title = "GENX Admin Portal"
admin.site.index_title = "Welcome to GENX Portal"
# ✅ DEFINE INLINE FIRST
# goal/admin.py

admin.site.register(contact)


# -- Inline: Resource (shown on Subject page) --
class ResourceInline(admin.StackedInline):
    model = Resource
    extra = 5             # number of empty resource rows shown by default
    fields = ('title', 'type', 'unit_number', 'content', 'link', 'link_text')
    show_change_link = True    # helpful link to open resource in its own admin page

# -- Inline: Subject (shown on Semester page) --
class SubjectInline(admin.TabularInline):
    model = Subject
    extra = 4
    fields = ('name',)

# -- Inline: Semester (shown on Course page) --
class SemesterInline(admin.TabularInline):
    model = Semester
    extra = 6
    fields = ('number',)

# -- Admin: Course --
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    inlines = [SemesterInline]

# -- Admin: Semester --
@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'course', 'number')  # adjust __str__ if needed
    list_filter = ('course',)
    search_fields = ('course__name',)
    inlines = [SubjectInline]

# -- Admin: Subject (primary place to add resources) --
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'semester')
    list_filter = ('semester__course', 'semester')
    search_fields = ('name',)
    inlines = [ResourceInline]

# -- Admin: Resource standalone (useful to search/filter resources globally) --
@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'type', 'unit_number')
    list_filter = ('type', 'subject__semester__course', 'subject')
    search_fields = ('title', 'content', 'link', 'link_text')
    ordering = ('subject', 'unit_number', 'type')
