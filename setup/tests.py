from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'setup/static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

print(STATIC_ROOT)