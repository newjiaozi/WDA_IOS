#coding = utf-8

import unittest
import wda

from .pageaciton import MyPageAction as MPA
from .pageaciton import MyToonPageAction as MTPA
from .pageaciton import FoundPageAction as FPA
from .pageaciton import UpdatePageAction as UPA
from .pageaciton import BasePageAction as BPA




class BasePageTescase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # wda.DEBUG = True  # default False
        # wda.HTTP_TIMEOUT = 60.0  # default 60.0 seconds
        cls.c = wda.Client("http://localhost:12345")
        cls.session = cls.c.session('com.naver.linewebtoon.cn')
        # cls.session.set_alert_callback(cls._alert_callback)
        cls.BPA = BPA(cls.session,cls.c)
        cls.MPA = MPA(cls.session,cls.c)
        cls.MTPA = MTPA(cls.session,cls.c)
        cls.FPA = FPA(cls.session,cls.c)
        cls.UPA = UPA(cls.session,cls.c)
        cls.BPA.dismissAll()


    @classmethod
    def tearDownClass(cls):
        print("ACTION TEAR DOWN")
        cls.MPA.getInMyPage()
        cls.MPA.getInAccountManagePage()
        cls.MPA.logout()
        cls.session.close()


class LoginTestCase(unittest.TestCase):

    def setUp(self):
        self.c = wda.Client("http://localhost:12345")
        self.session = self.c.session('com.naver.linewebtoon.cn')
        self.MPA = MPA(self.session,self.c)
        self.MPA.dismissAll()

    def tearDown(self):
        self.session.close()

    def test01_loginByEmail(self):
        self.MPA.getInMyPage()
        self.MPA.getInLoginPage()
        self.MPA.getInQuickLogin(other=True)
        self.MPA.toPasswordLogin()
        self.MPA.loginByPassword("weixindogs@163.com","qwe123",ltype="Email")
        self.MPA.getInAccountManagePage()
        self.MPA.logout()


    def test02_loginByQQ(self):
        self.MPA.getInMyPage()
        self.MPA.getInLoginPage()
        self.MPA.getInQuickLogin(other=True)
        self.MPA.toCodeLogin()
        self.MPA.loginByQQ()
        self.MPA.getInAccountManagePage()
        self.MPA.logout()

    def test03_loginByWechat(self):
        self.MPA.getInMyPage()
        self.MPA.getInLoginPage()
        self.MPA.getInQuickLogin(other=True)
        self.MPA.toCodeLogin()
        self.MPA.loginByWechat()
        self.MPA.getInAccountManagePage()
        self.MPA.logout()

    def test04_loginByWeibo(self):
        self.MPA.getInMyPage()
        self.MPA.getInLoginPage()
        self.MPA.getInQuickLogin(other=True)
        self.MPA.toCodeLogin()
        self.MPA.loginByWeibo()
        self.MPA.getInAccountManagePage()
        self.MPA.logout()

    def test05_loginByPass(self):
        self.MPA.getInMyPage()
        self.MPA.getInLoginPage()
        self.MPA.getInQuickLogin(other=True)
        self.MPA.toPasswordLogin()
        self.MPA.loginByPassword("13683581996","qwe123")
        # self.MPA.getInAccountManagePage()
        # self.MPA.logout()


class MyPageTestcase(BasePageTescase):
    #
    # def test01_loginByEmail(self):
    #     self.MPA.getInMyPage()
    #     self.MPA.getInLoginPage()
    #     self.MPA.getInQuickLogin(other=True)
    #     self.MPA.toPasswordLogin()
    #     self.MPA.loginByPassword("weixindogs@163.com","qwe123")
    #     self.MPA.getInAccountManagePage()
    #     self.MPA.logout()
    #
    #
    # def test02_loginByQQ(self):
    #     self.MPA.getInMyPage()
    #     self.MPA.getInLoginPage()
    #     self.MPA.getInQuickLogin(other=True)
    #     self.MPA.toCodeLogin()
    #     self.MPA.loginByQQ()
    #     self.MPA.getInAccountManagePage()
    #     self.MPA.logout()
    #     self.MPA.jumpSNS()
    #
    # def test03_loginByWechat(self):
    #     self.MPA.getInMyPage()
    #     self.MPA.getInLoginPage()
    #     self.MPA.getInQuickLogin(other=True)
    #     self.MPA.toCodeLogin()
    #     self.MPA.loginByWechat()
    #     self.MPA.getInAccountManagePage()
    #     self.MPA.logout()
    #     self.MPA.jumpSNS()
    #
    # def test04_loginByWeibo(self):
    #     self.MPA.getInMyPage()
    #     self.MPA.getInLoginPage()
    #     self.MPA.getInQuickLogin(other=True)
    #     self.MPA.toCodeLogin()
    #     self.MPA.loginByWeibo()
    #     self.MPA.getInAccountManagePage()
    #     self.MPA.logout()
    #     self.MPA.jumpSNS()
    #
    # def test05_loginByPass(self):
    #     self.MPA.getInMyPage()
    #     self.MPA.getInLoginPage()
    #     self.MPA.getInQuickLogin(other=True)
    #     self.MPA.toPasswordLogin()
    #     self.MPA.loginByPassword("13683581996","qwe123")
    #     # self.MPA.getInAccountManagePage()
    #     # self.MPA.logout()

    def test06_checkPersonInfo(self):
        self.MPA.getInMyPage()
        self.MPA.checkNickname()

    def test07_checkAccountManage(self):
        self.MPA.getInMyPage()
        self.MPA.checkAccountManage()

    def test08_checkMyWallet(self):
        self.MPA.getInMyPage()
        self.MPA.checkMyWallet()

    def test09_checkMessage(self):
        self.MPA.getInMyPage()
        self.MPA.checkMessage()

    def test10_checkAlarm(self):
        self.MPA.getInMyPage()
        self.MPA.checkAlarm()

    def test11_checkFeedback(self):
        self.MPA.getInMyPage()
        self.MPA.checkFeedback()

    def test12_checkAPPInfo(self):
        self.MPA.getInMyPage()
        self.MPA.checkAPPInfo()

class MyToonPageTescase(BasePageTescase):

    def test01_testGetInMyToon(self):
        self.MTPA.getInMyToonPage(check=True)


class FoundPageTescase(BasePageTescase):

    def test01_testGetInFound(self):
        self.FPA.getInFoundPage(check=True)


class UpdatePageTescase(BasePageTescase):

    def test01_testGetInUpdate(self):
        self.UPA.getInUpdatePage(check=True)




