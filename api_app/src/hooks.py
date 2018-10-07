import falcon
import uuid

from .data import CREDS


def validate_token(req, resp, resource, params):
    user = req.get_header('User')
    token = req.get_header('Token')

    if user is None or token is None:
        raise falcon.HTTPUnauthorized

    try:
        CREDS[user]
    except KeyError:
        raise falcon.HTTPUnauthorized
    else:
        if CREDS[user] != token:
            raise falcon.HTTPUnauthorized
        else:
            pass


def validate_uuid(req, resp, resource, params):
    try:
        uuid.UUID(params['book_id'], version=4)
    except ValueError:
        raise falcon.HTTPBadRequest(description="Not a valid uuid.")
