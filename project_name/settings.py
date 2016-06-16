"""
Django settings for {{ project_name }} project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.utils.translation import ugettext_lazy as _
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
PROJECT_PATH = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '{{ secret_key }}'

SITE_ID = 1
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG
THUMBNAIL_DEBUG = DEBUG

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIR, 'templates'),
)

ALLOWED_HOSTS = ['*']

MEDIA_ROOT = os.path.join(PROJECT_PATH, r'media')
MEDIA_URL = r'/media/'


# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(PROJECT_PATH, 'static')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.FileSystemFinder',
    'pipeline.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
    'compressor.finders.CompressorFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)



# Application definition

INSTALLED_APPS = (
    '{{ project_name }}',
    'sorl.thumbnail',

    # enable the admin
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',

    # The CMS apps
    #'fluent_pages',
    '{{ project_name }}.apps.FluentPagesConfig',

    # Required dependencies
    'mptt',
    'parler',
    'polymorphic',
    'polymorphic_tree',

    # main publication app
    'publication_backbone',

    # Optional widget pages via django-fluent-contents
    'fluent_pages.pagetypes.fluentpage',
    'fluent_contents',
    #'fluent_contents.plugins.text',
    'django_wysiwyg',

    # Optional other CMS page types
    'fluent_pages.pagetypes.redirectnode',

    'compressor',
    #'constance',
    '{{ project_name }}.apps.ConstanceConfig',

    'constance.backends.database',
    'django_mptt_admin',
    'salmonella',

    # CKEditor
    'ckeditor',

    # Publication Backbone Plugins
    'publication_backbone.plugins.text',
    'publication_backbone.plugins.content_gap',
    'publication_backbone.plugins.snippet',
    'publication_backbone.plugins.yandex_map',
    'publication_backbone.plugins.file',
    'publication_backbone.plugins.picture',
    #'publication_backbone.plugins.video',
    'publication_backbone.plugins.form_designer_plugin',
    'publication_backbone.plugins.promo',
    'publication_backbone.plugins.sub_menu',
    'publication_backbone.plugins.sitemap',

    #'publication_backbone.interview',
    'publication_backbone.apps.InterviewConfig',
    'publication_backbone.apps.QuizConfig',

    # Beautiful fields
    'beautiful_fields',

    # CSS and JS builder
    'twitter_bootstrap',
    'pipeline',

    'any_imagefield',
    'any_urlfield',
    #'grappelli',
    #'filebrowser',

    #'form_designer',
    '{{ project_name }}.apps.FormDesignerConfig',

    # Search
    'publication_backbone.search.backends.haystack_backend',
    'haystack',
    'elasticstack',
)

MIDDLEWARE_CLASSES = (
    'pipeline.middleware.MinifyHTMLMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.debug',
    'django.core.context_processors.csrf',
    'django.core.context_processors.tz',
    #    'constance.context_processors.config',
    #'sekizai.context_processors.sekizai',
)

ROOT_URLCONF = '{{ project_name }}.urls'

WSGI_APPLICATION = '{{ project_name }}.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_PATH, '{{ project_name }}.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True



DJANGO_WYSIWYG_FLAVOR = "ckeditor"
#DJANGO_WYSIWYG_MEDIA_URL
DJANGO_WYSIWYG_MEDIA_URL = STATIC_URL + "ckeditor/"

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'


PIPELINE_COMPILERS = (
  'pipeline.compilers.less.LessCompiler',
  'pipeline.compilers.coffee.CoffeeScriptCompiler',
)

STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'

if DEBUG:
    PIPELINE_LESS_ARGUMENTS = "-ru --source-map --include-path=../../../../../src/publicationbackbone/publication_backbone/:../../../../../lib/python2.7/site-packages/publication_backbone/:../../../../../lib/python2.7/site-packages/twitter_bootstrap/"
else:
    PIPELINE_LESS_ARGUMENTS = "-ru --clean-css --compress --include-path=../../../../../lib/python2.7/site-packages/publication_backbone/:../../../../../lib/python2.7/site-packages/twitter_bootstrap/"

PIPELINE_CSS = {
    'styles': {
        'source_filenames': (
            'src/less/styles.less',
        ),
        'output_filename': 'css/styles.css',
        'extra_context': {
            'media': 'screen',
        },
    },
}

PIPELINE_JS = {
    'bootstrap': {
        'source_filenames': (
          'twitter_bootstrap/js/transition.js',
          'twitter_bootstrap/js/alert.js',
          'twitter_bootstrap/js/button.js',
          'twitter_bootstrap/js/carousel.js',
          'twitter_bootstrap/js/collapse.js',
          'twitter_bootstrap/js/dropdown.js',
          'twitter_bootstrap/js/modal.js',
          'twitter_bootstrap/js/tooltip.js',
          'twitter_bootstrap/js/popover.js',
          'twitter_bootstrap/js/scrollspy.js',
          'twitter_bootstrap/js/tab.js',
          'twitter_bootstrap/js/affix.js',
        ),
        'output_filename': 'js/bootstrap.js',
    },
}

THUMBNAIL_ENGINE = 'publication_backbone.utils.sorl_pil_engine.Engine'

FLUENT_PAGES_TEMPLATE_DIR = os.path.join(TEMPLATE_DIRS[0], 'pages')

CKEDITOR_SETTINGS = {
    'language': '',
    'toolbar_CMS': [
                ['ShowBlocks'],
                ['NewPage', 'Preview', 'Print'],
                ['Cut', 'Copy', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo'],
                ['Find', 'Replace'],
                ['Source', 'Maximize'],
                '/',
                ['Bold', 'Italic', 'Underline', 'Strike', '-', 'Subscript', 'Superscript', '-', 'RemoveFormat'],
                ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
                '/',
                ['Format', 'Styles'],
                ['TextColor', 'BGColor'],
                ['Link', 'Unlink', 'Anchor'],
                ['Table', 'HorizontalRule', 'SpecialChar', 'Iframe'],
            ],
    'skin': 'moono',
}

CKEDITOR_CONFIGS = {'default': {
    'toolbar': [
                ['ShowBlocks'],
                ['Cut', 'Copy', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo'],
                ['Find', 'Replace'],
                ['Source', 'Maximize'],
                '/',
                ['Bold', 'Italic', 'Underline', 'Strike', '-', 'Subscript', 'Superscript', '-', 'RemoveFormat'],
                ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
                '/',
                ['Format', 'Styles', 'Font', 'FontSize'],
                ['TextColor', 'BGColor'],
                ['Link', 'Unlink', 'Anchor'],
                ['Table', 'HorizontalRule', 'SpecialChar', 'Iframe'],
            ],
    'skin': 'moono',
}}

CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'

FILEBROWSER_OVERWRITE_EXISTING = False

COMPRESS_OUTPUT_DIR = 'publication_backbone_cache'

# haystack search settings
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': '{{ project_name }}',
    }
}

PUBLICATION_BACKBONE_SEARCH_BACKENDS = [
    'publication_backbone.search.backends.haystack_backend.haystack_search.HaystackSearchBackend',
]

HAYSTACK_SEARCH_RESULTS_PER_PAGE = 15
#HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

CONSTANCE_CONFIG = {
    'TSG_ADMINS_LIST': ("", _("List of e-mail addresses of the administrators involved in the consideration of the completed information on the MC and the HOA. Use a semicolon to separate addresses.")),
    'META_CONTAINER': ("", _("Meta block")),
    'COUNTERS': ("", _("Counter without image")),
}

# EMAIL SETTINGS
EMAIL_USE_TLS = False
EMAIL_HOST = 'sample.com'
EMAIL_HOST_USER = 'admin@sample.com'
EMAIL_HOST_PASSWORD = 'password'
EMAIL_PORT = 25
DEFAULT_FROM_EMAIL = 'admin@sample.com'
DEFAULT_TO_EMAIL = 'admin@sample.com'