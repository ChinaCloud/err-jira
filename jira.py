# coding: utf-8
from errbot import BotPlugin, botcmd

class Jira(BotPlugin):
    """Jira plugin for Errbot"""

    @botcmd
    def jira_add(self, mess, args):
        # Will respond to !basket add
        return 'Jira added'

    @botcmd
    def jira_remove(self, mess, args):
        # Will respond to !basket remove
        return 'Jira removed'