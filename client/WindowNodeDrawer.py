import direct.directbase.DirectStart
from direct.gui.OnscreenText import OnscreenText 
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from Config import *

v = 1.0/120.0
theme = 'default'

def WindowNodeDrawer(w, h, style):

    # 0 1 2
    # 3 4 5
    # 6 7 8

    container = NodePath('foo')

    frames = (
        ( -v*(w/2   ), -v*(w/2-16),  v*(h/2-16),  v*(h/2   ) ),
        ( -v*(w/2-16),  v*(w/2-16),  v*(h/2-16),  v*(h/2   ) ),
        (  v*(w/2-16),  v*(w/2   ),  v*(h/2-16),  v*(h/2   ) ),
        ( -v*(w/2   ), -v*(w/2-16),  v*(h/2-16), -v*(h/2-16) ),
        ( -v*(w/2- 2),  v*(w/2- 2), -v*(h/2- 2),  v*(h/2- 2) ), # 4
        (  v*(w/2-16),  v*(w/2   ),  v*(h/2-16), -v*(h/2-16) ),
        ( -v*(w/2   ), -v*(w/2-16), -v*(h/2   ), -v*(h/2-16) ),
        ( -v*(w/2-16),  v*(w/2-16), -v*(h/2   ), -v*(h/2-16) ),
        (  v*(w/2-16),  v*(w/2   ), -v*(h/2   ), -v*(h/2-16) ),
    )

    for i in (4,0,1,2,3,5,6,7,8):

        path = GAME+'/textures/gui/'+theme+'/'+style+'/'+str(i)+'.png'

        tex = loader.loadTexture(path)
        tex.setMagfilter(Texture.FTNearest)
        tex.setMinfilter(Texture.FTNearest)
        tex.setWrapU(Texture.WMRepeat)
        tex.setWrapV(Texture.WMRepeat)

        cm = CardMaker('card')
        cm.setFrame(frames[i])
        if i == 4:
            cm.setUvRange((0,0), (w/tex.getOrigFileXSize(), h/tex.getOrigFileYSize()))

        card = render.attachNewNode(cm.generate())
        card.setTexture(tex)
        card.reparentTo(container)

    return container