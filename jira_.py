# coding: utf-8
from errbot import BotPlugin, botcmd

class Jira(BotPlugin):
    """Jira plugin for Errbot"""

    def get_configuration_template(self):
        return {
            'SERVER': 'http://172.16.80.81:8888',
            'USERNAME': 'xuwenbao',
            'PASSWORD': '123',
            'PROJECT': 'PAAS',
            'BOARD': 'Paas Scrum',
        }

    def callback_mention(self, message, mentioned_people):
        if self.bot_identifier in mentioned_people:
            self.send(message.frm, '找我嘎哈？')

    @botcmd
    def jira_add(self, mess, args):
        # Will respond to !basket add
        return 'Jira added'

    @botcmd
    def jira_remove(self, mess, args):
        # Will respond to !basket remove
        return 'Jira removed'