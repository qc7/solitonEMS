from django.db import models

from employees.models import Employee
from organisation_details.models import Position


class JobAdvertisement(models.Model):
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name='title')
    education = models.CharField(max_length=20)
    vacancy = models.IntegerField()
    experience = models.IntegerField()
    post_date = models.DateField(auto_now=True)
    description = models.TextField()
    show_salary = models.BooleanField(default=True)
    deadline = models.DateField()

    def __str__(self):
        return self.position.name

    @property
    def number_of_applications(self):
        return self.jobapplication_set.count()


class JobApplication(models.Model):
    job_ad = models.ForeignKey(JobAdvertisement, on_delete=models.CASCADE)
    applicant = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='job_application')
    cv = models.FileField(upload_to='cvs/')

    def __str__(self):
        return self.applicant.first_name
