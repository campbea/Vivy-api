from django.contrib.postgres.fields import HStoreField
from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    image_url = models.URLField(blank=True, default='')
    summary = models.TextField(blank=True, default='')
    questions = HStoreField(null=True)
    added_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
        ordering = ['id']

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)
