import falcon

from fountain_pens import Resource

api = application = falcon.API()

images = Resource()
api.add_route('/images', images)
