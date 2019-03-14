#coding = utf-8



import subprocess
import multiprocessing
import time
import unittest
from cn.dm.wda.HTMLTestRunner import HTMLTestRunner
from cn.dm.wda.pagetestcase import MyPageTestcase,MyToonPageTescase,FoundPageTescase,UpdatePageTescase,LoginTestCase

def iproxyOn():
    print("iproxy on")
    subprocess.run(["killall","iproxy"])
    subprocess.run(["iproxy", "12345", "8100"])
    print("iproxy on")


def xcodeBuild():
    subprocess.run(["security", "unlock-keychain", "-p", "111111", "/Users/dongman/Library/Keychains/login.keychain-db"])
    udid = "00008020-000E502E0E04002E"
    print("ready xcodebuild")
    # subprocess.Popen('xcodebuild -project /Users/dongman/WebDriverAgent/WebDriverAgent.xcodeproj -scheme WebDriverAgentRunner -destination "id=%s" test' % udid)
    subprocess.run(["xcodebuild","-project","/Users/dongman/WebDriverAgent/WebDriverAgent.xcodeproj",
                    "-scheme","WebDriverAgentRunner","-destination","id=%s" % udid,"test"])

def runCase():
    time.sleep(20)
    time.sleep(2000000)
    result_path = "report/IOS测试报告.html"
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(LoginTestCase))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(MyPageTestcase))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(MyToonPageTescase))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(FoundPageTescase))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(UpdatePageTescase))



    print(suite)

    with open(result_path,'wb') as f:
        runner = HTMLTestRunner(stream=f, title='IOS测试报告', description='测试报告 详细信息')
        runner.run(suite)


if __name__ == "__main__":
    print("Start Test")
    pool = multiprocessing.Pool(3)
    pool.apply_async(iproxyOn)
    pool.apply_async(xcodeBuild)
    res = pool.apply_async(runCase)
    pool.close()
    res.wait()
    print("End Test")


