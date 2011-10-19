from zope import interface
from zope import schema

from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary
from collective.aviaryimageeditor import messageFactory as _
from collective.aviaryimageeditor import i18n

class IAviaryLayer(interface.Interface):
    """Browser layer"""

vocab_EditOptions = SimpleVocabulary(
 [
  SimpleTerm(value=u"all",        title=_(u"All tools")),
  SimpleTerm(value=u"rotate",     title=_(u"Rotate")),
  SimpleTerm(value=u"resize",     title=_(u"Resize")),
  SimpleTerm(value=u"crop",       title=_(u"Crop")),
  SimpleTerm(value=u"flip",       title=_(u"Flip")),
  SimpleTerm(value=u"redeye",     title=_(u"Red eye")),
  SimpleTerm(value=u"blemish",    title=_(u"Blemish")),
  SimpleTerm(value=u"colors",     title=_(u"Colors")),
  SimpleTerm(value=u"saturation", title=_(u"Saturation")),
  SimpleTerm(value=u"brightness", title=_(u"Brightness")),
  SimpleTerm(value=u"contrast",   title=_(u"Contrast")),
  SimpleTerm(value=u"drawing",    title=_(u"Drawing")),
  SimpleTerm(value=u"text",       title=_(u"Text")),
  SimpleTerm(value=u"stickers",   title=_(u"Stickers")),
  SimpleTerm(value=u"blur",       title=_(u"Blur")),
  SimpleTerm(value=u"whiten",     title=_(u"Whiten")),
  ]
    )

vocab_Theme = SimpleVocabulary(
  [
  SimpleTerm(value=u"bluesky",   title=_(u"Bluesky")),
  SimpleTerm(value=u"black",     title=_(u"Black")),
  SimpleTerm(value=u"sliver",    title=_(u"Sliver")),
  SimpleTerm(value=u"darkblue",  title=_(u"Darkblue")),
  SimpleTerm(value=u"lightblue", title=_(u"Lightblue")),
  SimpleTerm(value=u"red",       title=_(u"Red")),
  SimpleTerm(value=u"green",     title=_(u"Green")),
  ]
    )

vocab_OpenType = SimpleVocabulary(
  [
  SimpleTerm(value=u"float",    title=_(u"Float")),
  SimpleTerm(value=u"lightbox", title=_(u"Lightbox")),
  SimpleTerm(value=u"inject",   title=_(u"Inject")),
  ]
    )

DEFAULT_STIKERS = """[
    [ 'http://www.aviary.com/images/feather/sticker/bandaid_01.png',
     'http://www.aviary.com/images/feather/sticker/bandaid_01.png' ],
    [ 'http://www.aviary.com/images/feather/sticker/beer_01.png',
     'http://www.aviary.com/images/feather/sticker/thumbs/beer_01.png' ], 
    [ 'http://www.aviary.com/images/feather/sticker/cigar_01.png',
     'http://www.aviary.com/images/feather/sticker/thumbs/cigar_01.png' ], 
    [ 'http://www.aviary.com/images/feather/sticker/glasses_01.png',
     'http://www.aviary.com/images/feather/sticker/thumbs/glasses_01.png' ], 
    [ 'http://www.aviary.com/images/feather/sticker/glasses_02.png',
     'http://www.aviary.com/images/feather/sticker/thumbs/glasses_02.png' ], 
    [ 'http://www.aviary.com/images/feather/sticker/glasses_03.png',
     'http://www.aviary.com/images/feather/sticker/thumbs/glasses_03.png' ], 
    [ 'http://www.aviary.com/images/feather/sticker/glasses_04.png',
     'http://www.aviary.com/images/feather/sticker/thumbs/glasses_04.png' ], 
    [ 'http://www.aviary.com/images/feather/sticker/hat_01.png',
     'http://www.aviary.com/images/feather/sticker/thumbs/hat_01.png' ], 
    [ 'http://www.aviary.com/images/feather/sticker/hat_02.png',
     'http://www.aviary.com/images/feather/sticker/thumbs/hat_02.png' ], 
    [ 'http://www.aviary.com/images/feather/sticker/hat_04.png',
     'http://www.aviary.com/images/feather/sticker/thumbs/hat_04.png' ], 
    [ 'http://www.aviary.com/images/feather/sticker/hat_05.png',
     'http://www.aviary.com/images/feather/sticker/thumbs/hat_05.png' ], 
    [ 'http://www.aviary.com/images/feather/sticker/hat_06.png',
     'http://www.aviary.com/images/feather/sticker/thumbs/hat_06.png' ], 
    [ 'http://www.aviary.com/images/feather/sticker/hat_07.png',
     'http://www.aviary.com/images/feather/sticker/thumbs/hat_07.png' ], 
    [ 'http://www.aviary.com/images/feather/sticker/patch_01.png',
     'http://www.aviary.com/images/feather/sticker/thumbs/patch_01.png' ], 
    [ 'http://www.aviary.com/images/feather/sticker/sguriken_01.png',
     'http://www.aviary.com/images/feather/sticker/thumbs/sguriken_01.png' ], 
    [ 'http://www.aviary.com/images/feather/sticker/stache_01.png',
     'http://www.aviary.com/images/feather/sticker/thumbs/stache_01.png' ], 
    [ 'http://www.aviary.com/images/feather/sticker/stache_02.png',
     'http://www.aviary.com/images/feather/sticker/thumbs/stache_02.png' ], 
    [ 'http://www.aviary.com/images/feather/sticker/stache_03.png',
     'http://www.aviary.com/images/feather/sticker/thumbs/stache_03.png' ], 
    [ 'http://www.aviary.com/images/feather/sticker/stache_04.png',
     'http://www.aviary.com/images/feather/sticker/thumbs/stache_04.png' ], 
    [ 'http://www.aviary.com/images/feather/sticker/stache_05.png',
     'http://www.aviary.com/images/feather/sticker/thumbs/stache_05.png' ]]"""


class AviaryConfiguration(interface.Interface):
    """Aviary configuration"""
    
    APIKey = schema.ASCIILine(title=_(u"API Key"),
                              default="")
    
    EditOptions = schema.List(title=_(u"Tools"),
                        default=["all"],
                        value_type=schema.Choice(title=_(u"Tools"),
                                                 vocabulary=vocab_EditOptions))

    OpenType = schema.Choice(title=_(u"Open type"),
                             default="lightbox",
                             vocabulary=vocab_OpenType)
    
    CropSizes =schema.List(title=_(u"Crop sizes"),
                           default=['320x240','640x480','800x600','1280x1024'],
                           value_type=schema.ASCIILine(title=_(u"Crop size"))
                           )
#
#    NoCloseButton = schema.Bool(title=_(u"No close button"),
#                                description=i18n.desc_NoCloseButton)

    Stickers = schema.ASCII(title=_(u"Stickers"),
                           description=i18n.desc_Stickers,
                           default=DEFAULT_STIKERS)
    
    Theme = schema.Choice(title=_(u"Theme"),
                          default="bluesky",
                          vocabulary=vocab_Theme)

    """
     <script type="text/javascript"> 
    var _featherLoaded = false; 
     
    Feather_APIKey = ''; 
    Feather_Theme = 'bluesky'; 
    Feather_EditOptions = 'rotate,,,,,,,,,,,,,,'; 
    Feather_OpenType = 'float'; 
    Feather_CropSizes = '320x240,640x480,800x600,1280x1024'; 
    Feather_Stickers = [ 
// big image, thumbnail image 
[ 'http://www.aviary.com/images/feather/sticker/bandaid_01.png', 'http://www.aviary.com/images/feather/sticker/bandaid_01.png' ], 
[ 'http://www.aviary.com/images/feather/sticker/beer_01.png', 'http://www.aviary.com/images/feather/sticker/thumbs/beer_01.png' ], 
[ 'http://www.aviary.com/images/feather/sticker/cigar_01.png', 'http://www.aviary.com/images/feather/sticker/thumbs/cigar_01.png' ], 
[ 'http://www.aviary.com/images/feather/sticker/glasses_01.png', 'http://www.aviary.com/images/feather/sticker/thumbs/glasses_01.png' ], 
[ 'http://www.aviary.com/images/feather/sticker/glasses_02.png', 'http://www.aviary.com/images/feather/sticker/thumbs/glasses_02.png' ], 
[ 'http://www.aviary.com/images/feather/sticker/glasses_03.png', 'http://www.aviary.com/images/feather/sticker/thumbs/glasses_03.png' ], 
[ 'http://www.aviary.com/images/feather/sticker/glasses_04.png', 'http://www.aviary.com/images/feather/sticker/thumbs/glasses_04.png' ], 
[ 'http://www.aviary.com/images/feather/sticker/hat_01.png', 'http://www.aviary.com/images/feather/sticker/thumbs/hat_01.png' ], 
[ 'http://www.aviary.com/images/feather/sticker/hat_02.png', 'http://www.aviary.com/images/feather/sticker/thumbs/hat_02.png' ], 
[ 'http://www.aviary.com/images/feather/sticker/hat_04.png', 'http://www.aviary.com/images/feather/sticker/thumbs/hat_04.png' ], 
[ 'http://www.aviary.com/images/feather/sticker/hat_05.png', 'http://www.aviary.com/images/feather/sticker/thumbs/hat_05.png' ], 
[ 'http://www.aviary.com/images/feather/sticker/hat_06.png', 'http://www.aviary.com/images/feather/sticker/thumbs/hat_06.png' ], 
[ 'http://www.aviary.com/images/feather/sticker/hat_07.png', 'http://www.aviary.com/images/feather/sticker/thumbs/hat_07.png' ], 
[ 'http://www.aviary.com/images/feather/sticker/patch_01.png', 'http://www.aviary.com/images/feather/sticker/thumbs/patch_01.png' ], 
[ 'http://www.aviary.com/images/feather/sticker/sguriken_01.png', 'http://www.aviary.com/images/feather/sticker/thumbs/sguriken_01.png' ], 
[ 'http://www.aviary.com/images/feather/sticker/stache_01.png', 'http://www.aviary.com/images/feather/sticker/thumbs/stache_01.png' ], 
[ 'http://www.aviary.com/images/feather/sticker/stache_02.png', 'http://www.aviary.com/images/feather/sticker/thumbs/stache_02.png' ], 
[ 'http://www.aviary.com/images/feather/sticker/stache_03.png', 'http://www.aviary.com/images/feather/sticker/thumbs/stache_03.png' ], 
[ 'http://www.aviary.com/images/feather/sticker/stache_04.png', 'http://www.aviary.com/images/feather/sticker/thumbs/stache_04.png' ], 
[ 'http://www.aviary.com/images/feather/sticker/stache_05.png', 'http://www.aviary.com/images/feather/sticker/thumbs/stache_05.png' ]];
      
    Feather_OnSave = function(id, url) { 
        var e = document.getElementById(id); 
        e.src = url; 
        aviaryeditor_close(); 
    } 
     
    Feather_OnLoad = function() { 
        _featherLoaded = true; 
    } 
     
    function launchEditor(imageid) { 
        if (_featherLoaded) { 
            var src = document.getElementById(imageid).src; 
            aviaryeditor(imageid, src); 
        } 
    } 
</script> 
<script type="text/javascript" src="http://feather.aviary.com/js/feather.js"></script>  
 
<!-- End Generated Code -- Don't Copy Below This Line --> 
 
<div id="injection_site"></div>
<img id="image1" src="http://developers.aviary.com/images/feather/redeye.jpg"/> 
<p><input type="image" src="http://developers.aviary.com/images/feather/edit-photo.png" value="Edit photo" onclick="launchEditor('image1'); return false;" /></p> 
"""