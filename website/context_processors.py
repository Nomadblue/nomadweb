from django.conf import settings

def google_analytics(request):
    ga_key = getattr(settings, 'GOOGLE_ANALYTICS_KEY', False)
    if not settings.DEBUG and ga_key:
        return {'google_analytics_key': ga_key}
    return {}

