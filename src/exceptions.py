import attr

@attr.s
class InvalidRequestStructureError(Exception):
    error_msg = attr.ib() # type: str
    errors = attr.ib() # type: dict