from tgen.blobby import Blobby, ttypes as o
from hashlib import sha1
import os.path

class BlobbySimpleDiskHandler(object):
    """
    very simply we are going to store the data on the
    disk, subfolders based on pieces of hash. file
    name is hash, data is data
    """

    ## CODE ASSUMES ONLY ONE SERVICE RUNNING AGAINST THE
    ## SAME DATA SOURCE

    def __init__(self, save_root):
        self.save_root = save_root

    def get_data(self, bhash):
        try:
            path = self.get_data_path(bhash)
            if not os.path.exists(path):
                # we could use a raise here instead
                return ''
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
            raise o.Exception('oException set: %s %s' % (len(data),ex))

        return bhash

    def delete_data(self, bhash):
        path = self.get_data_path(bhash)
        try:
            if not os.path.exists(path):
                return False
            os.unlink(path)
        except Exception, ex:
            raise o.Exception('oException delete: %s %s' % (bhash,ex))
        return True


    def get_data_path(self, bhash):
        return os.path.join(self.save_root,bhash)

    def get_data_bhash(self, data):
        return sha1(data).hexdigest()

def run():
    from lib.discovery import serve_service
    save_root = os.path.abspath(os.path.join(
                    os.path.dirname(os.path.abspath(__file__)),
                    '../data'))
    print 'save root: %s' % save_root
    serve_service(Blobby, BlobbySimpleDiskHandler(save_root))
