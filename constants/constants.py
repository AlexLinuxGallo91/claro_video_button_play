"""
Modulo principal el cual se encarga de almacenar todas las constantes que usan en todo el proyecto,
la mayoria son utilizadas para hacer las peticiones web a la API de Claro Video
"""

LOGIN_MAIN_PAGE = 'https://www.clarovideo.com'

LOGIN_REQ_CLARO_VIDEO = 'https://mfwkweb-api.clarovideo.net/services/user/login?device_id=web&device_category=web&device_' \
                        'model=web&device_type=web&device_so=Firefox&format=json&device_manufacturer=generic&authpn=' \
                        'webclient&authpt={}&api_version=v5.92&region={}&HKS={}&incl' \
                        'udpaywayprofile=true'

PUSH_SESION_REQ_CLARO_VIDEO = "https://mfwkweb-api.clarovideo.net/services/user/push_session?user_id={}&" \
                              "device_id=web&device_category=web&device_model=web&device_type=web&format=json&" \
                              "device_so=Chrome&device_manufacturer=generic&authpn=webclient&authpt={}" \
                              "&api_version=v5.93&region={}&HKS={}"

BTN_REQ_CLARO_VIDEO = 'https://mfwkweb-api.clarovideo.net/services/payway/purchasebuttoninfo?device_id=web&device_cat' \
                      'egory=web&device_model=web&device_type=web&device_so=Chrome&format=json&device_manufacturer=' \
                      'generic&authpn=webclient&authpt={}&api_version=v5.93&region={}&HKS={}&user_id={}&' \
                      'group_id={}'

COOKIE_PHPSESSION_ID = 'PHPSESSID'

POST_STARTER_HEADER_INFO = 'https://mfwkweb-api.clarovideo.net/services/user/startheaderinfo?device_id=' \
                           'web&device_category=web&device_manufacturer=generic&device_model=web&device_type=web&' \
                           'api_version=v5.93&authpn=webclient&authpt={}&format=json&device_so=Chrome&' \
                           'HKS={}'

REQUEST_URL_COMMON = 'http://10.20.1.92:9200/common_clarovideo/grupo/{}'

ARG_CORREO = "correo"
ARG_PASSWORD = "password"
ARG_REGION = "region"
ARG_NODO = "nodo"
ARG_FILTER_ID = "filter_id"
ARG_NODE_ID = "node_id"

