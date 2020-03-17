import chaotic_keygen
import errno
import os
import time

class Space:

    def __init__(self, path=None):
        self.path = path
        if path is None:
            self.path = os.getcwd()

    def create_space(self, path):

        home_dir = 'keys'
        os.chdir(path)
        access_rights = 0o755

        try:
            if not os.path.exists(r'%s' % home_dir):
                os.mkdir(r'%s' % home_dir, access_rights)
                print("Successfully created the directory %s\%s" % (path, home_dir))
                return 0
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise
            print("Creation of the directory %s\%s failed" % (path, home_dir))
            return 1

    def clear_space(self, path):

        home_dir = 'keys'
        os.chdir(path)

        for root, dirs, files in os.walk(r'%s' % home_dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))

        try:
            if os.path.exists(r'%s' % home_dir):
                os.rmdir(r'%s' % home_dir)  # <= removes the created dir.
                print("Successfully removed the directory %s\%s" % (path, home_dir))
                return 0
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise
            print("Deletion of the directory %s\%s failed" % (path, home_dir))
            return 1






