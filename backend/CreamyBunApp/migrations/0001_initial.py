# Generated by Django 3.2.14 on 2022-11-20 02:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_type', models.IntegerField(default=0)),
                ('description', models.CharField(default='no description', max_length=500)),
                ('image_url', models.CharField(default='image', max_length=1000)),
                ('inform_email', models.CharField(default='email', max_length=350)),
                ('advice', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Int',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('int_content', models.IntegerField(default=-1)),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.BigIntegerField(default=-1)),
                ('is_test', models.BooleanField(default=False)),
                ('receiver', models.BigIntegerField(default=-1)),
                ('current_state', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.BigIntegerField(default=-1)),
                ('question_type', models.IntegerField(default=0)),
                ('description', models.CharField(default='no description', max_length=500)),
                ('must_do', models.BooleanField(default=False)),
                ('answer', models.CharField(default='', max_length=10000)),
                ('standard_answer', models.CharField(default='', max_length=26)),
            ],
        ),
        migrations.CreateModel(
            name='Str',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('str_content', models.CharField(default='', max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='StringToString',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(default='', max_length=500)),
                ('value', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='TaskDict',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.BigIntegerField(default=-1)),
                ('task_status_for_user', models.IntegerField(default=0)),
                ('task_status_for_itself', models.IntegerField(default=-1)),
            ],
        ),
        migrations.CreateModel(
            name='FillBlankQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='CreamyBunApp.question')),
                ('min_answer_length', models.IntegerField(default=10000)),
                ('max_answer_length', models.IntegerField(default=0)),
            ],
            bases=('CreamyBunApp.question',),
        ),
        migrations.CreateModel(
            name='FrameSelectionQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='CreamyBunApp.question')),
                ('min_frame_number', models.IntegerField(default=100)),
                ('max_frame_number', models.IntegerField(default=0)),
            ],
            bases=('CreamyBunApp.question',),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='username', max_length=12)),
                ('password', models.CharField(default='password', max_length=18)),
                ('email', models.CharField(default='email', max_length=350)),
                ('avatar_url', models.CharField(default='image', max_length=1000)),
                ('mobile_number', models.CharField(default='', max_length=11)),
                ('donut_number', models.IntegerField(default=0)),
                ('credit_rank', models.IntegerField(default=1)),
                ('current_exp', models.IntegerField(default=0)),
                ('dark_mode', models.BooleanField(default=False)),
                ('today_violation', models.IntegerField(default=0)),
                ('is_today_sign_in', models.BooleanField(default=False)),
                ('continue_sign_in_days', models.IntegerField(default=0)),
                ('task_info_list', models.ManyToManyField(to='CreamyBunApp.TaskDict')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.BigIntegerField(default=-1)),
                ('task_name', models.CharField(default='task_name', max_length=40)),
                ('description', models.CharField(default='task_description', max_length=500)),
                ('task_type', models.IntegerField(default=-1)),
                ('answer_type', models.IntegerField(default=-1)),
                ('problem_total_number', models.IntegerField(default=-1)),
                ('finished_problem_number', models.IntegerField(default=0)),
                ('test_problem_number', models.IntegerField(default=0)),
                ('problem_number_for_single_receiver', models.IntegerField(default=-1)),
                ('star_rank', models.IntegerField(default=-1)),
                ('single_bonus', models.IntegerField(default=-1)),
                ('release_mode', models.IntegerField(default=0)),
                ('begin_time', models.CharField(default='begin_time', max_length=25)),
                ('end_time', models.CharField(default='end_time', max_length=25)),
                ('problem_list', models.ManyToManyField(to='CreamyBunApp.Problem')),
                ('receiver_list', models.ManyToManyField(to='CreamyBunApp.Int')),
            ],
        ),
        migrations.AddField(
            model_name='problem',
            name='material_path',
            field=models.ManyToManyField(to='CreamyBunApp.Str'),
        ),
        migrations.AddField(
            model_name='problem',
            name='question_list',
            field=models.ManyToManyField(to='CreamyBunApp.Question'),
        ),
        migrations.CreateModel(
            name='ChoiceQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='CreamyBunApp.question')),
                ('min_option_num', models.IntegerField(default=26)),
                ('max_option_num', models.IntegerField(default=0)),
                ('option_list', models.ManyToManyField(to='CreamyBunApp.StringToString')),
            ],
            bases=('CreamyBunApp.question',),
        ),
    ]
