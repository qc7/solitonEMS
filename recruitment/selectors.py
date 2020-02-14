
from recruitment.models import JobAdvertisement, JobApplication


def get_all_job_ads():
    return JobAdvertisement.objects.all()


def get_job_advertisement(job_advertisement_id):
    return JobAdvertisement.objects.get(pk=job_advertisement_id)


def get_job_advertisement(job_description_id):
    return JobAdvertisement.objects.get(pk=job_description_id)


def get_job_applications(job_advertisement):
    job_applications = JobApplication.objects.filter(job_ad=job_advertisement)
    return job_applications
