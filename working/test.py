from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys

username = "15052251322"
time_five = 180

path = r"D:\anaconda\chromedriver.exe"
url = 'http://skills.kjcxchina.com'

# 车间url
sub_url = (
    '/videoDetail.html?id=98&chapter_id=1203',
    '/videoDetail.html?id=98&chapter_id=1204',
    '/videoDetail.html?id=208&chapter_id=2689',
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
    '/videoDetail.html?id=959&chapter_id=9256',  # 41:39 按钮隐藏，需要移动鼠标才能显示
    '/videoDetail.html?id=960&chapter_id=6519',
    '/videoDetail.html?id=1065&chapter_id=6614',  # 54:08 按钮隐藏，需要移动鼠标才能显示
    '/videoDetail.html?id=1269&chapter_id=7952',  # 10:01 按钮隐藏，需要移动鼠标才能显示
    '/videoDetail.html?id=1511&chapter_id=9534',  # 45:00 按钮隐藏，需要移动鼠标才能显示
    '/videoDetail.html?id=1511&chapter_id=9535',
    '/videoDetail.html?id=1511&chapter_id=9536',
    '/videoDetail.html?id=1511&chapter_id=9537',
    '/videoDetail.html?id=1511&chapter_id=9538',
    '/videoDetail.html?id=1511&chapter_id=9539',  # 47:18 按钮隐藏，需要移动鼠标才能显示
    '/videoDetail.html?id=1511&chapter_id=9540',  # 51:58 按钮隐藏，需要移动鼠标才能显示
    '/videoDetail.html?id=1511&chapter_id=9541',
    '/videoDetail.html?id=1634&chapter_id=10261',
    '/videoDetail.html?id=1634&chapter_id=10262',
    '/videoDetail.html?id=1634&chapter_id=10269',
)

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
    "/videoDetail.html?id=959&chapter_id=9256",  # 51:58 按钮隐藏，需要移动鼠标才能显示
    "/videoDetail.html?id=960&chapter_id=6519",
    "/videoDetail.html?id=1058&chapter_id=6607",
    "/videoDetail.html?id=1060&chapter_id=6609",  # 51:58 按钮隐藏，需要移动鼠标才能显示
    "/videoDetail.html?id=1082&chapter_id=6631",
    "/videoDetail.html?id=1084&chapter_id=6633",  # 51:58 按钮隐藏，需要移动鼠标才能显示
    "/videoDetail.html?id=1511&chapter_id=9534",  # 51:58 按钮隐藏，需要移动鼠标才能显示
    "/videoDetail.html?id=1511&chapter_id=9535",
    "/videoDetail.html?id=1511&chapter_id=9536",
    "/videoDetail.html?id=1511&chapter_id=9537",
    "/videoDetail.html?id=1511&chapter_id=9538",
    "/videoDetail.html?id=1511&chapter_id=9539",  # 51:58 按钮隐藏，需要移动鼠标才能显示
    "/videoDetail.html?id=1511&chapter_id=9540",
    "/videoDetail.html?id=1511&chapter_id=9541",
    "/videoDetail.html?id=1631&chapter_id=10249",
    "/videoDetail.html?id=1631&chapter_id=10250",
    "/videoDetail.html?id=1634&chapter_id=10261",
    "/videoDetail.html?id=1634&chapter_id=10262",
    "/videoDetail.html?id=1634&chapter_id=10269",
    "/videoDetail.html?id=1635&chapter_id=10263",
    "/videoDetail.html?id=1635&chapter_id=10264",
    "/videoDetail.html?id=1635&chapter_id=10265",
    "/videoDetail.html?id=1635&chapter_id=10266",
    "/videoDetail.html?id=1635&chapter_id=10267",
    "/videoDetail.html?id=1635&chapter_id=10268",
}



