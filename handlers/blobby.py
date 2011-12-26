from blobby import Blobby, ttypes as o

class BlobbySimpleDiskHandler(object):
    """
    very simply we are going to store the data on the
    disk, subfolders based on pieces of hash. file
    name is hash, data is data
    """

    ## CODE ASSUMES ONLY ONE SERVICE RUNNING AGAINST THE
    ## SAME DATA SOURCE

    def get_data(self, bhash):
        try:
            path = self.get_data_path(bhash)
            if not os.path.exists(path):
                return None
            else:
                with open(path,'r') as fh:
                    return fh.read()
        except Exception, ex:
            raise o.Exception('oException get: %s %s' % (bhash,ex))

    def set_data(self, data):
        try:
            bhash = self.get_data_bhash(data)
            path = self.get_data_path(bhash)
            with open(path,'w') as fh:
                fh.write(data)
        except Exception, ex:
            raise o.Exception('oException set: %s %s' % (bhash,ex))

    def delete_set(self, bhash):
        path = self.get_data_path(bhash)
        try:
            if not os.path.exists(path):
                return False
            os.unlink(path)
        except Exception, ex:
            raise o.Exception('oException delete: %s %s' % (bhash,ex))

def run():
    from lib.discovery import serve_service
    serve_service(Blobby, BlobbySimpleDiskHandler())
