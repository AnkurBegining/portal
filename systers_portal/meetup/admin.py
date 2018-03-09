from django.contrib import admin

from meetup.models import MeetupLocation, Meetup, Rsvp, SupportRequest


class meetupModelAdmin(admin.ModelAdmin):
    search_fields = ['title', 'venue', 'description']
    list_filter = ['date']
    prepopulated_fields = {'slug': ('title',), }

    class Meta:
        model = Meetup

admin.site.register(MeetupLocation)
admin.site.register(Meetup, meetupModelAdmin)
admin.site.register(Rsvp)
admin.site.register(SupportRequest)
