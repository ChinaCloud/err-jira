# coding: utf-8

import pygal
import pandas as pd
from pandas import Series, DataFrame


JIRA_JOB_TYPE = ['Story', '任务']
JIRA_BUG_TYPE = ['缺陷']
JIRA_ISSUE_STATUS = [
    '开始',
    'In Dev',
    'Ready For Product Testing',
    'Product Testing',
    'Ready For Test',
    'Testing',
    '完成'
]


class Analyzer(object):

    def tranfer(self, issues:list) -> None:
        raise(NotImplementedError)


class JiraIssueAnalyzer(Analyzer):

    def tranfer(self, issues:list) -> None:
        data = {
            issue.key: [
                issue.key,
                issue.fields.summary,
                issue.fields.status.name,
                issue.fields.components[0].name if issue.fields.components else None,
                issue.fields.issuetype.name,
                issue.fields.priority.name,
                issue.fields.workratio,
                issue.fields.assignee.displayName,
                issue.fields.creator.displayName,
                issue.fields.reporter.displayName,
                issue.fields.created,
                issue.fields.updated,
                issue.fields.duedate,
            ] for issue in issues
        }
        index = ['key', 'summary', 'status', 'component', 'type', 'priority', 'workratio', 'assignee',
                   'creator', 'reporter', 'created', 'updated', 'duedate']
        self._base_frame = DataFrame(data=data, index=index).T

    def stories_status_report(self, groupby=None):
        if not groupby:
            groupby = ['assignee', 'status']

        # TODO: 替换成可变索引列
        counted = self._base_frame.groupby(groupby)['status'].count()
        frame = counted.unstack(fill_value=0).reindex(columns=JIRA_ISSUE_STATUS, fill_value=0)

        bar_chart = pygal.HorizontalStackedBar()
        bar_chart.title = "Stories status"
        bar_chart.x_labels = frame.index.tolist()

        for col in frame:
            bar_chart.add(col, frame[col].tolist())
        bar_chart.render()