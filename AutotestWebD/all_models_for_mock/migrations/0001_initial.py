# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-04-15 14:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tb4DataKeyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_column='title', default='', max_length=255, verbose_name='标题')),
                ('descText', models.CharField(db_column='descText', default='', max_length=2000, verbose_name='描述')),
                ('keywordKey', models.CharField(db_column='keywordKey', default='', max_length=255, unique=True, verbose_name='自定义关键字的key')),
                ('keywordCode', models.TextField(db_column='keywordCode', default='', verbose_name='自定义关键字的代码')),
                ('status', models.IntegerField(choices=[(1, '新增'), (2, '审核中'), (3, '审核通过'), (4, '审核未通过')], default=1, verbose_name='状态')),
                ('type', models.CharField(db_column='type', default='DATA_KEYWORD', max_length=50, verbose_name='类型：DATA_KEYWORD PYTHON_CODE')),
                ('state', models.IntegerField(default=1, verbose_name='状态 0删除 1有效')),
                ('addBy', models.CharField(db_column='addBy', max_length=25, null=True, verbose_name='添加者登录名')),
                ('modBy', models.CharField(db_column='modBy', max_length=25, null=True, verbose_name='修改者登录名')),
                ('addTime', models.DateTimeField(auto_now_add=True, db_column='addTime', verbose_name='创建时间')),
                ('modTime', models.DateTimeField(auto_now=True, db_column='modTime', verbose_name='修改时间')),
            ],
            options={
                'db_table': 'tb4_data_keyword',
            },
        ),
        migrations.CreateModel(
            name='Tb4MockHttp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mockId', models.CharField(db_column='mockId', default='', max_length=50, unique=True, verbose_name='mock的ID')),
                ('title', models.CharField(db_column='title', default='', max_length=500, verbose_name='标题')),
                ('businessLineId', models.IntegerField(db_column='businessLineId', default=1, verbose_name='业务线id')),
                ('moduleId', models.IntegerField(db_column='moduleId', default=1, verbose_name='模块id')),
                ('uriKey', models.CharField(db_column='uriKey', default='', max_length=50, verbose_name='mock的服务')),
                ('tagKey', models.CharField(db_column='tagKey', default='common', max_length=50, verbose_name='mock的tag的key')),
                ('reqMethod', models.CharField(db_column='reqMethod', default='GET', max_length=20, verbose_name='请求Method')),
                ('reqUrl', models.CharField(db_column='reqUrl', default='/', max_length=255, verbose_name='请求Url')),
                ('reqParam', models.CharField(db_column='reqParam', default='', max_length=255, verbose_name='请求行参数')),
                ('reqHeader', models.CharField(db_column='reqHeader', default='', max_length=3000, verbose_name='请求头dict')),
                ('reqBody', models.TextField(db_column='reqBody', default='', verbose_name='请求体')),
                ('respStatusCode', models.CharField(db_column='respStatusCode', default='', max_length=5, verbose_name='状态码')),
                ('respStatusReason', models.CharField(db_column='respStatusReason', default='', max_length=50, verbose_name='状态文本')),
                ('respContentType', models.CharField(db_column='respContentType', default='', max_length=100, verbose_name='响应类型-html json等')),
                ('respBody', models.TextField(db_column='respBody', default='', verbose_name='响应体')),
                ('respCookie', models.CharField(db_column='respCookie', default='', max_length=2048, verbose_name='设置cookie到请求端，json')),
                ('respHeader', models.CharField(db_column='respHeader', default='', max_length=2048, verbose_name='设置header到请求端，json')),
                ('respCharset', models.CharField(db_column='respCharset', default='', max_length=20, verbose_name='响应编码')),
                ('mockMode', models.IntegerField(db_column='mockMode', default=0, verbose_name='mock模式 0 普通mormal模式 1 高级advanced模式')),
                ('advancedPythonCode', models.TextField(db_column='advancedPythonCode', default='', verbose_name='高级模式的code')),
                ('interfaceIds', models.TextField(db_column='interfaceIds', default='', verbose_name='接口ID列表，例如HTTP_INTERFACE_1,HTTP_INTERFACE_2,')),
                ('state', models.IntegerField(default=1, verbose_name='状态 0删除 1有效')),
                ('addBy', models.CharField(db_column='addBy', max_length=25, null=True, verbose_name='添加者登录名')),
                ('modBy', models.CharField(db_column='modBy', max_length=25, null=True, verbose_name='修改者登录名')),
                ('addTime', models.DateTimeField(auto_now_add=True, db_column='addTime', verbose_name='创建时间')),
                ('modTime', models.DateTimeField(auto_now=True, db_column='modTime', verbose_name='修改时间')),
            ],
            options={
                'db_table': 'tb4_mock_http',
            },
        ),
        migrations.CreateModel(
            name='Tb4MockHttpInvokeHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mockId', models.CharField(db_column='mockId', default='', max_length=50, verbose_name='mock的ID')),
                ('title', models.CharField(db_column='title', default='', max_length=500, verbose_name='标题')),
                ('businessLineId', models.IntegerField(db_column='businessLineId', default=1, verbose_name='业务线id')),
                ('moduleId', models.IntegerField(db_column='moduleId', default=1, verbose_name='模块id')),
                ('uriKey', models.CharField(db_column='uriKey', default='', max_length=50, verbose_name='mock的服务')),
                ('tagKey', models.CharField(db_column='tagKey', default='common', max_length=50, verbose_name='mock的tag的key')),
                ('reqMethod', models.CharField(db_column='reqMethod', default='GET', max_length=20, verbose_name='请求Method')),
                ('reqUrl', models.CharField(db_column='reqUrl', default='/', max_length=255, verbose_name='请求Url')),
                ('reqParam', models.CharField(db_column='reqParam', default='', max_length=255, verbose_name='请求行参数')),
                ('reqHeader', models.CharField(db_column='reqHeader', default='', max_length=3000, verbose_name='请求头dict')),
                ('reqBody', models.TextField(db_column='reqBody', default='', verbose_name='请求体')),
                ('respStatusCode', models.CharField(db_column='respStatusCode', default='200', max_length=5, verbose_name='状态码')),
                ('respStatusReason', models.CharField(db_column='respStatusReason', default='OK', max_length=50, verbose_name='状态文本')),
                ('respContentType', models.CharField(db_column='respContentType', default='', max_length=100, verbose_name='响应类型-html json等')),
                ('respBody', models.TextField(db_column='respBody', default='', verbose_name='响应体')),
                ('respCookie', models.CharField(db_column='respCookie', default='', max_length=2048, verbose_name='设置cookie到请求端，json')),
                ('respHeader', models.CharField(db_column='respHeader', default='', max_length=2048, verbose_name='设置header到请求端，json')),
                ('respCharset', models.CharField(db_column='respCharset', default='utf8', max_length=20, verbose_name='响应编码')),
                ('mockMode', models.IntegerField(db_column='mockMode', default=0, verbose_name='mock模式 0 普通mormal模式 1 高级advanced模式')),
                ('advancedPythonCode', models.TextField(db_column='advancedPythonCode', default='', verbose_name='高级模式的code')),
                ('fromHostIp', models.CharField(db_column='fromHostIp', default='', max_length=16, verbose_name='请求来源IP')),
                ('httpConfKey', models.CharField(db_column='httpConfKey', default='', max_length=16, verbose_name='录制来源环境的key')),
                ('actualReqUrl', models.CharField(db_column='actualReqUrl', default='/', max_length=255, verbose_name='实际请求Url')),
                ('actualReqParam', models.CharField(db_column='actualReqParam', default='', max_length=255, verbose_name='实际请求行参数')),
                ('actualReqHeader', models.CharField(db_column='actualReqHeader', default='', max_length=3000, verbose_name='实际请求头dict')),
                ('actualReqBody', models.TextField(db_column='actualReqBody', default='', verbose_name='实际请求体')),
                ('actualRespStatusCode', models.CharField(db_column='actualRespStatusCode', default='200', max_length=5, verbose_name='实际状态码')),
                ('actualRespStatusReason', models.CharField(db_column='actualRespStatusReason', default='OK', max_length=50, verbose_name='实际状态文本')),
                ('actualRespContentType', models.CharField(db_column='actualRespContentType', default='', max_length=100, verbose_name='实际响应类型-html json等')),
                ('actualRespBody', models.TextField(db_column='actualRespBody', default='', verbose_name='实际响应体')),
                ('actualRespCookie', models.CharField(db_column='actualRespCookie', default='', max_length=2048, verbose_name='实际设置cookie到请求端')),
                ('actualRespCharset', models.CharField(db_column='actualRespCharset', default='', max_length=20, verbose_name='实际响应编码')),
                ('state', models.IntegerField(default=1, verbose_name='状态 0删除 1有效')),
                ('addBy', models.CharField(db_column='addBy', max_length=25, null=True, verbose_name='添加者登录名')),
                ('modBy', models.CharField(db_column='modBy', max_length=25, null=True, verbose_name='修改者登录名')),
                ('addTime', models.DateTimeField(auto_now_add=True, db_column='addTime', verbose_name='创建时间')),
                ('modTime', models.DateTimeField(auto_now=True, db_column='modTime', verbose_name='修改时间')),
            ],
            options={
                'db_table': 'tb4_mock_http_invoke_history',
            },
        ),
        migrations.CreateModel(
            name='Tb4MockTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagKey', models.CharField(db_column='tagKey', default='', max_length=50, unique=True, verbose_name='mock的tag的key')),
                ('tagAlias', models.CharField(db_column='tagAlias', default='', max_length=200, unique=True, verbose_name='mock的tag的描述')),
                ('state', models.IntegerField(default=1, verbose_name='状态 0删除 1有效')),
                ('addBy', models.CharField(db_column='addBy', max_length=25, null=True, verbose_name='添加者登录名')),
                ('modBy', models.CharField(db_column='modBy', max_length=25, null=True, verbose_name='修改者登录名')),
                ('addTime', models.DateTimeField(auto_now_add=True, db_column='addTime', verbose_name='创建时间')),
                ('modTime', models.DateTimeField(auto_now=True, db_column='modTime', verbose_name='修改时间')),
            ],
            options={
                'db_table': 'tb4_mock_tag',
            },
        ),
        migrations.CreateModel(
            name='Tb4StatisticTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('businessLineId', models.IntegerField(db_column='businessLineId', default=0, verbose_name='业务线id')),
                ('moduleId', models.IntegerField(db_column='moduleId', default=0, verbose_name='模块id')),
                ('title', models.CharField(db_column='title', default='', max_length=255, verbose_name='统计任务标题')),
                ('descText', models.CharField(db_column='descText', default='', max_length=2000, verbose_name='统计任务描述')),
                ('state', models.IntegerField(default=1, verbose_name='状态 0删除 1有效')),
                ('addBy', models.CharField(db_column='addBy', max_length=25, null=True, verbose_name='添加者登录名')),
                ('modBy', models.CharField(db_column='modBy', max_length=25, null=True, verbose_name='修改者登录名')),
                ('addTime', models.DateTimeField(auto_now_add=True, db_column='addTime', verbose_name='创建时间')),
                ('modTime', models.DateTimeField(auto_now=True, db_column='modTime', verbose_name='修改时间')),
            ],
            options={
                'db_table': 'tb4_statistic_task',
            },
        ),
        migrations.CreateModel(
            name='Tb4StatisticTaskExecuteInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statisticTaskId', models.IntegerField(db_column='statisticTaskId', default=0, verbose_name='统计任务Id')),
                ('businessLineId', models.IntegerField(db_column='businessLineId', default=0, verbose_name='业务线id')),
                ('moduleId', models.IntegerField(db_column='moduleId', default=0, verbose_name='模块id')),
                ('title', models.CharField(db_column='title', default='', max_length=255, verbose_name='统计任务标题')),
                ('descText', models.CharField(db_column='descText', default='', max_length=2000, verbose_name='统计任务描述')),
                ('executeDetailText', models.TextField(db_column='executeDetailText', default='', verbose_name='统计任务执行详情')),
                ('testResult', models.CharField(db_column='testResult', default='', max_length=10, verbose_name='PASS/FAIL/EXCEPTION/ERROR')),
                ('codeCoverage', models.FloatField(db_column='codeCoverage', default=0.0, verbose_name='代码覆盖率')),
                ('executeStartTime', models.DateTimeField(db_column='executeStartTime', verbose_name='执行开始时间')),
                ('executeTaketime', models.IntegerField(db_column='executeTaketime', default=0, verbose_name='执行耗时单位秒')),
                ('httpConfKey', models.CharField(db_column='httpConfKey', default='', max_length=50, verbose_name='执行环境key')),
                ('executeType', models.CharField(db_column='executeType', default='', max_length=20, verbose_name='执行类型pipeline/daily/manual')),
                ('executeBy', models.CharField(db_column='executeBy', default='', max_length=30, verbose_name='执行人的loginName')),
                ('comments', models.CharField(db_column='comments', default='', max_length=4000, verbose_name='备注')),
                ('reason', models.CharField(db_column='reason', default='', max_length=4000, verbose_name='执行失败的原因等')),
                ('state', models.IntegerField(default=1, verbose_name='状态 0删除 1有效')),
                ('addBy', models.CharField(db_column='addBy', max_length=25, null=True, verbose_name='添加者登录名')),
                ('modBy', models.CharField(db_column='modBy', max_length=25, null=True, verbose_name='修改者登录名')),
                ('addTime', models.DateTimeField(auto_now_add=True, db_column='addTime', verbose_name='创建时间')),
                ('modTime', models.DateTimeField(auto_now=True, db_column='modTime', verbose_name='修改时间')),
            ],
            options={
                'db_table': 'tb4_statistic_task_execute_info',
            },
        ),
    ]
