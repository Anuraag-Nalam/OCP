from django.db import models
class Blogpost(models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=70)
    head0=models.CharField(max_length=1000)
    chead0=models.CharField(max_length=1000)
    head1=models.CharField(max_length=1000)
    chead1=models.CharField(max_length=1000)
    head2=models.CharField(max_length=1000)
    chead2=models.CharField(max_length=1000)
    pub_date=models.DateField()
    image=models.ImageField(upload_to='shop/images',default='')
    def __str__(self):
        return self.title
