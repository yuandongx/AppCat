import time

from tornado.web import RequestHandler
import hashlib
from xml.etree import ElementTree as ET


def parse_msg_body(msg):
    if isinstance(msg, (str, bytes)):
        return parse_xml(msg)


def parse_xml(data):
    if len(data) == 0:
        return
    xml_data = ET.fromstring(data)
    result = {}
    result["ToUserName"] = xml_data.find('ToUserName').text
    result["FromUserName"] = xml_data.find('FromUserName').text
    result["CreateTime"] = xml_data.find('CreateTime').text
    result["MsgType"] = xml_data.find('MsgType').text
    result["MsgId"] = xml_data.find('MsgId').text
    return result


def make_msg(**kwargs):
    XmlForm = """
                <xml>
                    <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
                    <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
                    <CreateTime>{CreateTime}</CreateTime>
                    <MsgType><![CDATA[text]]></MsgType>
                    <Content><![CDATA[{Content}]]></Content>
                </xml>
                """
    return XmlForm.format(**kwargs)


def check_signature(param, signature):
    sha1 = hashlib.sha1()
    param.sort()
    for p in param:
        sha1.update(p.encode())
    hashcode = sha1.hexdigest()
    return hashcode == signature


class Handler(RequestHandler):
    def get(self):
        signature = self.get_argument("signature", None)
        timestamp = self.get_argument("timestamp", None)
        nonce = self.get_argument("nonce", None)
        echostr = self.get_argument("echostr", None)
        token = "weimaomao"  # 请按照公众平台官网\基本配置中信息填写
        checked = check_signature([token, timestamp, nonce], signature)
        if checked:
            self.write(echostr)
        else:
            self.write("")

    def post(self):
        data = parse_xml(self.request.body)
        msg = {
            "ToUserName": data.get("FromUserName"),
            "FromUserName": data.get("ToUserName"),
            "CreateTime": time.time(),
            "Content": data.get("Content"),
        }
        data = make_msg(**msg)
        self.write(data)
