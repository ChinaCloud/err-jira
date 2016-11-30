# coding: utf-8
from errbot import BotPlugin, botcmd

class Jira(BotPlugin):
    """Jira plugin for Errbot"""

    def get_configuration_template(self):
        return {
            'ID_TOKEN': '00112233445566778899aabbccddeeff',
            'USERNAME':'changeme'
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