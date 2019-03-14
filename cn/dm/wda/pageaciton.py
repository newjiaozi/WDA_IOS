#coding = utf-8

import datetime

class BasePageAction():
    def __init__(self,session,client):
        self.session = session
        self.client = client

    def clickByName(self,name="",seconds=5):
        if name:
            self.session(name=name).click_exists(seconds)
        else:
            print("缺少关键参数name")

    def checkElementExist(self,name):
        try:
            self.session(name=name).get(timeout=5.0)
            return True
        except Exception as e:
            print(e)
            return False

    def getInMyPage(self):
        self.clickByName("MY")

    def getInMyToonPage(self,check=False):
        self.clickByName(name="我的漫画")
        self.checkElementExist("最近观看")
        if check:
            self.savePng("我的漫画页")

    def getInFoundPage(self,check=False):
        self.clickByName(name="发现")
        self.checkElementExist("个性推荐")
        if check:
            self.savePng("发现页")


    def getInUpdatePage(self,check=False):
        self.clickByName(name="更新")
        self.checkElementExist("今天")
        if check:
            self.savePng("更新页")

    def savePng(self,name):
        src = "./report/%s" % name+".png"
        self.client.screenshot(src)
        print(r'''<img src="%(src)s"  alt="%(name)s"  title="%(name)s" height="100" width="100" class="pimg"  onclick="javascript:window.open(this.src);"/>%(name)s''' % {'name':name,"src":name+".png"})


    def inputText(self,element,text):
        element.clear_text()
        element.set_text(text)

    def dismissAll(self):
        self.clickByName("允许",seconds=2)
        self.clickByName("确定",seconds=2)
        self.clickByName("Close",seconds=2)


    def jumpSNS(self):
        self.session.close()

    def waitGone(self,name):
        try:
            return self.session(name=name,visible=True).wait_gone(5)
        except Exception as e:
            print(e)
            return False

    ## all=True时，将所有的value返回；all=False时，只返回今天周几
    def getWeekday(self,all=True):
        week_day_dict = {
                    0 : '周一',
                    1 : '周二',
                    2 : '周三',
                    3 : '周四',
                    4 : '周五',
                    5 : '周六',
                    6 : '周日',
                    7 : '完结',
                    }
        cur_time = datetime.datetime.now()
        day = cur_time.weekday()
        if all:
            week_day_dict[day]="今天"
            return week_day_dict.values()
        else:
            return week_day_dict[day]




class MyPageAction(BasePageAction):

    def getInLoginPage(self):
        self.clickByName("账号管理")

    def getInAccountManagePage(self):
        self.clickByName("账号管理")

    def getInMyWalletPage(self):
        self.clickByName("我的钱包")

    def getInMessagePage(self):
        self.clickByName("咚漫消息")
        # self.checkElementExist("btnBack")
        # self.checkElementExist("公告事项")
        # self.savePng("咚漫消息页")

    def getInAlarmPage(self):
        self.clickByName("推送设置")
        # self.checkElementExist("新作品上线")
        # self.savePng("推荐设置页")

    def getInFeedbackPage(self):
        self.clickByName("意见反馈")
        # self.checkElementExist("E-mail")
        # self.savePng("意见反馈页")

    def getInAPPInfoPage(self):
        self.clickByName("APP信息")
        # self.checkElementExist("许可证")
        # self.savePng("APP信息页")

    def getInQuickLogin(self,close=False,other=False):
        ql = self.checkElementExist("快捷登录")
        if ql:
            if close:
                self.clickByName("invalidLogin")
            elif other:
                self.clickByName("其他方式登录")
            else:
                self.clickByName("快捷登录")

        else:
            print("【快捷登录】元素不存在")


    def toPasswordLogin(self):
        if self.checkElementExist("密码登录"):
            self.clickByName("密码登录")
        else:
            pass


    def toCodeLogin(self):
        if self.checkElementExist("验证码登录"):
            self.clickByName("验证码登录")
        else:
            pass

    def loginByPassword(self,userinput,passinput,ltype="mobile"):
        user= self.session(text="请输入手机号/邮箱")
        password = self.session(className="SecureTextField")
        self.inputText(user,text=userinput)
        self.inputText(password,text=passinput)
        self.clickByName("登录")
        self.checkElementExist("登录成功")
        self.savePng("%s密码登录成功" % ltype)
        self.waitGone("登录成功")







    def loginByCode(self):
        pass

    def loginByQQ(self):
        self.clickByName("qqLogin")
        self.clickByName("登录")
        self.checkElementExist("登录成功")
        self.savePng("QQ登录成功")
        self.waitGone("登录成功")


    def loginByWechat(self):
        self.clickByName("wechatLogin")
        self.checkElementExist("登录成功")
        self.savePng("Wechat登录成功")
        self.waitGone("登录成功")


    def loginByWeibo(self):
        self.clickByName("weiboLogin")
        self.checkElementExist("登录成功")
        self.savePng("Weibo登录成功")
        self.waitGone("登录成功")


    def logout(self):
        self.clickByName("退出")
        self.waitGone("退出")




    def checkNickname(self):
        self.session('name LIKE "*账号"').click_exists(5)
        self.clickByName("编辑个人资料")
        if self.checkElementExist("personalClose.png"):
            pass
            self.savePng("个人资料页")
            close = self.session(name="personalClose.png")
            cbc = close.bounds.center
            self.session.tap(cbc.x,cbc.y)


    def checkAccountManage(self):
        self.getInAccountManagePage()
        if self.session('name LIKE "咚漫ID*"').exists:
            self.savePng("账号管理页")

        self.clickByName("btnBack")

    def checkMyWallet(self):
        self.getInMyWalletPage()
        if self.checkElementExist("消费记录"):
            self.savePng("我的钱包页")
        self.clickByName("btnBack")

    def checkMessage(self):
        self.getInMessagePage()
        if self.checkElementExist("公告事项"):
            self.savePng("咚漫消息页")
        self.clickByName("btnBack")


    def checkAlarm(self):
        self.getInAlarmPage()
        if self.checkElementExist("新作品上线"):
            self.savePng("推送设置页")
        self.clickByName("recommend back btn")


    def checkFeedback(self):
        self.getInFeedbackPage()
        if self.checkElementExist("E-mail"):
            self.savePng("意见反馈页")
        self.clickByName("recommend back btn")


    def checkAPPInfo(self):
        self.getInAPPInfoPage()
        if self.checkElementExist("许可证"):
            self.savePng("APP信息页")
        self.clickByName("recommend back btn")



class MyToonPageAction(BasePageAction):

    def getInRecently(self):
        self.clickByName("最近观看")

    def getInMySubscribe(self):
        self.clickByName("我的关注")

    def getInSave(self):
        self.clickByName("临时保存")
        self.checkElementExist("没有临时保存的漫画。")

    def getInMyComment(self):
        self.clickByName("我的评论")

    def checkRecently(self):
        pass

    def checMySuscribe(self):
        pass

    def checkSave(self):
        pass

    def checkMyComment(self):
        pass


class FoundPageAction(BasePageAction):

    def getInNew(self):
        pass

    def getInRank(self):
        pass

    def getInRecommend(self):
        pass

    def getInGenre(self):
        pass

    def getInDMRecommendMore(self):
        pass

    def getInQXKMore(self):
        pass

    def getInNewLoginMore(self):
        pass

    def getInGenreMore(self):
        pass

    def getInThemeMore(self):
        pass

    def getInUpRankMore(self):
        pass

    def getInNewRankMore(self):
        pass

    def getInSumRankMore(self):
        pass

    def getInGuessULikeMore(self):
        pass

    def getInBigBanner(self):
        pass

    def getInBarBanner1(self):
        pass

    def getInBarBanner2(self):
        pass

    def getInBarBanner(self):
        pass

    def searchByTitleName(self):
        pass

    def searchByTitleAuthor(self):
        pass

    def searchByTitleText(self):
        pass

class UpdatePageAction(BasePageAction):

    def searchByTitleName(self):
        self.clickByName(name = "card home base search")

    def searchByTitleAuthor(self):
        pass

    def searchByTitleText(self):
        pass

    def getInRQ(self):
        pass

    def getInSubscribe(self):
        pass


