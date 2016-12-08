# coding: utf-8
from typing import Callable

from jira import JIRA
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


class ClientFacadeMixin(object):

    JQL_CURRENT_ISSUES = 'project = %s AND sprint in openSprints() AND sprint not in futureSprints()'
    JQL_CURRENT_STORIES = JQL_CURRENT_ISSUES + ' AND type != "缺陷"'

    def _get_client(self):
        # TODO: 通过Message形式配置, 删除以下代码
        self.projects = ['PAAS']
        self.project_boards = {
            'PAAS': ['Paas Scrum']
        }

        if not hasattr(self, '_client') or self._client is None:
            assert hasattr(self, 'config') or self.config is None, \
                '缺少服务器与认证配置, 请联系管理员(通过"!plugin config"命令指定相关配置).'
            self._client = JIRA(server=self.config['SERVER'],
                                basic_auth=(self.config['USERNAME'], self.config['PASSWORD']))
        return self._client

    def get_current_issues(self, project_name) -> list:
        return self._client.search_issues(self.JQL_CURRENT_ISSUES % project_name)

    def get_current_stories(self, project_name) -> list:
        return self._client.search_issues(self.JQL_CURRENT_STORIES % project_name)