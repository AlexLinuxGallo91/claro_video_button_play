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

ARG_USER = "user"
ARG_PASSWORD = "password"
ARG_REGION = "region"
ARG_FILTER_ID = "filter_id"
ARG_NODE_ID = "node_id"

SUBJECT_MAIL_INCONSISTENCIA_PLAY_BUTTON = 'Notificación de inconsistencia en play button en los nodos {} de ' \
                                          'la región {}.'

# HTML
HTML_MSG_NOTIFICACION_PLAY_BUTTON = '<p>Se notifica una inconsistencia del boton de play, detectada en el monitoreo ' \
                                    'interno de Triara del Servicio de Claro Video:</p><br>'

HTML_TABLE = '<table style="{}">{}</table>'
HTML_TABLE_TR = '<tr style="{}">{}</tr>'
HTML_TABLE_TH = '<th style="{}">{}</th>'
HTML_TABLE_TD = '<td style="{}">{}</td>'
HTML_HREF = '<a href="{}">{}</a>'

# HTML STYLES
HTML_STYLE_BORDER_TABLE = 'border: 1px dotted black; border-collapse: collapse; padding: 5px;'
HTML_STYLE_HEADER = 'border: 1px dotted black; border-collapse: collapse; background: #DEEAF6; padding: 5px;'

HTML_LISTA_HEADERS_PUSH_BUTTON = ['Nodo', 'Group_id', 'Titulo', 'Boton Play', 'Vigente', 'Descripcion']

# CATALAGOS
CAT_CATALAGO = 'Catalago'
CAT_FILTER_ID_CATALAGO = 9482

CAT_CATALAGO_PELICULAS = 'Catalago Peliculas'
CAT_NODE_ID_CATALAGO_PELICULAS = 102686

CAT_CATALAGO_SERIES = 'Catalago Series'
CAT_NODE_ID_CATALAGO_SERIES = 102687

CAT_HBO_PELICULAS = 'HBO Peliculas'
CAT_FILTER_ID_HBO_PELICULAS = 31069

CAT_HBO_SERIES = 'HBO Series'
CAT_FILTER_ID_HBO_SERIES = 31049

CAT_NOGGIN = 'Noggin'
CAT_NODE_ID_NOGGIN = 102737

CAT_EDYE = 'Edye'
CAT_NODE_ID_EDYE = 102738

CAT_PARAMOUNT_SERIES = 'Paramount Series'
CAT_FILTER_ID_PARAMOUNT_SERIES = 36125

CAT_PARAMOUNT_PELICULAS = 'Paramount Peliculas'
CAT_FILTER_ID_PARAMOUNT_PELICULAS = 36217

CAT_PICARDIA_NACIONAL = 'Picardia Nacional'
CAT_NODE_ID_PICARDIA_NACIONAL = 102741

CAT_INDYCAR = 'INDYCAR'
CAT_FILTER_ID_INDYCAR = 38146

CAT_STINGRAY_KARAOKE_FIESTA_KARAOKE = 'Stingray Karaoke / Fiesta Karaoke'
CAT_FILTER_ID_STINGRAY_KARAOKE_FIESTA_KARAOKE_1 = 38485
CAT_FILTER_ID_STINGRAY_KARAOKE_FIESTA_KARAOKE_2 = 38503

CAT_STINGRAY_KARAOKE_PORTUGUES = 'Stingray Karaoke / En portugués'
CAT_FILTER_ID_STINGRAY_KARAOKE_PORTUGUES = 38504

CAT_STINGRAY_KARAOKE_HIPHOP = 'Stingray Karaoke / hiphop'
CAT_FILTER_ID_STINGRAY_KARAOKE_HIPHOP = 38540

CAT_STINGRAY_KARAOKE_ROCK = 'Stingray Karaoke / Rock'
CAT_FILTER_ID_STINGRAY_KARAOKE_ROCK = 38539

CAT_STINGRAY_KARAOKE_DISNEY = 'Stingray Karaoke / Disney'
CAT_FILTER_ID_STINGRAY_KARAOKE_DISNEY = 38488

CAT_STINGRAY_KARAOKE_FESTIVOS = 'Stingray Karaoke / Festivos'
CAT_FILTER_ID_STINGRAY_KARAOKE_FESTIVOS = 38489

CAT_STINGRAY_QUELLO_TODOS_LOS_PROGRAMAS = 'Stingray Quello / Todos los programas'
CAT_FILTER_ID_STINGRAY_QUELLO_TODOS_LOS_PROGRAMAS = 38466

CAT_ATRES_SERIES = 'atres / series'
CAT_FILTER_ID_ATRES_SERIES = 39597

CAT_ATRES_PROGRAMAS = 'atres / programas'
CAT_FILTER_ID_ATRES_PROGRAMAS = 39581

CAT_ATRES_PELÍCULAS = 'atres / películas'
CAT_FILTER_ID_ATRES_PELÍCULAS = 39522

LIST_FILTER_ACTIVE_TYPES = [
    'Type 63',
    'Type 63D',
    'Type 66',
    'Type 66D',
    'Type 43D',
    'Type 46D',
    'Type 3',
    'Type 6'
]

DICT_NODOS = [
    {'node_id': CAT_NODE_ID_CATALAGO_PELICULAS, 'filter_id': '', 'node_name': CAT_CATALAGO_PELICULAS},
    {'node_id': CAT_NODE_ID_CATALAGO_SERIES, 'filter_id': '', 'node_name': CAT_CATALAGO_SERIES},
    {'node_id': CAT_NODE_ID_NOGGIN, 'filter_id': '', 'node_name': CAT_NOGGIN},
    {'node_id': CAT_NODE_ID_EDYE, 'filter_id': '', 'node_name': CAT_EDYE},
    {'node_id': CAT_NODE_ID_PICARDIA_NACIONAL, 'filter_id': '', 'node_name': CAT_PICARDIA_NACIONAL},
    {'node_id': '', 'filter_id': CAT_FILTER_ID_CATALAGO, 'node_name': CAT_CATALAGO},
    {'node_id': '', 'filter_id': CAT_FILTER_ID_HBO_PELICULAS, 'node_name': CAT_HBO_PELICULAS},
    {'node_id': '', 'filter_id': CAT_FILTER_ID_HBO_SERIES, 'node_name': CAT_HBO_SERIES},
    {'node_id': '', 'filter_id': CAT_FILTER_ID_PARAMOUNT_SERIES, 'node_name': CAT_PARAMOUNT_SERIES},
    {'node_id': '', 'filter_id': CAT_FILTER_ID_PARAMOUNT_PELICULAS, 'node_name': CAT_PARAMOUNT_PELICULAS},
    {'node_id': '', 'filter_id': CAT_FILTER_ID_INDYCAR, 'node_name': CAT_INDYCAR},
    # {'node_id': '', 'filter_id': CAT_FILTER_ID_STINGRAY_KARAOKE_FIESTA_KARAOKE_1,
    #  'node_name': CAT_STINGRAY_KARAOKE_FIESTA_KARAOKE},
    {'node_id': '', 'filter_id': CAT_FILTER_ID_STINGRAY_KARAOKE_FIESTA_KARAOKE_2,
     'node_name': CAT_STINGRAY_KARAOKE_FIESTA_KARAOKE},
    {'node_id': '', 'filter_id': CAT_FILTER_ID_STINGRAY_KARAOKE_PORTUGUES, 'node_name': CAT_STINGRAY_KARAOKE_PORTUGUES},
    {'node_id': '', 'filter_id': CAT_FILTER_ID_STINGRAY_KARAOKE_HIPHOP, 'node_name': CAT_STINGRAY_KARAOKE_HIPHOP},
    {'node_id': '', 'filter_id': CAT_FILTER_ID_STINGRAY_KARAOKE_ROCK, 'node_name': CAT_STINGRAY_KARAOKE_ROCK},
    {'node_id': '', 'filter_id': CAT_FILTER_ID_STINGRAY_KARAOKE_DISNEY, 'node_name': CAT_STINGRAY_KARAOKE_DISNEY},
    {'node_id': '', 'filter_id': CAT_FILTER_ID_STINGRAY_KARAOKE_FESTIVOS, 'node_name': CAT_STINGRAY_KARAOKE_FESTIVOS},
    {'node_id': '', 'filter_id': CAT_FILTER_ID_STINGRAY_QUELLO_TODOS_LOS_PROGRAMAS,
     'node_name': CAT_STINGRAY_QUELLO_TODOS_LOS_PROGRAMAS},
    {'node_id': '', 'filter_id': CAT_FILTER_ID_ATRES_SERIES, 'node_name': CAT_ATRES_SERIES},
    {'node_id': '', 'filter_id': CAT_FILTER_ID_ATRES_PROGRAMAS, 'node_name': CAT_ATRES_PROGRAMAS},
    {'node_id': '', 'filter_id': CAT_FILTER_ID_ATRES_PELÍCULAS, 'node_name': CAT_ATRES_PELÍCULAS},
]
