from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserFollows(models.Model):
    # Your UserFollows model definition goes here
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following'
    )

    followed_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='followed_by'
    )

    def __str__(self):
        return f'{self.followed_user.username}'

    class Meta:
        # ensures we don't get multiple UserFollows instances
        # for unique user-user_followed pairs
        unique_together = ('user', 'followed_user', )
