from django.test import SimpleTestCase
from django.urls import reverse, resolve
from game.views import IndexView, SwitchGame, PS4Game, XBOGame, DetailView, VGCreate, VGSearch, VGUpdate, VGDelete

class TetsUrls(SimpleTestCase):

    def setUp(self):
        self.VGCreate = reverse('game:createVG')
    
    def testCreation(self):
        self.assertEquals(resolve(self.VGCreate).func, VGCreate)
    
    def testIndex(self):
        url = reverse('game:allgame')
        self.assertEquals(resolve(url).func.view_class , IndexView)
    
    def testSw(self):
        url = reverse('game:nswgame')
        self.assertEquals(resolve(url).func.view_class , SwitchGame)
    
    def testPS4(self):
        url = reverse('game:ps4game')
        self.assertEquals(resolve(url).func.view_class , PS4Game)
    
    def testXBO(self):
        url = reverse('game:xbogame')
        self.assertEquals(resolve(url).func.view_class , XBOGame)
    
    def testDetail(self):
        url = reverse('game:details', args=['ys8nsw'])
        self.assertEquals(resolve(url).func.view_class , DetailView)
    
    def testSearch(self):
        url = reverse('game:serchVG')
        self.assertEquals(resolve(url).func, VGSearch)
    
    def testUpdate(self):
        url = reverse('game:editar', args=['ys8nsw'])
        self.assertEquals(resolve(url).func, VGUpdate)
    
    def testDelete(self):
        url = reverse('game:eliminar', args=['ys8nsw'])
        self.assertEquals(resolve(url).func, VGDelete)

    
