from django.contrib import admin
from .models import Torneo, TournamentRegistration
from .models import Torneo

@admin.register(Torneo)
class TorneoAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'quantity', 'start', 'finish', 'location', 'province')
    list_filter = ('location', 'province', 'start', 'finish')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ('author',)
    # date_hierarchy = 'publish'
    # ordering = ('-start',)
    readonly_fields = ('created', 'updated')

@admin.register(TournamentRegistration)
class TournamentRegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'surnames', 'mail', 'tournament_title', 'status', 'paid')
