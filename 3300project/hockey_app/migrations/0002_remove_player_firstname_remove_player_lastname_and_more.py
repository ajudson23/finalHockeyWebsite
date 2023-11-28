from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('hockey_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='firstName',
        ),
        migrations.RemoveField(
            model_name='player',
            name='lastName',
        ),
        migrations.AddField(
            model_name='player',
            name='name',
            field=models.CharField(default='Name', max_length=200, verbose_name='First & last name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='player',
            name='email',
            field=models.CharField(max_length=200, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='player',
            name='phoneNum',
            field=models.CharField(max_length=200, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='player',
            name='teamLevel',
            field=models.CharField(choices=[('Advanced', 'Advanced'), ('Intermediate', 'Intermediate'), ('N/A', 'N/A')], max_length=200, verbose_name='Team Level'),
        ),
        migrations.AlterField(
            model_name='player',
            name='teamName',
            field=models.CharField(choices=[('Wardique', 'Wardique'), ('Tochka', 'Tochka'), ('Palmer', 'Palmer'), ('Bristol', 'Bristol'), ('Waffels', 'Waffels'), ('Tonys', 'Tonys'), ('Platinum', 'Platinum'), ('N/A', 'N/A')], max_length=200, verbose_name='Team Name'),
        ),
    ]
