# Generated by Django 1.11.29 on 2020-11-09 21:35

from django.db import migrations
import django.db.models.deletion
import sentry.db.models.fields.foreignkey


class Migration(migrations.Migration):
    # This flag is used to mark that a migration shouldn't be automatically run in
    # production. We set this to True for operations that we think are risky and want
    # someone from ops to run manually and monitor.
    # General advice is that if in doubt, mark your migration as `is_dangerous`.
    # Some things you should always mark as dangerous:
    # - Large data migrations. Typically we want these to be run manually by ops so that
    #   they can be monitored. Since data migrations will now hold a transaction open
    #   this is even more important.
    # - Adding columns to highly active tables, even ones that are NULL.
    is_dangerous = False

    # This flag is used to decide whether to run this migration in a transaction or not.
    # By default we prefer to run in a transaction, but for migrations where you want
    # to `CREATE INDEX CONCURRENTLY` this needs to be set to False. Typically you'll
    # want to create an index concurrently when adding one to an existing table.
    atomic = True

    dependencies = [
        ("sentry", "0125_add_platformexternalissue_project_id"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.AddField(
                    model_name="platformexternalissue",
                    name="group",
                    field=sentry.db.models.fields.foreignkey.FlexibleForeignKey(
                        db_constraint=False,
                        db_index=False,
                        null=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sentry.Group",
                    ),
                ),
                migrations.RemoveField(
                    model_name="platformexternalissue",
                    name="group_id",
                ),
                migrations.AlterUniqueTogether(
                    name="platformexternalissue",
                    unique_together=set([("group", "service_type")]),
                ),
            ]
        )
    ]
