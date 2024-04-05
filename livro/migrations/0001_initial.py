# Generated by Django 4.2.11 on 2024-04-05 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Autores",
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
                ("nome", models.CharField(max_length=150)),
                ("sobrenome", models.CharField(max_length=150)),
            ],
            options={
                "verbose_name_plural": "Autores",
            },
        ),
        migrations.CreateModel(
            name="Editora",
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
                ("nome", models.CharField(max_length=150)),
                ("cnpj", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Genero",
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
                ("nome", models.CharField(max_length=150)),
            ],
            options={
                "verbose_name_plural": "Generos",
            },
        ),
        migrations.CreateModel(
            name="Livro",
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
                ("isbn", models.IntegerField()),
                ("titulo", models.CharField(max_length=150)),
                ("valor", models.FloatField()),
                ("estoque", models.IntegerField()),
                ("descricao", models.CharField(max_length=200)),
                ("autores", models.ManyToManyField(to="livro.autores")),
                (
                    "editora",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="livro.editora",
                    ),
                ),
                (
                    "id_genero",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="livro.genero",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Usuario",
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
                ("nome", models.CharField(max_length=150)),
                ("sobrenome", models.CharField(max_length=150)),
                ("endereco", models.CharField(max_length=150)),
                ("email", models.CharField(max_length=150)),
                ("telefone", models.IntegerField()),
                ("cpf", models.IntegerField()),
                ("id_livros", models.ManyToManyField(to="livro.livro")),
            ],
        ),
        migrations.CreateModel(
            name="Pedidos",
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
                ("data", models.DateTimeField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("PENDENTE", "Pendente"),
                            ("EM_PROCESSAMENTO", "Em Processamento"),
                            ("CONCLUIDO", "Concluído"),
                            ("CANCELADO", "Cancelado"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="livro.usuario"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Pedidos",
            },
        ),
    ]