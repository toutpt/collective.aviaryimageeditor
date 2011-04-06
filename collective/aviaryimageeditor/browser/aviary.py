import json
from Products.Five import BrowserView

class AviaryPostHandler(BrowserView):
    """Handler for saving process"""

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        #import pdb;pdb.set_trace()
        self.context.plone_log('TODO: handle save')

class AviaryView(BrowserView):
    """Aviary image view"""

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def img_src(self):
        return self.context.absolute_url()
    
    def img_alt(self):
        return self.context.Title()

    def javascript(self):
        options = {'apikey':'9dde187dedd6953c7c2419cea9b083a3',
                   'posturl':self.context.absolute_url()+'/aviary_post_handler',
                   'theme':'bleusky',
                   'editoptions':'all',
                   'opentype':'float',
                   'cropsizes':'320x240,640x480,800x600,1280x1024'}
        return "aviaryOpt = "+json.dumps(options)
