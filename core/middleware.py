from django.utils import translation

# TODO Implement this


class force_default_language_middleware:
    """
    Middleware that forces the language selected in the settings.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        translation.activate(translation.get_language())
        response = self.get_response(request)
        return response


class SetupTranslationsLang:
    """
    Middleware that sets up language based on user preferences.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response


class AccessLogsMiddleware:
    """
    Middleware that logs access to views.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response


class ResponseTimeMiddleware:
    """
    Middleware that tracks response time.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response
