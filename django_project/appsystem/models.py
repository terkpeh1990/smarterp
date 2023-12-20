from django.db import models
from company.models import *

# Create your models here.
class appmodules(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        db_table = 'Systemconfig'
        verbose_name = 'Systemconfig'
        verbose_name_plural = 'Systemconfigs'    

    def __str__(self):
        return self.name

class Companymodule(models.Model):
    tenant_id = models.ForeignKey(
        Tenants, blank=True, null=True, related_name = 'companyapp',on_delete=models.CASCADE)
    app = models.ForeignKey(
        appmodules, blank=True, null=True, related_name = 'app',on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.app.name} ---- {self.tenant_id.name}"

