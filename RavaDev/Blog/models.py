from django.db import models
from About import models as AboutModels

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='posts/', null=True, blank=True),
    author = models.ForeignKey(AboutModels.TeamMember, on_delete=models.SET_NULL, null=True),
    views = models.IntegerField(default=0)



    def __str__(self):
        return self.title
    
    def get_rate(self):
        reviews = Review.objects.filter(post=self)
        if reviews.exists():
            return sum(review.rating for review in reviews) / reviews.count()
        return 0
    
    def snippet(self):
        return self.content[:100] + '...'
    
class Review(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=100)
    rating = models.IntegerField()
    comment = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reviewer_name} - {self.post.title}"