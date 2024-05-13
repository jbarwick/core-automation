from .._version import __version__
from boto3 import client

def title():
    """
    Print the title of the program.
    """
    print(f"Core Automation v{__version__}")

def other_util():
    """
    Placeholder for other utility functions.
    """
    pass

def download_facts() -> bool:
    """
    Download facts from the S3 bucket.

    Returns: False if there is an error, True otherwise.
    """
    try:
        s3 = client('s3')
        s3.download_file('sck-core-automation', 'facts.txt', '/tmp/facts.txt')
        print("Downloaded facts.txt")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
