from django.db import models
from common.models import CommonModel

# Create your models here.
class Community(CommonModel):
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="communities"
    )
    question = models.TextField(max_length=240)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name_plural = "Communities"


class Answer(CommonModel):
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="answers"
    )
    community = models.ForeignKey(
        "Community", on_delete=models.CASCADE, related_name="answers"
    )
    answer = models.TextField(max_length=240)


class Wonder(CommonModel):
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="wonders"
    )
    community = models.ForeignKey(
        "Community", on_delete=models.CASCADE, related_name="wonders"
    )
    wonder = models.BooleanField(default=False)
