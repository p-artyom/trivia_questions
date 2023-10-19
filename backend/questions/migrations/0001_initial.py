from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Question",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, db_index=True),
                ),
                (
                    "modified",
                    models.DateTimeField(blank=True, db_index=True, null=True),
                ),
                (
                    "id_question",
                    models.IntegerField(verbose_name="идентификатор вопроса"),
                ),
                ("question", models.TextField(verbose_name="текст вопроса")),
                ("answer", models.TextField(verbose_name="текст ответа")),
                (
                    "created_question_at",
                    models.DateTimeField(verbose_name="дата создания вопроса"),
                ),
            ],
            options={
                "verbose_name": "вопрос",
                "verbose_name_plural": "вопросы",
                "get_latest_by": "pk",
            },
        ),
    ]
