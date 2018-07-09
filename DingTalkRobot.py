import urllib3
import json
import Common.Const
urllib3.disable_warnings()
CONST = Common.Const


def send_text(text_msg):
    data = {
        "msgtype": "text",
        "text": {
            "content": text_msg
        }
     }
    encoded_data = json.dumps(data).encode('utf-8')
    http = urllib3.PoolManager()
    r = http.request(
        'POST',
        CONST.DINGTALK_ROBOT,
        body=encoded_data,
        headers={'Content-Type':'application/json'}
    )