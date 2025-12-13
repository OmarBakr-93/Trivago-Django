from .models import Settings


def my_footer(request):
  footer = Settings.objects.last()
  return {'footer': footer}