try:
    from credentials import *
except ImportError:
    GOOGLE_API_KEY = 'replace_with_key'

GOOGLE_PAGESPEED_URL = 'https://www.googleapis.com/pagespeedonline/v2/runPagespeed'