import re


def validate_spf_string(spf: str) -> bool:
    """Validate an SPF string.

    Args:
        spf: The SPF string to validate.

    Returns:
        True if the SPF string is valid, False otherwise.
    """

    # Check for empty string
    if not spf:
        return False

    version_regex = re.compile(r"(?P<version>\bv=\S+\b)")
    version_instances = version_regex.findall(spf)

    # First, make sure we are not missing the version instance.
    if len(version_instances) == 0:
        return False

    # Next, make sure we only have 1 version instance.
    if len(version_instances) > 1:
        return False

    # Next, make sure the version instance is at the beginning of the string.
    if version_regex.match(spf).span()[0] != 0:
        return False
