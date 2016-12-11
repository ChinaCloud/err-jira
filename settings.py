# coding: utf-8
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

    debug = False
    testing = False

    jira = JiraConfiguration()
    static = StaticConfiguration()


settings = AppConfiguration.load()