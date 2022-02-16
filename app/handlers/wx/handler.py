"""
wx handler
"""
import time
import hashlib
from xml.etree import ElementTree as ET
from tornado.web import RequestHandler
from ...settings import WX_TOKEN


def parse_msg_body(msg):
    """
    parse_msg_body
    """
    if isinstance(msg, (str, bytes)):
        return parse_xml(msg)
    return None


def parse_xml(data):
    """
    parse_xml
    """
    if len(data) == 0:
        return {}
    xml_data = ET.fromstring(data)
    result = {"ToUserName": xml_data.find('ToUserName').text,
              "FromUserName": xml_data.find('FromUserName').text,
              "CreateTime": xml_data.find('CreateTime').text,
              "MsgType": xml_data.find('MsgType').text,
              "MsgId": xml_data.find('MsgId').text,
              "Content": xml_data.find('Content').text}
    return result


def make_msg(**kwargs):
    """
    make_msg
    """
    xml_form = """
                <xml>
                    <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
                    <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
                    <CreateTime>{CreateTime}</CreateTime>
                    <MsgType><![CDATA[text]]></MsgType>
                    <Content><![CDATA[{Content}]]></Content>
                </xml>
                """
    return xml_form.format(**kwargs)


def check_signature(param, signature):
    """
    check_signature
    """
    sha1 = hashlib.sha1()
    param.sort()
    for pa in param:
        sha1.update(pa.encode())
    hashcode = sha1.hexdigest()
    return hashcode == signature


class Handler(RequestHandler):
    """Handler"""
    def get(self):
        """

        :rtype: None
        """
        signature = self.get_argument("signature", None)
        timestamp = self.get_argument("timestamp", None)
        nonce = self.get_argument("nonce", None)
        echostr = self.get_argument("echostr", None)
        # token = "weimaomao"  # 请按照公众平台官网\基本配置中信息填写
        token = WX_TOKEN  # 请按照公众平台官网\基本配置中信息填写
        checked = check_signature([token, timestamp, nonce], signature)
        if checked:
            self.write(echostr)
        else:
            self.write("")

    def post(self):
        """

        :rtype: object
        """
        data = parse_xml(self.request.body)
        msg = {
            "ToUserName": data.get("FromUserName"),
            "FromUserName": data.get("ToUserName"),
            "CreateTime": time.time(),
            "Content": data.get("Content"),
        }
        data = make_msg(**msg)
        self.write(data)
