# Generated by Django 4.2.4 on 2023-10-11 22:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('veiculo', '0002_alter_veiculo_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(auto_now_add=True)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descricao', models.CharField(max_length=500)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='anuncios_realizados', to=settings.AUTH_USER_MODEL)),
                ('veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='anuncios', to='veiculo.veiculo')),
            ],
        ),
    ]