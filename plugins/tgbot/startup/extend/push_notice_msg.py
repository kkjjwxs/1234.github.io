# coding:utf-8

import sys
import io
import os
import time
import re
import json
import base64
import threading

sys.path.append(os.getcwd() + "/class/core")
import mw

import telebot
from telebot import types
from telebot.util import quick_markup

# 轮播实例

chat_id = -1001578009023
# chat_id = 5568699210


def writeLog(log_str):
    if __name__ == "__main__":
        print(log_str)

    now = mw.getDateFromNow()
    log_file = mw.getServerDir() + '/tgbot/task.log'
    mw.writeFileLog(now + ':' + log_str, log_file, limit_size=5 * 1024)
    return True


def send_msg(bot, tag='ad', trigger_time=300):
    # 信号只在一个周期内执行一次|start
    lock_file = mw.getServerDir() + '/tgbot/lock.json'
    if not os.path.exists(lock_file):
        mw.writeFile(lock_file, '{}')

    lock_data = json.loads(mw.readFile(lock_file))
    if tag in lock_data:
        diff_time = time.time() - lock_data[tag]['do_time']
        if diff_time >= trigger_time:
            lock_data[tag]['do_time'] = time.time()
        else:
            return False, 0, 0
    else:
        lock_data[tag] = {'do_time': time.time()}
    mw.writeFile(lock_file, json.dumps(lock_data))
    # 信号只在一个周期内执行一次|end

    # https://t.me/gjgzs2022 ｜ 19/m
    # 代付支付宝微信❤️淘宝帮付/💰流量变现💰集团收量/🕵️‍♀️实名认证/接码✅过人脸👤 ｜ 28/m
    # 香港高防CDN ｜9/m
    # 🅾️代实名lDCApp🙎‍♂️+86接码全天在线🅾️ | 15/m
    keyboard = [
        [
            types.InlineKeyboardButton(
                text="🅾️代实名lDCApp🙎‍♂️+86接码全天在线🅾️", url='https://t.me/ljh09852')
        ],
        [
            types.InlineKeyboardButton(
                text="香港高防CDN、免实名、试用30天", url='https://www.100dun.com')
        ],
        [
            types.InlineKeyboardButton(
                text="🕵️‍♀️实名认证/接码✅过人脸👤", url='https://t.me/zhanzhangyewu')
        ],
        [
            types.InlineKeyboardButton(
                text="代付支付宝微信❤️淘宝帮付", url='https://t.me/Uxuanzhenpin')
        ],
        [
            types.InlineKeyboardButton(
                text="💰流量变现💰集团收量", url='https://t.me/taohaozhan')
        ],
        [
            types.InlineKeyboardButton(
                text="🙎‍♂️代实名🙍‍♀️过人脸🅾️国际阿里云腾讯云", url='https://t.me/gjgzs2022')
        ],
        [
            types.InlineKeyboardButton(
                text="官网", url='https://github.com/midoks/mdserver-web'),
            types.InlineKeyboardButton(
                text="💎DigitalVirt(赞助商)", url='https://digitalvirt.com/aff.php?aff=154')
        ],
        [
            types.InlineKeyboardButton(
                text="论坛", url='https://bbs.midoks.me'),
            types.InlineKeyboardButton(
                text="搜索", url='https://bbs.midoks.me/search.php'),
            types.InlineKeyboardButton(
                text="@ME", url='tg://user?id=5568699210'),
            types.InlineKeyboardButton(
                text="100RMB/M", url='tg://user?id=5568699210')
        ]
    ]
    markup = types.InlineKeyboardMarkup(keyboard)

    msg_notice = "由于在解决的问题的时候，不给信息，无法了解情况。以后不再群里回答技术问题。全部去论坛提问。在解决问题的过程中，可能需要面板信息，和SSH信息，如无法提供请不要提问。为了让群里都知晓。轮播一年！\n"
    msg_notice += "为了不打扰双方，私聊解决问题先转100U，否则无视!\n"
    msg = bot.send_message(chat_id, msg_notice, reply_markup=markup)

    # print(msg.message_id)
    time.sleep(90)
    try:
        bot.delete_message(
            chat_id=chat_id, message_id=msg.message_id)
    except Exception as e:
        pass


def run(bot):
    try:
        send_msg(bot, 'notice_msg', 90)
    except Exception as e:
        writeLog('-----push_notice_msg error start -------')
        print(mw.getTracebackInfo())
        writeLog('-----push_notice_msg error start -------')
