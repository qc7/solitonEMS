from learning_and_development.models import Resource


def get_all_resources():
    return Resource.objects.all()


def get_resource(resource_id):
    return Resource.objects.get(pk=resource_id)
