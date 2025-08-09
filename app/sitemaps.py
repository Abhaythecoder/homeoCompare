from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        # Replace 'home' with your URL names (e.g., 'about', 'contact')
        return ['home', 'remedy_compare', 'allen_compare', 'about']

    def location(self, item):
        return reverse(item)
