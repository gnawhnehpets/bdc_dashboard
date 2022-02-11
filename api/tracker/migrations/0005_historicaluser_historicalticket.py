# Generated by Django 4.0.2 on 2022-02-10 18:43

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_rename_data_upload_completed_by_ticket_data_uploaded_completed_by_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalUser',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(db_index=True, max_length=254, verbose_name='Email')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('date_joined', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical user',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalTicket',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='Name of primary contact', max_length=100, verbose_name='Name')),
                ('email', models.EmailField(default='', max_length=254, verbose_name='Email')),
                ('organization', models.CharField(default='', help_text='Name of requesting organization', max_length=250, verbose_name='Organization')),
                ('study_name', models.CharField(default='', help_text='Name of Study or Dataset', max_length=250, verbose_name='Study Name')),
                ('study_id', models.CharField(default='', help_text='Please refer to Data Custodian Instructions for more information', max_length=100, validators=[django.core.validators.RegexValidator('^[a-z0-9][a-z0-9.]{0,59}[a-z0-9]$', 'Study ID format invalid')], verbose_name='Study ID')),
                ('consent_code', models.CharField(default='', help_text='Please refer to Data Custodian Instructions for more information', max_length=100, validators=[django.core.validators.RegexValidator('^[a-z0-9][a-z0-9.]{0,59}[a-z0-9]$', 'Consent Code format invalid')], verbose_name='Consent Code')),
                ('data_size', models.CharField(default='', help_text='Please provide an estimated size of your data set(s) (ex. 100 GB)', max_length=100, validators=[django.core.validators.RegexValidator('^[0-9]{1,5}(.[0-9]{1,5})?\\s?(MB|GB|TB|PB)$', 'Data Size format invalid. Please add a unit of measurement (MB, GB, TB, PB)')], verbose_name='Data Size')),
                ('dataset_description', models.CharField(blank=True, default='', help_text='Describe the dataset you are uploading', max_length=2500, verbose_name='Dataset Description')),
                ('google_email', models.EmailField(blank=True, default='', help_text="If you're uploading to Google, please provide your google email for access", max_length=254, verbose_name='Google Email')),
                ('aws_iam', models.CharField(blank=True, default='', help_text="If you're uploading to Amazon, please provide your AWS IAM (ex: arn:aws:iam::123456789012:user/username)", max_length=100, validators=[django.core.validators.RegexValidator('^arn:aws:iam::[0-9]{12}:user/[a-zA-Z0-9-_]{1,64}$', 'AWS IAM format invalid. Please use the following format: arn:aws:iam::123456789012:user/username')], verbose_name='AWS IAM')),
                ('is_test_data', models.BooleanField(blank=True, default=False, help_text='Check this box if this is test data', verbose_name='Is Test Data')),
                ('ticket_review_comment', models.CharField(blank=True, default='', help_text='Please provide a comment for approval or rejection', max_length=1000, verbose_name='Ticket Review Comment')),
                ('created_dt', models.DateTimeField(blank=True, editable=False, verbose_name='Created Date')),
                ('ticket_approved_dt', models.DateTimeField(blank=True, null=True, verbose_name='Intake Form Approved Date')),
                ('ticket_rejected_dt', models.DateTimeField(blank=True, null=True, verbose_name='Intake Form Rejected Date')),
                ('bucket_created_dt', models.DateTimeField(blank=True, null=True, verbose_name='Bucket Created Date')),
                ('data_uploaded_started_dt', models.DateTimeField(blank=True, null=True, verbose_name='Data Uploaded Started Date')),
                ('data_uploaded_completed_dt', models.DateTimeField(blank=True, null=True, verbose_name='Data Uploaded Completed Date')),
                ('data_accepted_dt', models.DateTimeField(blank=True, null=True, verbose_name='Gen3 Accepted Date')),
                ('ticket_approved_by', models.EmailField(default='', max_length=254, verbose_name='Ticket approved by')),
                ('ticket_rejected_by', models.EmailField(default='', max_length=254, verbose_name='Ticket rejected by')),
                ('bucket_created_by', models.EmailField(default='', max_length=254, verbose_name='Bucket created by')),
                ('data_uploaded_started_by', models.EmailField(default='', max_length=254, verbose_name='Data upload started by')),
                ('data_uploaded_completed_by', models.EmailField(default='', max_length=254, verbose_name='Data upload completed by')),
                ('data_accepted_by', models.EmailField(default='', max_length=254, verbose_name='Data accepted by')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('created_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical ticket',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
