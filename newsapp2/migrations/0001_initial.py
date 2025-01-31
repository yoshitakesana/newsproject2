# Generated by Django 4.2 on 2025-01-15 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='タイトル')),
                ('content', models.TextField(verbose_name='本文')),
                ('posted_at', models.DateTimeField(auto_now_add=True, verbose_name='投稿日時')),
                ('category', models.CharField(choices=[('スキンケア・コスメ', '肌を愛でる毎日。注目のスキンケアとコスメをチェック'), ('怖い話', 'ゾクッとする恐怖体験、あなたの心を震わせる怪談'), ('人気のスイーツ', '甘い幸せ、今食べたい人気スイーツをチェック！'), ('ライフハック', '生活をもっと快適に！知って得するライフハック集'), ('今日のコーデ', '今日のコーデで決まる！毎日のスタイルアイデア'), ('可愛い動物', '癒される瞬間、可愛い動物たちの癒し動画＆写真')], max_length=50, verbose_name='カテゴリ')),
            ],
        ),
    ]
