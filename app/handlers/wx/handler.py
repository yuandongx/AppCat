from tornado.web import RequestHandler
import hashlib
from xml.etree import ElementTree as ET


def parse_xml(data):
    if len(data) == 0:
        return
    xml_data = ET.fromstring(data)
    


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
        print(self.request, "<<<32343")
        print(dir(self.request), "<<<<1111")
        print(dir(self.request.body), "<<<<1111")
        print(self.request.body, "<<<<1111")
