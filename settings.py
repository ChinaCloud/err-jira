# coding: utf-8
import os

import confire


class JiraConfiguration(confire.Configuration):

    server = None
    username = None
    password = None

    job_type = None
    bug_type = None
    issue_status = None
    issue_status_displayname = None


class StaticConfiguration(confire.Configuration):

    dir = None
    access_prefix = None


class AppConfiguration(confire.Configuration):

    CONF_PATHS = [
        '/etc/err-jira.yaml',                    # The global configuration
        os.path.expanduser('~/.err-jira.yaml'),  # User specific configuration
        os.path.abspath('conf/err-jira.yaml')    # Local directory configuration
    ]

    debug = False
    testing = False

    jira = JiraConfiguration()
    static = StaticConfiguration()


settings = AppConfiguration.load()