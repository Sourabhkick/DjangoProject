# from django.db import models
# from store.contrib.contenttype.model import ContentType
# from store.contrib.contenttype.fields import GenericForeignKey
#
# class Tag(models.Model):
#     label = models.CharField(max_length=225)
#
#
# class TaggedItem(models.Model):
#     tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
#
#     Content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()
#     content_object = GenericForeignKey()


from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Tag(models.Model):
    label = models.CharField(max_length=225)

    def __str__(self):
        return self.label


class TaggedItem(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    def __str__(self):
        return f"{self.tag.label} - {self.content_object}"
