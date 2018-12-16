# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-12-16 17:12
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0130_initialinternfeedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='initialinternfeedback',
            name='ip_address',
            field=models.GenericIPAddressField(default='127.0.0.1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='initialmentorfeedback',
            name='ip_address',
            field=models.GenericIPAddressField(default='127.0.0.1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='initialmentorfeedback',
            name='mentors_report',
            field=models.TextField(blank=True, null=True, verbose_name="(Optional) Please provide a paragraph for Outreachy coordinators and other mentors describing your intern's progress. This will be shared on the mentors mailing list, but will not be made public."),
        ),
        migrations.AddField(
            model_name='initialmentorfeedback',
            name='request_termination',
            field=models.BooleanField(default=False, help_text='Sometimes after several extensions, interns still do not put in a full-time effort. If you believe that your intern would not put in a full-time effort with a further extension, you may request to terminate the internship. The Outreachy organizers will be in touch to discuss the request.', verbose_name='Do you believe the internship should be terminated?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='initialmentorfeedback',
            name='termination_reason',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, help_text="Please elaborate on the efforts you have put in to get your intern back on track, and the results of those efforts. Tell us about your intern's work efforts, communication frequency, and meeting attendance since their last extension. Provide links to any work that is still in progress or has been completed since their last extension. Please let us know any additional information about why the internship should be terminated.", null=True, verbose_name='Why you feel the internship should be terminated?'),
        ),
        migrations.AlterField(
            model_name='initialmentorfeedback',
            name='progress_report',
            field=models.TextField(verbose_name="Please provide a paragraph describing your intern's progress on establishing communication with you, connecting to your FOSS community, and ramping up on their first tasks. This will only be shown to Outreachy organizers and Software Freedom Conservancy accounting staff."),
        ),
    ]
