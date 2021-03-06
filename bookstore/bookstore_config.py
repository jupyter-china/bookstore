"""Configuration settings for bookstore"""
from traitlets import Int, Unicode
from traitlets.config import LoggingConfigurable


class BookstoreSettings(LoggingConfigurable):
    """Configuration settings for archival, publishing, and scheduling.

    Settings include storage directory locations, S3 authentication,
    additional S3 settings, and Bookstore resources.

    S3 authentication settings can be set, or they can be left unset when
    IAM is used.

    Attributes
    ----------

    - workspace_prefix : str('workspace')
        the directory to use for user workspace storage
    - published_prefix : str('published')
        the directory to use for published notebook storage
    - s3_access_key_id : str, optional
        environment variable ``JPYNB_S3_ACCESS_KEY_ID``
    - s3_secret_access_key : str, optional
        environment variable ``JPYNB_S3_SECRET_ACCESS_KEY``
    - s3_endpoint_url : str("https://s3.amazonaws.com")
        environment variable ``JPYNB_S3_ENDPOINT_URL``
    - s3_region_name : str("us-east-1")
        environment variable ``JPYNB_S3_REGION_NAME``
    - s3_bucket : str("")
        bucket name, environment variable ``JPYNB_S3_BUCKET``
    - max_threads : int(16)
        Maximum threads from the threadpool available to do S3 read and writes
    """

    workspace_prefix = Unicode("workspace", help="Prefix for the live workspace notebooks").tag(
        config=True
    )
    published_prefix = Unicode("published", help="Prefix for published notebooks").tag(config=True)

    s3_access_key_id = Unicode(
        help="S3/AWS access key ID", allow_none=True, default_value=None
    ).tag(config=True, env="JPYNB_S3_ACCESS_KEY_ID")
    s3_secret_access_key = Unicode(
        help="S3/AWS secret access key", allow_none=True, default_value=None
    ).tag(config=True, env="JPYNB_S3_SECRET_ACCESS_KEY")

    s3_endpoint_url = Unicode("https://s3.amazonaws.com", help="S3 endpoint URL").tag(
        config=True, env="JPYNB_S3_ENDPOINT_URL"
    )
    s3_region_name = Unicode("us-east-1", help="Region name").tag(
        config=True, env="JPYNB_S3_REGION_NAME"
    )
    s3_bucket = Unicode("", help="Bucket name to store notebooks").tag(
        config=True, env="JPYNB_S3_BUCKET"
    )

    max_threads = Int(
        16, help="Maximum number of threads for the threadpool allocated for S3 read/writes"
    ).tag(config=True)


def validate_bookstore(settings: BookstoreSettings):
    """Validate bookstore configuration settings.

    Parameters
    ----------
    settings: bookstore.bookstore_config.BookstoreSettings
        The instantiated `Settings` object to be validated.
    """
    general_settings = [settings.s3_bucket != "", settings.s3_endpoint_url != ""]
    archive_settings = [settings.workspace_prefix != ""]
    published_settings = [settings.published_prefix != ""]

    validation_checks = {
        "bookstore_valid": all(general_settings),
        "archive_valid": all(archive_settings),
        "publish_valid": all(published_settings),
    }
    return validation_checks
