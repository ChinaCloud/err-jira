# coding: utf-8
import io

from errbot import botcmd, BotPlugin

from analyzers import JiraIssueAnalyzer
from helpers.messaging import processing
from mixins import (
    CronableMixin,
    ClientFacadeMixin,
)


class Jira(CronableMixin, ClientFacadeMixin, BotPlugin):
    """Jira plugin for Errbot"""

    def activate(self):
        super().activate()
        self._init_scheduler()

        self.project_name = 'PAAS'

    def deactivate(self):
        super().deactivate()
        self._shutdown_scheduler()

    def callback_mention(self, message, mentioned_people):
        if self.bot_identifier in mentioned_people:
            self.send(message.frm, '找我嘎哈？')

    def check_configuration(self, configuration):
        # TODO: 添加配置验证, 且在验证不通过时, 清除_client属性
        pass

    def get_configuration_template(self):
        return {
            'SERVER': 'http://172.16.80.81:8888', # Jira服务器地址
            'USERNAME': 'xuwenbao', # Jira用户名
            'PASSWORD': '123', # Jira密码
        }

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

    @botcmd
    @processing
    def report_stories(self, mess, args):
        stories = self.get_current_stories(self.project_name)
        analyzer = JiraIssueAnalyzer()
        analyzer.tranfer(stories)
        f = io.BytesIO(analyzer.stories_status_report())
        self.send_stream_request(mess.frm, f, name='stories.svg', stream_type='image/svg+xml')