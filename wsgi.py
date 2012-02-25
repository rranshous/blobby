
## wsgi app for serving blobby data

import handlers.blobby
import web

save_root = './data'
blobby_handler = handlers.blobby.BlobbySimpleDiskHandler(save_root)

# TODO: not read the whole file into memory

class GetBlobbyData:
    def GET(self,_hash):

        # check and see if we have the data
        try:
            data = blobby_handler.get_data(_hash)
        except Exception, ex:
            # woops, error!
            web.internalerror()

        # if we don't have any let the client know
        if not data:
            web.notfound()

        # if we have the data return it
        return data


# setup our web.py urls
urls = (
    '/(.+)', 'GetBlobbyData'
)
application = web.application(urls, globals())

if __name__ == "__main__":
    application.run()
