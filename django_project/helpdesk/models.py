# from django.db import models
# from company.models import *
# from authentication.models import User

# # Create your models here.
# class Teams(models.Model):
#     team_name = models.CharField(max_length=100)
#     tenant_id = models.ForeignKey(
#         Tenants, blank=True, null=True, related_name = 'team',on_delete=models.CASCADE)
   
#     class Meta:
        
#         db_table = 'Teams'
#         verbose_name = 'Team'
#         verbose_name_plural = 'Teams'

        

#     def __str__(self):
#         return f"{self.team_name} ---- {self.tenant_id}"

   


# class Technicians(models.Model):
#     technician = models.ForeignKey(User, on_delete=models.CASCADE)
#     team = models.ForeignKey(Teams, on_delete=models.CASCADE)
#     tenant_id = models.ForeignKey(
#         Tenants, blank=True, null=True, related_name = 'technicains',on_delete=models.CASCADE)
   
#     class Meta:
        
#         db_table = 'Technicians'
#         verbose_name = 'Technician'
#         verbose_name_plural = 'Technicians'

#     def __str__(self):
#         return f"{self.technician.first_name } { self.technician.last_name} ---- {self.tenant_id}"

# class Tickets(models.Model):
#     ess = (
#         ('Escalate', 'Escalate'),
#     )
#     id = models.CharField(max_length=200, primary_key=True)
#     name = models.ForeignKey(
#         Profile, null=True, blank=True, on_delete=models.CASCADE)
#     subject = models.CharField(max_length=200)
#     description = models.CharField(max_length=200)
#     region = models.ForeignKey(
#         Region, blank=True, null=True, on_delete=models.CASCADE)
#     district = models.ForeignKey(
#         District, blank=True, null=True, on_delete=models.CASCADE)
#     category = models.ForeignKey(
#         Category, null=True, blank=True, on_delete=models.CASCADE)
#     ticket_category = models.ForeignKey(
#         Ticket_category, null=True, blank=True, on_delete=models.CASCADE)
#     status = models.ForeignKey(
#         Status, null=True, blank=True, on_delete=models.CASCADE)
#     astatus = models.ForeignKey(
#         agent_Status, null=True, blank=True, on_delete=models.CASCADE)
#     prority = models.ForeignKey(
#         Prority, null=True, blank=True, on_delete=models.CASCADE)
#     agent = models.ForeignKey(Technician, null=True,
#                               blank=True, on_delete=models.CASCADE)
#     agent_team = models.ForeignKey(
#         Team, null=True, blank=True, on_delete=models.CASCADE)
#     ticket_date = models.DateField()
#     ticket_time = models.TimeField()
#     use_date = models.DateTimeField()
#     expected_date = models.DateField(null=True, blank=True)
#     expected_days = models.DurationField(null=True, blank=True)
#     escalated = models.CharField(max_length=60, choices=ess)
#     remarks = models.CharField(max_length=200, null=True, blank=True)
#     close_date = models.DateField(null=True, blank=True)
#     completed_days = models.DurationField(null=True, blank=True)
#     elapsed_time = models.DurationField(null=True, blank=True)
#     history = HistoricalRecords()