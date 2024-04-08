from django.db import models


class BaseEntity(models.Model):
    id = models.AutoField(primary_key=True)

    class Meta:
        abstract = True


class Announcement(BaseEntity):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=4096)

    class Meta:
        managed = False
        db_table = "announcements"

    def __str__(self):
        return self.title


class Rule(BaseEntity):
    description = models.TextField(max_length=4096)

    class Meta:
        managed = False
        db_table = "rules"

    def __str__(self):
        return self.description


class Team(BaseEntity):
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        managed = False
        db_table = "teams"

    def __str__(self):
        return self.name


class User(BaseEntity):
    tg_id = models.CharField(max_length=16, unique=True)
    admin = models.BooleanField(default=False)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name="users")

    class Meta:
        managed = False
        db_table = "users"

    def __str__(self):
        return self.tg_id


class VpnConfig(BaseEntity):
    path = models.CharField(max_length=128)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="vpn_configs")

    class Meta:
        managed = False
        db_table = "vpn_configs"

    def __str__(self):
        return self.path


class Vulnbox(BaseEntity):
    description = models.CharField(max_length=1024)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="vulnboxes")

    class Meta:
        managed = False
        db_table = "vulnboxes"

    def __str__(self):
        return self.description
