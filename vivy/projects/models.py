from django.db import models

from django.contrib.postgres.fields import ArrayField


class Project(models.Model):
    name = models.CharField(max_length=50, unique=True)
    headline = models.CharField(max_length=300)
    logo_url = models.URLField(blank=True, default='')
    opportunity = models.TextField(blank=True, default='')
    solution = models.TextField(blank=True, default='')
    technology = models.TextField(blank=True, default='')
    staff = models.ManyToManyField('employees.Employee', related_name='project_staff')
    screenshot = ArrayField(models.URLField(blank=True, default=''), size=5)
    added_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ['-added_at']

    def __str__(self):
        return '{0}'.format(self.name)
