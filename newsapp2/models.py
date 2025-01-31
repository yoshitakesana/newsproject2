from django.db import models
from django.conf import settings

class NewsPost(models.Model):
    CATEGORY = (('スキンケア・コスメ','肌を愛でる毎日。注目のスキンケアとコスメをチェック'),
                ('怖い話','ゾクッとする恐怖体験、あなたの心を震わせる怪談'),
                ('人気のスイーツ','甘い幸せ、今食べたい人気スイーツをチェック！'),
                ('ライフハック','生活をもっと快適に！知って得するライフハック集'),
                ('今日のコーデ','今日のコーデで決まる！毎日のスタイルアイデア'),
                ('可愛い動物','癒される瞬間、可愛い動物たちの癒し動画＆写真')
                )


    title = models.CharField(
        max_length=100,
        verbose_name='タイトル')

    content = models.TextField(verbose_name='本文')

    posted_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='投稿日時')

    category = models.CharField(
        max_length=50,
        choices=CATEGORY,
        verbose_name='カテゴリ')

    likes = models.PositiveIntegerField(default=0)  # いいね数を保存するフィールド

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        'NewsPost',
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='記事'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='ユーザー'
    )
    content = models.TextField(verbose_name='コメント内容')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='作成日時')

    def __str__(self):
        return f'{self.user.username} - {self.content[:20]}'