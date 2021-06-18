import json
import requests

from login_claro_video.claro_video_login import LoginClaroVideo

session = requests.Session()
group_id = 742129

acquired_resp_data = LoginClaroVideo.login_portal('dummy@gmail.com', 'dummypass', session)
acquired_resp_data = LoginClaroVideo.push_session(acquired_resp_data, session)
json_resp = LoginClaroVideo.get_purchased_button_info(group_id, acquired_resp_data, session)
json_text = json.dumps(json_resp, indent=4, sort_keys=True)
print(json_text)
