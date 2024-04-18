from celery import shared_task
from .downloaddb import download_all


@shared_task
def update_db():
    download_all()
