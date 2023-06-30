from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, help_text='Разместите фото для объявления', null=True, upload_to='images/', verbose_name='фото')),
                ('title', models.CharField(help_text='введите название товара', max_length=200, verbose_name='Название товара')),
                ('price', models.PositiveIntegerField(help_text='Добавьте цену товара', verbose_name='Цена товара')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Введите время создания объявления', verbose_name='Время создания объявления')),
                ('description', models.CharField(blank=True, help_text='Введите описание товара', max_length=1000, null=True, verbose_name='Описание товара')),
                ('author', models.ForeignKey(help_text='Выберите автора объявления', on_delete=django.db.models.deletion.CASCADE, related_name='ads', to=settings.AUTH_USER_MODEL, verbose_name='Автор объявления')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(help_text='Оставьте свой комментарий здесь', max_length=1000, verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Введите время создания комментария', verbose_name='Время создания комментария')),
                ('ad', models.ForeignKey(help_text='Объявление, к которому относится комментарий', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='ads.ad', verbose_name='Объявление')),
                ('author', models.ForeignKey(help_text='Выберите автора комментария', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='Автор комментария')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'ordering': ('-created_at',),
            },
        ),
    ]
