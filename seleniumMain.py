from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
import re
url="https://so.csdn.net/so/search?spm=1001.2101.3001.4498&q=selenium%E5%90%91%E4%B8%8B%E6%BB%9A%E5%8A%A8&t=&u=&urw="
urlX="https://www.goofish.com/search?spm=a21ybx.item.searchHistory.1.46323da6UHZN2H&q=%E9%9B%B7%E8%9B%878k%E6%8E%A5%E6%94%B6%E5%99%A8"
urla="https://www.goofish.com/search?q=%E6%AF%92%E8%9D%B0v3pro&spm=a21ybx.search.searchInput.0"
resultClass=".so-items-normal"
wrapClass=".feeds-item-wrap--rGdH_KoF"
titleClass=".row1-wrap-title--qIlOySTh"
numClass=".number--NKh1vXWM"
arrow=".search-pagination-arrow-container--lt2kCP6J"
sizeClass=".cpv--R1RkOhUI"
sizeTable=("XL","L","2XL","S","M","XS")

def sizeBool(sizeFilter:tuple,size):
    if size in sizeFilter:
        return True
    return False

class SampleTutorial:

    def __init__(self,url,file_path,option,minPrice=0,maxPrice=100000000000000,pages=10,betweenTime=3):
        # 创建了一个Chrome浏览器的WebDriver实例
        self.driver = webdriver.Chrome(options=option)
        self.url=url
        # 最大化窗口
        self.driver.maximize_window()
        # 隐式等待,设置最大的等待时长,只对查找元素(find_elementXXX)生效
        self.driver.implicitly_wait(2)
        self.file_path = file_path
        self.minPrice = minPrice
        self.maxPrice = maxPrice
        self.pages = pages
        self.betweenTime = betweenTime
        #self.reg = reg
        #self.withSize = withSize
        #self.sizeFilter = sizeFilter
    def method(self):
        """代码执行"""
        # 通过get()方法打开网页
        self.driver.get(
        self.url
        )
     #       'https://www.goofish.com/search?q=%E9%9B%B7%E8%9B%878k%E6%8E%A5%E6%94%B6%E5%99%A8&spm=a21ybx.home.searchInput.0')

    def sign_out(self):
        """退出浏览器"""
        # 关闭浏览器，调用driver.quit()会终止WebDriver对象的相关进程和资源，及时清理测试环境。
        self.driver.quit()

    def load_cookies(self):

        with open('G:\code\spider\cookies1.json', 'r') as f:
            # 使用json读取cookies 注意读取的是文件 所以用load而不是loads
            cookies_list = json.load(f)
            for cookie in cookies_list:
                self.driver.add_cookie(cookie)



        """加载cookies"""
        #self.driver.get_cookies()


        self.driver.refresh()
    def get_cookies(self):
        """获取cookies"""
        cookies = self.driver.get_cookies()
        return cookies
    def driv(self):
        self.driver.execute_script('window.scrollBy(0,500)')

    def start(self):
        f = open(self.file_path, "w", encoding="utf-8")
        for j in range(1, self.pages + 1):

            self.driv()
            time.sleep(1.5)
            # 等待页面加载完成
            size = ''
            nums = run.driver.find_elements(By.CSS_SELECTOR, numClass)
            links = run.driver.find_elements(By.CSS_SELECTOR, wrapClass)
            titles = run.driver.find_elements(By.CSS_SELECTOR, titleClass)
            '''
            if self.withSize:
                size = run.driver.find_elements(By.CSS_SELECTOR, sizeClass)
                '''
            for i in range(len(nums)):

                try:
                    num = nums[i].text
                    link = links[i].get_attribute("href")
                    title = titles[i].text
                    '''
                    if self.withSize:
                        sizestr = size[i].text
                        print(sizestr)
                        '''
                    if (int(num)>=self.minPrice and int(num)<=self.maxPrice):
                        print(f"{title}  ,{num}   ,link: ,{link}")
                        f.write(f"{title}  ,{num}   ,link: ,{link}\n")
                except Exception as e:
                    print(f"error   {e}")
                    break

            buttons = run.driver.find_elements(By.CSS_SELECTOR, ".search-pagination-page-box--AbqmJFFp")
            flage = 0
            for b in buttons:
                if b.text == str(j+1):

                    print(f"第{b.text}页")
                    b.click()
                    flage = 1
                    break
            if flage == 0:
                run.driver.find_elements(By.CSS_SELECTOR,arrow)[1].click()
            #buttons[j + 1].click()

            time.sleep(self.betweenTime)











if __name__ == "__main__":
    #pattern = r'\b(xl|2xl|l)\b'
    # 加载cookies
    urlf="https://www.goofish.com/"
    #cookie_dics = []
    options = webdriver.ChromeOptions()

    options.debugger_address = 'localhost:9222'
    #options.add_experimental_option('detach', True)
    run = SampleTutorial(urlf,r"result.csv",options,minPrice=130,maxPrice=350,pages=50,betweenTime=2)

    #run.load_cookies()
    #run.load_cookies(cookies)
    run.method()
    input("请手动登录，然后按回车继续")
    #time.sleep(15)

    run.start()

    '''
    cookie=run.get_cookies()

    with open('cookies1.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(cookie))
        f.close()

    print(cookie)
    
     '''
    #run.driv()
    # 当自动化测试脚本执行完毕后，WebDriver对象会自动关闭相关的浏览器进程，释放资源并终止与浏览器的会话。
    # 但是，有时候在测试过程中，脚本出现异常导致未关闭浏览器，这时我们就需要手动调用来关闭浏览器。
    #time.sleep(3)
    #run.sign_out()
