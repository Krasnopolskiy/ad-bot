from bot.models import Announcement, Rule, Team, User, VpnConfig, Vulnbox
from bot.s3 import S3Config
from django import forms
from django.conf import settings
from django.contrib import admin


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ("title", "shorten_description", "created_at")
    search_fields = ("title", "description")

    @admin.display(description="Description")
    def shorten_description(self, obj: Announcement) -> str:
        max_length = 64
        if len(obj.description) < max_length:
            return obj.description
        return f"{obj.description[:max_length]}..."


@admin.register(Rule)
class RuleAdmin(admin.ModelAdmin):
    list_display = ("description",)
    search_fields = ("description",)


class UserInline(admin.TabularInline):
    model = User
    fields = ["tg_id", "admin"]
    extra = 0
    can_delete = False


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    inlines = [UserInline]


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("tg_id", "admin", "team")
    list_filter = ("admin", "team")
    search_fields = ("tg_id",)


class VpnConfigForm(forms.ModelForm):
    class Meta:
        model = VpnConfig
        fields = ["path", "team"]

    path = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        items = S3Config().list_items()
        self.base_fields["path"].choices = [(item, item) for item in items]
        super().__init__(*args, **kwargs)


@admin.register(VpnConfig)
class VpnConfigAdmin(admin.ModelAdmin):
    change_form_template = "s3_change_form.html"

    list_display = ("path", "team")
    list_filter = ("team",)
    search_fields = ("path",)
    form = VpnConfigForm

    def changeform_view(self, request, object_id=None, form_url="", extra_context=None):
        extra_context = extra_context or {}
        extra_context["S3_URL"] = settings.S3_URL
        return super().changeform_view(request, object_id, form_url, extra_context=extra_context)


@admin.register(Vulnbox)
class VulnboxAdmin(admin.ModelAdmin):
    list_display = ("description", "team")
    list_filter = ("team",)
    search_fields = ("description",)
