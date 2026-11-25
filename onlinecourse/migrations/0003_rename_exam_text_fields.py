from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("onlinecourse", "0002_choice_submission_question_choice_question"),
    ]

    operations = [
        migrations.RenameField("question", "content", "question_text"),
        migrations.RenameField("choice", "content", "choice_text"),
    ]