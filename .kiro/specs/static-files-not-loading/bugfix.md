# Bugfix Requirements Document

## Introduction

CSS stylesheets and image files fail to load in the Django application, leaving the UI unstyled and broken. The root causes are: (1) no static file serving middleware (WhiteNoise) is configured for production, (2) `python-decouple` is missing from `requirements.txt` which can prevent the app from starting at all on a fresh install, and (3) `collectstatic` has never been run so `STATIC_ROOT` is empty. Together these mean static assets are never reachable — either the app crashes on startup or the web server has no files to serve.

## Bug Analysis

### Current Behavior (Defect)

1.1 WHEN the application runs with `DEBUG=False` (production) THEN the system returns HTTP 404 for all `/static/` URLs because Django does not serve static files in production and no middleware (e.g. WhiteNoise) is present to do so

1.2 WHEN `collectstatic` has not been run THEN the system has an empty `staticfiles/` directory, so even a correctly configured static file server finds no files to serve

1.3 WHEN the project is installed from `requirements.txt` on a fresh environment THEN the system fails to start because `python-decouple` is imported in `settings.py` but is not listed as a dependency

1.4 WHEN the application runs with `DEBUG=True` and static files are referenced via `{% static %}` template tags THEN the system serves files correctly from `STATICFILES_DIRS` through `django.contrib.staticfiles`, masking the production misconfiguration during local development

### Expected Behavior (Correct)

2.1 WHEN the application runs with `DEBUG=False` THEN the system SHALL serve all `/static/` URLs correctly, returning the appropriate CSS, JS, and image files with HTTP 200

2.2 WHEN `collectstatic` is run THEN the system SHALL copy all static assets from `STATICFILES_DIRS` into `STATIC_ROOT` (`staticfiles/`) so they are available for serving

2.3 WHEN the project is installed from `requirements.txt` THEN the system SHALL start successfully because all required packages including `python-decouple` and `whitenoise` are listed

2.4 WHEN WhiteNoise middleware is added to `MIDDLEWARE` THEN the system SHALL serve compressed and cached static files in both development and production without requiring a separate web server configuration

### Unchanged Behavior (Regression Prevention)

3.1 WHEN the application runs with `DEBUG=True` THEN the system SHALL CONTINUE TO serve static files from `STATICFILES_DIRS` via `django.contrib.staticfiles` as it does today

3.2 WHEN media files are uploaded and accessed via `MEDIA_URL` THEN the system SHALL CONTINUE TO serve them correctly in development via the existing `static(MEDIA_URL, ...)` URL pattern in `urls.py`

3.3 WHEN existing URL patterns are accessed (admin, auth, project, service routes) THEN the system SHALL CONTINUE TO resolve and respond correctly after the static file fix is applied

3.4 WHEN templates use `{% static 'css/style.css' %}` or similar tags THEN the system SHALL CONTINUE TO generate correct URLs pointing to `/static/css/style.css`
