"""
Thin wrapper around django-storages' S3Boto3Storage, pointed at Supabase
Storage's S3-compatible endpoint (configured in settings via SUPABASE_STORAGE_*
env vars). Using a dedicated class - rather than referencing S3Boto3Storage
directly in STORAGES - means we can swap the underlying provider later
(e.g. AWS S3, Cloudflare R2) by changing this one file.
"""

from storages.backends.s3boto3 import S3Boto3Storage
from whitenoise.storage import CompressedManifestStaticFilesStorage


class SupabaseMediaStorage(S3Boto3Storage):
    location = "media"
    file_overwrite = False


class LenientManifestStaticFilesStorage(CompressedManifestStaticFilesStorage):
    """
    Falls back to a file's unhashed name instead of raising a 500 when its
    entry is missing from staticfiles.json - collectstatic's manifest can end
    up incomplete for a handful of files (a known Django/whitenoise edge case
    around CSS url() post-processing passes) even when the command reports
    success, and whitenoise already serves the unhashed path correctly.
    """

    manifest_strict = False
