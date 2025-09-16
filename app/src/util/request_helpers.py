from http.client import RemoteDisconnected

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


def requests_retry_session(
    retries=3,
    backoff_factor=0.3,
    status_forcelist=(500, 502, 504),
    session=None,
):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
        allowed_methods=frozenset(['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'OPTIONS']),
        raise_on_status=False,
    )
    adapter = HTTPAdapter(max_retries=retry)

    session.mount('http://', adapter)
    session.mount('https://', adapter)

    return session


def get_url_content(url: str) -> str:
    """Get url content.

    Attrs:
        url - string representation of site to get content on.

    Returns:
        bytes object representing site content.

    """
    try:
        session = requests_retry_session()
        response = session.get(url, timeout=10)
        response.raise_for_status()

    except RemoteDisconnected:
        print("RemoteDisconnected error occurred. Consider retrying the request.")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

    return response.content
