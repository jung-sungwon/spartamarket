from django.db import models
from accounts.models import User


class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    content = models.TextField(default="상품상세 내용")
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to="images/",
        blank=True,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="products",
        null=True,
    )

    def __str__(self):
        return self.name
