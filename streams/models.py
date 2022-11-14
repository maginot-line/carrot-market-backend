from django.db import models
from common.models import CommonModel

# Create your models here.
class Stream(CommonModel):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.TextField()
    cloudflare_id = models.CharField(max_length=100, blank=True, null=True)
    cloudflare_url = models.CharField(max_length=100, blank=True, null=True)
    cloudflare_key = models.CharField(max_length=100, blank=True, null=True)


class Message(CommonModel):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    stream = models.ForeignKey("streams.Stream", on_delete=models.CASCADE)
    message = models.TextField()
