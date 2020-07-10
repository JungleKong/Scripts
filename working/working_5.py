from selenium import webdriver
import time

name = (
    # "13771113786",
    # "13961841700",
    # "13665118166",
    # "15961824673",
    # "15251627686",
    # "13093125996",
    # "13812269202",
    # "18851500521",
    # "18914156223",
    # "13812533905",
    # "15961737832",
    # "18912459175",
    # "13915351375",
    # "13626230192",
    # "13814269180",
    # "15251669724",
    # "13771125450",
    # "13400002797",
    # "15190255305",
    # "13861887024",
    # "13921280134",
    # "15861571269",
    "15951560839",
)

time_five = 120

path = r"D:\anaconda\chromedriver.exe"
url = 'http://skills.kjcxchina.com'

# 行政url
subUrl2 = {
    "/videoDetail.html?id=390&chapter_id=4864",
    "/videoDetail.html?id=390&chapter_id=4865",
    "/videoDetail.html?id=390&chapter_id=4866",
    "/videoDetail.html?id=390&chapter_id=4867",
    "/videoDetail.html?id=390&chapter_id=4868",
    "/videoDetail.html?id=390&chapter_id=4869",
    "/videoDetail.html?id=390&chapter_id=4870",
    "/videoDetail.html?id=390&chapter_id=4871",
    "/videoDetail.html?id=390&chapter_id=4872",
    "/videoDetail.html?id=390&chapter_id=4873",
    "/videoDetail.html?id=399&chapter_id=4913",
    "/videoDetail.html?id=399&chapter_id=4914",
    "/videoDetail.html?id=399&chapter_id=4915",
    "/videoDetail.html?id=399&chapter_id=4916",
    "/videoDetail.html?id=399&chapter_id=4917",
    "/videoDetail.html?id=399&chapter_id=4918",
    "/videoDetail.html?id=399&chapter_id=4919",
    "/videoDetail.html?id=399&chapter_id=4920",
    "/videoDetail.html?id=399&chapter_id=4921",
    "/videoDetail.html?id=1635&chapter_id=10266",
    "/videoDetail.html?id=1635&chapter_id=10267",
    "/videoDetail.html?id=1635&chapter_id=10268",
    "/videoDetail.html?id=1634&chapter_id=10269",
    "/videoDetail.html?id=1635&chapter_id=10264",
    "/videoDetail.html?id=960&chapter_id=6519",
    "/videoDetail.html?id=1058&chapter_id=6607",
    "/videoDetail.html?id=1511&chapter_id=9535",
    "/videoDetail.html?id=1511&chapter_id=9536",
    "/videoDetail.html?id=1511&chapter_id=9537",
    "/videoDetail.html?id=1511&chapter_id=9538",
    "/videoDetail.html?id=1511&chapter_id=9541",
    "/videoDetail.html?id=1631&chapter_id=10249",
    "/videoDetail.html?id=1631&chapter_id=10250",
    "/videoDetail.html?id=1635&chapter_id=10263",
    "/videoDetail.html?id=1635&chapter_id=10265",
    "/videoDetail.html?id=1634&chapter_id=10261",  # 01:24:46
    "/videoDetail.html?id=1634&chapter_id=10262",  # 01:26:26
    "/videoDetail.html?id=1082&chapter_id=6631",  # 01:44:54
    "/videoDetail.html?id=959&chapter_id=9256",  # 42 按钮隐藏，需要移动鼠标才能显示
    "/videoDetail.html?id=1060&chapter_id=6609",  # 47 按钮隐藏，需要移动鼠标才能显示
    "/videoDetail.html?id=1084&chapter_id=6633",  # 59 按钮隐藏，需要移动鼠标才能显示
    "/videoDetail.html?id=1511&chapter_id=9534",  # 45 按钮隐藏，需要移动鼠标才能显示
    "/videoDetail.html?id=1511&chapter_id=9539",  # 48 按钮隐藏，需要移动鼠标才能显示
    "/videoDetail.html?id=1511&chapter_id=9540",  # 52 按钮隐藏，需要移动鼠标才能显示
}

# option = webdriver.ChromeOptions()
# option.add_argument('disable-infobars')
subUrl = (  # 车间url
    '/videoDetail.html?id=98&chapter_id=1203',
    '/videoDetail.html?id=98&chapter_id=1204',
    '/videoDetail.html?id=1634&chapter_id=10269',
    '/videoDetail.html?id=390&chapter_id=4864',
    '/videoDetail.html?id=390&chapter_id=4865',
    '/videoDetail.html?id=390&chapter_id=4866',
    '/videoDetail.html?id=390&chapter_id=4867',
    '/videoDetail.html?id=390&chapter_id=4868',
    '/videoDetail.html?id=390&chapter_id=4869',
    '/videoDetail.html?id=390&chapter_id=4870',
    '/videoDetail.html?id=390&chapter_id=4871',
    '/videoDetail.html?id=390&chapter_id=4872',
    '/videoDetail.html?id=390&chapter_id=4873',
    '/videoDetail.html?id=399&chapter_id=4913',
    '/videoDetail.html?id=399&chapter_id=4914',
    '/videoDetail.html?id=399&chapter_id=4915',
    '/videoDetail.html?id=399&chapter_id=4916',
    '/videoDetail.html?id=399&chapter_id=4917',
    '/videoDetail.html?id=399&chapter_id=4918',
    '/videoDetail.html?id=399&chapter_id=4919',
    '/videoDetail.html?id=399&chapter_id=4920',
    '/videoDetail.html?id=399&chapter_id=4921',
    '/videoDetail.html?id=405&chapter_id=4953',
    '/videoDetail.html?id=405&chapter_id=4954',
    '/videoDetail.html?id=405&chapter_id=4955',
    '/videoDetail.html?id=405&chapter_id=4956',
    '/videoDetail.html?id=405&chapter_id=4957',
    '/videoDetail.html?id=405&chapter_id=4958',
    '/videoDetail.html?id=405&chapter_id=4959',
    '/videoDetail.html?id=405&chapter_id=4960',
    '/videoDetail.html?id=960&chapter_id=6519',
    '/videoDetail.html?id=1511&chapter_id=9535',
    '/videoDetail.html?id=1511&chapter_id=9536',
    '/videoDetail.html?id=1511&chapter_id=9537',
    '/videoDetail.html?id=1511&chapter_id=9538',
    '/videoDetail.html?id=208&chapter_id=2689',
    '/videoDetail.html?id=1511&chapter_id=9541',
    '/videoDetail.html?id=1634&chapter_id=10261',
    '/videoDetail.html?id=1634&chapter_id=10262',
    '/videoDetail.html?id=959&chapter_id=9256',  # 41:39 按钮隐藏，需要移动鼠标才能显示
    '/videoDetail.html?id=1065&chapter_id=6614',  # 54:08 按钮隐藏，需要移动鼠标才能显示
    '/videoDetail.html?id=1269&chapter_id=7952',  # 10:01 按钮隐藏，需要移动鼠标才能显示
    '/videoDetail.html?id=1511&chapter_id=9534',  # 45:00 按钮隐藏，需要移动鼠标才能显示
    '/videoDetail.html?id=1511&chapter_id=9539',  # 47:18 按钮隐藏，需要移动鼠标才能显示
    '/videoDetail.html?id=1511&chapter_id=9540',  # 51:58 按钮隐藏，需要移动鼠标才能显示
)
for j in range(len(name)):
    username = name[j]
    my_driver = webdriver.Chrome(executable_path=path)
    my_driver.maximize_window()
    my_driver.get(url+'/my.html')
    time.sleep(1)
    #
    my_driver.find_element_by_id("phone").send_keys(username)
    my_driver.find_element_by_id("password").send_keys("aa"+username[5:])
    my_driver.find_element_by_id('login').click()
    time.sleep(1)

    # study_record = my_driver.find_elements_by_xpath('//div[@class="myBoxNav"]//li/a')[2]

    for i in range(10):
        # windows_all = my_driver.window_handles
        # my_driver.switch_to.window(windows_all[0])
        # my_driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
        # my_driver.switch_to.window(windows_all[i+1])
        # my_driver.get(url+subUrl[i])
        js = 'window.open("{}");'.format(url+subUrl[i])
        my_driver.execute_script(js)
        windows_all = my_driver.window_handles
        my_driver.switch_to.window(windows_all[i+2])
        while True:
            try:
                my_driver.find_element_by_class_name('prism-big-play-btn').click()
                break
            except:
                time.sleep(1)

    print("正在播放"+username+"第一部分")

    time.sleep(time_five)

    for i in range(len(windows_all)-1):
        my_driver.switch_to.window(windows_all[i+1])
        my_driver.close()
        time.sleep(1)
    my_driver.switch_to.window(windows_all[0])

    for i in range(10, 20):
        js = 'window.open("{}");'.format(url+subUrl[i])
        my_driver.execute_script(js)
        windows_all = my_driver.window_handles
        my_driver.switch_to.window(windows_all[i-9])
        while True:
            try:
                my_driver.find_element_by_class_name('prism-big-play-btn').click()
                break
            except:
                time.sleep(1)
    print("正在播放"+username+"第二部分")

    time.sleep(time_five)

    for i in range(len(windows_all)-1):
        my_driver.switch_to.window(windows_all[i+1])
        my_driver.close()
        time.sleep(1)

    my_driver.switch_to.window(windows_all[0])

    for i in range(20, 30):
        js = 'window.open("{}");'.format(url+subUrl[i])
        my_driver.execute_script(js)
        windows_all = my_driver.window_handles
        my_driver.switch_to.window(windows_all[i-19])
        while True:
            try:
                my_driver.find_element_by_class_name('prism-big-play-btn').click()
                break
            except:
                time.sleep(1)
    print("正在播放"+username+"第三部分")

    time.sleep(time_five)

    for i in range(len(windows_all)-1):
        my_driver.switch_to.window(windows_all[i+1])
        my_driver.close()
        time.sleep(1)

    my_driver.switch_to.window(windows_all[0])

    for i in range(30, 39):
        js = 'window.open("{}");'.format(url+subUrl[i])
        my_driver.execute_script(js)
        windows_all = my_driver.window_handles
        my_driver.switch_to.window(windows_all[i-29])
        while True:
            try:
                my_driver.find_element_by_class_name('prism-big-play-btn').click()
                break
            except:
                time.sleep(1)
    print("正在播放"+username+"第四部分")

    time.sleep(time_five)

    for i in range(len(windows_all)-1):
        my_driver.switch_to.window(windows_all[i+1])
        my_driver.close()
        time.sleep(1)

    my_driver.switch_to.window(windows_all[0])

    for i in range(39, 45):
        js = 'window.open("{}");'.format(url+subUrl[i])
        my_driver.execute_script(js)
        windows_all = my_driver.window_handles
        my_driver.switch_to.window(windows_all[i-38])
        while True:
            try:
                my_driver.find_element_by_class_name('prism-player').click()
                break
            except:
                time.sleep(1)

    print("正在播放"+username+"第五部分")

    time.sleep(time_five)

    for i in range(len(windows_all)-1):
        my_driver.switch_to.window(windows_all[i+1])
        my_driver.close()
        time.sleep(1)
    my_driver.switch_to.window(windows_all[0])

    my_driver.find_elements_by_xpath('//div[@class="myBoxNav"]//li/a')[1].click()
    my_driver.refresh()
    time.sleep(10)
    my_driver.quit()
    print(username+":播放完成----"+ time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    time.sleep(10)

