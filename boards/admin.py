from django.contrib import admin
from boards.models import Person, Organization, Relationship

class PersonInline(admin.StackedInline):
	model = Relationship

class OrganizationAdmin(admin.ModelAdmin):
	inlines = [PersonInline]
	list_display = ('name', 'org_type')


admin.site.register(Person)
admin.site.register(Organization, OrganizationAdmin)


