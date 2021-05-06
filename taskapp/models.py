from django.conf import settings
from django.db import models

# Create your models here.


class ToDoListQuerySet(models.QuerySet):
    pass

class ToDoListManager(models.Manager):
    def get_queryset(self):
        return ToDoListQuerySet(self.model, using=self._db)

class ToDoList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.TextField(help_text='Enter field documentation',blank=True,unique=True)
    modified_timestamp = models.DateTimeField(auto_now=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField()

    objects = ToDoListManager()

    def __str__(self):
        return str(self.name)[:]

    class Meta:
        verbose_name  = "ToDoList"
        verbose_name_plural = "ToDoLists"

    @property
    def owner(self):
        return self.user

class ListItem(models.Model):
    PRIORITY_CHOICES = (
        ('1', 'Low'),
        ('2', 'Medium'),
        ('3', 'Important'),
        ('4', 'Critical'),
    )
    to_do_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    item_name = models.TextField(help_text='Enter field documentation',blank=True,null=True)
    modified_timestamp = models.DateTimeField(auto_now=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='1')
    objects = ToDoListManager()

    def __str__(self):
        return str(self.item_name)[:]

    # class Meta:
    #     verbose_name  = "ToDoList"
    #     verbose_name_plural = "ToDoLists"

    @property
    def owner(self):
        return self.user
