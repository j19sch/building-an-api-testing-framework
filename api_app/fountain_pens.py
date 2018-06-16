import json
import falcon


class Resource(object):
    def __init__(self):
        self.doc =  {
            'images': [
                {
                    'href': '/images/1eaf6ef1-7f2d-4ecc-a8d5-6e8adba7cc0e.png'
                }
            ]
        }

    def on_get(self, req, resp):
        # Create a JSON representation of the resource
        resp.body = json.dumps(self.doc, ensure_ascii=False)

        # The following line can be omitted because 200 is the default
        # status returned by the framework, but it is included here to
        # illustrate how this may be overridden as needed.
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        self.doc['images'].append(req.media)

        resp.body = json.dumps(self.doc, ensure_ascii=False)
        resp.status = falcon.HTTP_201
