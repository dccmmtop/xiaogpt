import requests

keyword = "电脑"
base_url = "http://127.0.0.1:4567"


def include(target, source):
    for msg in target:
        if msg in source:
            return True
    return False


def send_request(url, params=""):
    url = base_url + url
    response = requests.get(url, data={})
    if response.status_code != 200:
        msg = "请求控制电脑失败, 返回的状态码是 " + str(response.status_code)
        print(msg)
        return msg

    msg = response.text
    print(msg)
    return msg


def router(msg):
    msg = msg.replace(keyword, "")
    print(msg)
    if include(["增大音量", "调大音量", "加大音量", "音量加"], msg):
        return send_request("/volAdd")
    if include(["减少音量", "降低音量", "音量减"], msg):
        return send_request("/volSub")
    if include(["音量百分之十", "调到百分之十"], msg):
        return send_request("/volSet10")
    if include(["音量百分之五十", "调到百分之五十"], msg):
        return send_request("/volSet50")
    if include(["音量百分之八十", "调到百分之八十"], msg):
        return send_request("/volSet80")
    if include(["休眠", "睡眠"], msg):
        return send_request("/sleep")
    if include(["静音", "取消静音"], msg):
        return mute_toggle(msg)
    return "您的电脑还不识别这个命令哦"


def is_control_pc(msg):
    print("电脑 " + msg)
    return msg.startswith(keyword)


def mute_toggle(msg):
    if send_request("/changeVol") == "0":
        return "已" + msg
    return msg + "失败"
