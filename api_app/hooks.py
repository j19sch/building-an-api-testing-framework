import falcon
from data import CREDS


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
