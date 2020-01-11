from django.db import models

from employees.models import Employee, Position


class JobAdvertisement(models.Model):

    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name='title')
    education = models.CharField(max_length=20)
    vacancy = models.IntegerField()
    experience = models.IntegerField()
    post_date = models.DateField(auto_now=True)
    description = models.TextField()
    show_salary = models.BooleanField()

    def __str__(self):
        return self.position


class JobApplication(models.Model):
    job_ad = models.ForeignKey(JobAdvertisement, on_delete=models.CASCADE)
    applicant = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='job_application')
    cv = models.FileField()

    def __str__(self):
        return self.applicant

