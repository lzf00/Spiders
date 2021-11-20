#-*- codeing = utf-8 -*-
#coding=utf-8
# @Time : 2021/11/16 19:54
# @Author : lzf
# @File : Summarizer.py
# @Software :PyCharm
from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import nltk

LANGUAGE = "english"
SENTENCES_COUNT = 1

# if __name__ == "__main__":
#     #url = "https://en.wikipedia.org/wiki/Automatic_summarization"
#     #parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
#     nltk.download ( 'punkt' )
#     # or for plain text files
#     # parser = PlaintextParser.from_file("document.txt", Tokenizer(LANGUAGE))
#     parser = PlaintextParser.from_string("On August 23, Israel’s Ministry of Defense announced successful flight tests of the Iron Dome missile defense system with the United States. The test took place at White Sands Missile Range in New Mexico and demonstrated the first of two Iron Dome batteries configured for U.S. Army service under the Interim Fire Protection Capability (IFPC) program. Each battery will feature 6 launchers, a radar unit, a battle management center, and 120 interceptors.", Tokenizer(LANGUAGE))
#     stemmer = Stemmer(LANGUAGE)
#
#     summarizer = Summarizer(stemmer)
#     summarizer.stop_words = get_stop_words(LANGUAGE)
#
#     for sentence in summarizer(parser.document, SENTENCES_COUNT):
#         print(sentence)



from aip import AipNlp
""" 你的 APPID AK SK """
APP_ID = '25179895'
API_KEY = 'vzhF4GPEcVk5mkL1rAoLfvEC'
SECRET_KEY = 'lGTxmx0DKlQY715B92dU64HlBTByfTZY'
client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
#content = "8月23日，以色列国防部宣布与美国成功试飞铁穹导弹防御系统。测试在新墨西哥州的白沙导弹靶场进行，展示了根据临时防火能力 (IFPC) 计划为美国陆军服务配置的两个铁穹电池中的第一个。每个电池将配备 6 个发射器、一个雷达装置、一个战斗管理中心和 120 个拦截器。"
#content = "On May 28, Reuters reported that ?U.S. officials are considering suspending F-35 training for Turkish pilots as Turkey continues to move forward with its plans to purchase Russia’s S-400 and and missile defense system. The delivery of F-35 equipment to Turkey was previously halted in late March due to U.S. objection to the planned purchase. As Turkish military personnel receive training in Russia for the S-400 program, Turkish pilots continue to receive F-35 training at Luke Air Force Base in Arizona. U.S. officials argue that Turkey’s deployment of the S-400 deployment poses a threat to the F-35 program."
content="On August 23, Israel’s Ministry of Defense announced successful flight tests of the Iron Dome missile defense system with the United States. The test took place at White Sands Missile Range in New Mexico and demonstrated the first of two Iron Dome batteries configured for U.S. Army service under the Interim Fire Protection Capability (IFPC) program. Each battery will feature 6 launchers, a radar unit, a battle management center, and 120 interceptors."
print(len(content))
maxSummaryLen = 1000
""" 如果有可选参数 """
options = {}
options["title"] = "US Tests Iron Dome For Army Use"
""" 带参数调用新闻摘要接口 """
sumy=client.newsSummary(content, maxSummaryLen, options)
print(sumy['summary'])
print(len(sumy['summary']))
