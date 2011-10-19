import json
from zope import component
from Products.Five import BrowserView
from plone.registry.interfaces import IRegistry

from collective.aviaryimageeditor import interfaces

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
        self._config = None

    def javascript_configuration(self):
        config = self.configuration()
        #'9dde187dedd6953c7c2419cea9b083a3'
        options = {'APIKey':config.APIKey,
                   'Theme': config.Theme,
                   'posturl':self.context.absolute_url()+'/aviary_post_handler',
                   'EditOptions':','.join(config.EditOptions),
                   'OpenType':config.OpenType,
                   'cropsizes':','.join(config.CropSizes)}

        return "aviaryOpt = %s;"%json.dumps(options)

    def configuration(self):
        if self._config is None:
            registry = component.queryUtility(IRegistry)
            self._config = registry.forInterface(interfaces.AviaryConfiguration)
        return self._config

    def img_src(self):
        return self.context.absolute_url()
    
    def img_alt(self):
        return self.context.Title()
