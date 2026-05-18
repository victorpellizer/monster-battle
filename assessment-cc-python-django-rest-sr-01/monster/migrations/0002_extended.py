from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('monster', '0001_initial'),
    ]

    run_before = [
        ('monster', '0002_auto_20221226_2153'),
    ]

    operations = [
        migrations.AddField(
            model_name='monster',
            name='name',
            field=models.CharField(default='Unknown', max_length=100, verbose_name='Name'),
            preserve_default=False,
        ),
    ]
