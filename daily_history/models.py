from django.db import models


class Contents(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    detail = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'daily_history'


class Image(models.Model):
    contents = models.ForeignKey("Contents", on_delete=models.CASCADE, related_name='images')
    id = models.AutoField(primary_key=True)
    image = models.FileField(upload_to='images')