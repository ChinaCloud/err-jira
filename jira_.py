# coding: utf-8
import os.path
import urllib.parse

from errbot import botcmd, BotPlugin

from settings import settings
from helpers import messaging
from reporters import JiraIssueReporter
from mixins import (
    CronableMixin,
    ClientFacadeMixin,
)


class Jira(CronableMixin, ClientFacadeMixin, BotPlugin):
    """Jira plugin for Errbot"""

    def activate(self):
        super().activate()
        self._init_scheduler()

    def deactivate(self):
        super().deactivate()
        self._shutdown_scheduler()

    def check_configuration(self, configuration):
        # TODO: 添加配置验证, 且在验证不通过时, 清除_client属性
        pass

    def get_configuration_template(self):
        pass

    @botcmd
    def jiratest(self, mess, args):
        return '大爷, 来玩玩啊!'

    @botcmd
    def project_list(self, mess, args):
        """
        查看Jira项目列表
        """
        # TODO: 优化列表显示形式
        return ' '.join([project.name for project in self._get_client().projects()])

    @botcmd(template='story_members')
    def story_members(self, mess, args):
        filename = 'story_members.svg'
        filepath = os.path.join(settings.static.dir, filename)
        uri = urllib.parse.urljoin(settings.static.access_prefix, filename)

        stories = self.get_current_stories(settings.jira.project_name)
        reporter = JiraIssueReporter(stories)
        reporter.horizontalstacked_bar('成员任务统计', ['assignee', 'status'], 'status', 'file', filepath)

        return {
            'member_stories': stories,
            'story_members_chart': uri,
        }

    @botcmd
    def story_teams(self, mess, args):
        # stories = self.get_current_issues(self.project_name)
        # return {
        #     'team_stories': stories,
        #     'story_teams_chart': [],
        # }
        project = self.get_project_by_name(settings.jira.project_name)
        return project.name