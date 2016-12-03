# coding: utf-8
from jira import JIRA
from errbot import botcmd, BotPlugin
from helpers.jira_ import CronableMixin


class Jira(CronableMixin, BotPlugin):
    """Jira plugin for Errbot"""

    def activate(self):
        super().activate()
        self._init_scheduler()

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

    def get_client(self):
        if not hasattr(self, '_client') or self._client is None:
            assert hasattr(self, 'config') or self.config is None, \
                '缺少服务器与认证配置, 请联系管理员(通过"!plugin config"命令指定相关配置).'
            self._client = JIRA(server=self.config['SERVER'],
                                basic_auth=(self.config['USERNAME'], self.config['PASSWORD']))
        return self._client

    @botcmd
    def jira_test(self, mess, args):
        return '大爷, 来玩玩啊!'

    @botcmd
    def project_list(self, mess, args):
        """
        查看Jira项目列表
        """
        # TODO: 优化列表显示形式
        return ' '.join([project.name for project in self.get_client().projects()])