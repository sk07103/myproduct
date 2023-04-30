from datetime import datetime, date
from apscheduler.schedulers.background import BackgroundScheduler
import logging

logger = logging.getLogger('file')


def send_mail():
    logger.info(f'メールが送信されました')


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_mail, 'interval', minutes=1)
    scheduler.start()
