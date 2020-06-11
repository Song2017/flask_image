import json
import json.decoder

__all__ = [
    "json_dumps_unicode",
    "json_loads",
]


def json_dumps_unicode(obj):
    """
    Change Python default json.dumps acting like JavaScript, including allow
    Chinese characters and no space between any keys or values.
    """
    return json.dumps(obj,
                      ensure_ascii=False,
                      separators=(',', ':'),
                      cls=RawDataEncoder
                      )


class RawDataEncoder(json.JSONEncoder):

    def default(self, o):
        if isinstance(o, bytes):
            return o.decode("utf-8")
        return super(RawDataEncoder, self).default(o)


def json_loads(json_str: str) -> dict:
    """ An enhanced version of json.loads. """
    if isinstance(json_str, dict):
        return json_str  # if it's json already

    try:
        return json.loads(json_str)
    except json.decoder.JSONDecodeError as e:
        raise ValueError(f"""
Error: {e}, Wrong json_str:{repr(json_str)}
        """.strip())
