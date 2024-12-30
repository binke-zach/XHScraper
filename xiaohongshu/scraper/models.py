from django.db import models

class ScraperTask(models.Model):
    keyword = models.CharField(max_length=255)
    xhs_id = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    result_image = models.ImageField(upload_to='scraper_results/', null=True, blank=True)

    def __str__(self):
        return f"Scraper Task {self.id} - {self.keyword} | {self.xhs_id}"

