# coding: utf-8
from errbot import botcmd, BotPlugin
from helpers.jira_ import CronableMixin


class Jira(CronableMixin, BotPlugin):
    """Jira plugin for Errbot"""

    def get_configuration_template(self):
        return {
            'SERVER': 'http://172.16.80.81:8888', # Jira服务器地址
            'USERNAME': 'xuwenbao', # Jira用户名
            'PASSWORD': '123', # Jira密码
            'PROJECT': 'PAAS', # Jira项目
            'BOARD': 'Paas Scrum', # Jira Board
        }

    def activate(self):
        super().activate()
        self._init_scheduler()

    def deactivate(self):
        super().deactivate()
        self._shutdown_scheduler()

    def callback_mention(self, message, mentioned_people):
        if self.bot_identifier in mentioned_people:
            self.send(message.frm, '找我嘎哈？')

    @botcmd
    def jira_test(self, mess, args):
        return '大爷, 来玩玩啊!'

    @botcmd
    def jira_remove(self, mess, args):
        # Will respond to !basket remove
        return 'Jira removed'