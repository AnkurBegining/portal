from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from ckeditor.fields import RichTextField
from django.db.models.signals import pre_save

from users.models import SystersUser
from django.utils.text import slugify


class Post(models.Model):
    """Abstract base class for postings like news and resources.
    This class can't be used in isolation.
    """
    slug = models.SlugField(max_length=150, verbose_name="Slug")
    title = models.CharField(max_length=255, verbose_name="Title")
    date_created = models.DateField(auto_now=False, auto_now_add=True, verbose_name="Date published")
    date_modified = models.DateField(auto_now=True, auto_now_add=False, verbose_name="Date last modified")
    author = models.ForeignKey(SystersUser, verbose_name="Author")
    content = RichTextField(verbose_name="Content")

    class Meta:
        abstract = True


# def create_slug(instance, new_slug=None):
#     slug = slugify(instance.title)
#     if new_slug is not None:
#         slug = new_slug
#     qs = Post.objects.filter(slug=slug).order_by("-id")
#     exists = qs.exists()
#
#     if exists:
#         new_slug = "%s-%s" % (slug, qs.first().id)
#         return create_slug(instance, new_slug=new_slug)
#     return slug
#
#
# def pre_save_post_receiver(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = create_slug(instance)
#
#
# pre_save.connect(pre_save_post_receiver, sender=Post)


class Comment(models.Model):
    """Model to represent a comment to a generic model.
    Intended to be used for News and Resource models."""
    date_created = models.DateField(auto_now=False, auto_now_add=True, verbose_name="Date created")
    author = models.ForeignKey(SystersUser, verbose_name="Author")
    is_approved = models.BooleanField(default=True, verbose_name='Is approved')
    body = models.TextField(verbose_name="Body")
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    def __str__(self):
        return "Comment by {0} to {1}".format(self.author, self.content_object)
