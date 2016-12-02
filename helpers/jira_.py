# coding: utf-8
from typing import Callable

from apscheduler.schedulers.background import BackgroundScheduler


class CronableMixin(object):

    def _init_scheduler(self) -> None:
        self.log.info('Init scheduler and start')
        self.scheduler = BackgroundScheduler()
        self.scheduler.start()

    def _shutdown_scheduler(self) -> None:
        if self.scheduler.running:
            self.scheduler.shutdown()

    def start_cron(self, method: Callable[..., None], args=None, kwargs=None,
                   year='*', month='*', day='*', week='*', day_of_week='*', hour='*',
                   minute='*', second='*', start_date=None, end_date=None, timezone=None) -> None:
        self.log.info('Add new cron job.')
        self.scheduler.add_job(func=method, args=args, kwargs=kwargs, trigger='cron', year=year,
                               month=month, day=day, week=week, day_of_week=day_of_week, hour=hour,
                               minute=minute, second=second, start_date=start_date, end_date=end_date,
                               timezone=timezone)