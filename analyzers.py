# coding: utf-8

from typing import List

import pygal
import pandas as pd
from pandas import Series, DataFrame
from jira.resources import Issue


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
JIRA_ISSUE_STATUS_DISPLAYNAME = [
    '准备开发',
    '开发中',
    '等待产品经理测试',
    '产品经理测试',
    '等待测试',
    '测试',
    '完成'
]


class Analyzer(object):

    def tranfer(self, issues:List[Issue]) -> None:
        raise(NotImplementedError)


class JiraIssueAnalyzer(Analyzer):

    def tranfer(self, issues:List[Issue]) -> None:
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

    def stories_report(self, groupby:str=None, title:str= 'Stories status') -> str:
        if not groupby:
            groupby = ['assignee', 'status']
        else:
            groupby = [groupby].append('status')

        # TODO: 替换成可变索引列
        counted = self._base_frame.groupby(groupby)['status'].count()
        frame = counted.unstack(fill_value=0).reindex(columns=JIRA_ISSUE_STATUS, fill_value=0)

        bar_chart = pygal.HorizontalStackedBar()
        bar_chart.title = title
        bar_chart.x_labels = frame.index.tolist()

        for col in frame:
            bar_chart.add(col, frame[col].tolist())
        return bar_chart.render()