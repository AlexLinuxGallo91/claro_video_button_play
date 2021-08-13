"""
Modulo principal el cual se encarga de almacenar todas las constantes que usan en todo el proyecto,
la mayoria son utilizadas para hacer las peticiones web a la API de Claro Video
"""

LOGIN_MAIN_PAGE = 'https://www.clarovideo.com'

LOGIN_REQ_CLARO_VIDEO = 'https://mfwkweb-api.clarovideo.net/services/user/login?device_id=web&device_category=web&' \
                        'device_model=web&device_type=web&device_so=Firefox&format=json&device_manufacturer=generic&' \
                        'authpn=webclient&authpt={}&api_version=v5.92&region={}&HKS={}&incl' \
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

HTML_BODY_EMAIL_GMAIL_MESSAGE = \
    '<html> <head> <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"> <style> <!-- @font-face ' \
    '{ font-family: Calibri } @font-face { font-family: Tahoma } p.MsoNormal, li.MsoNormal, div.MsoNormal { margin: ' \
    '0cm; margin-bottom: .0001pt; font-size: 11.0pt; font-family: "Calibri", "sans-serif" } a:link, span.MsoHyperlink' \
    ' { color: blue; text-decoration: underline } a:visited, span.MsoHyperlinkFollowed { color: purple; text-decorati' \
    'on: underline } p.MsoAcetate, li.MsoAcetate, div.MsoAcetate { margin: 0cm; margin-bottom: .0001pt; font-size: 8' \
    '.0pt; font-family: "Tahoma", "sans-serif" } span.TextodegloboCar { font-family: "Tahoma", "sans-serif" } span.e' \
    'mailstyle17 { font-family: "Calibri", "sans-serif"; color: windowtext } span.balloontextchar { font-family: "Ta' \
    'homa", "sans-serif" } span.EstiloCorreo21 { font-family: "Calibri", "sans-serif"; color: #4A442A } .MsoChpDefau' \
    'lt { font-size: 10.0pt } @page WordSection1 { margin: 70.85pt 3.0cm 70.85pt 3.0cm } div.WordSection1 {} --> </s' \
    'tyle> </head> <body lang="ES-MX" link="blue" vlink="purple"> <div class="WordSection1"> <p class="MsoNormal"></' \
    'p> <div> <p class="MsoNormal"> <img width="677" height="138" id="_x0031__x0020_Imagen" src="http://200.57.138.13' \
    '4/ITOC/images/bannerItoc.jpg" alt="bannerItoc.jpg"> </p> <p class="MsoNormal"></p> <p>Se notifica una inconsiste' \
    'ncia del boton de play, detectada en el monitoreo interno de Triara del Servicio de Claro Video. Se adjunta ' \
    'archivo excel con la informacion de inconsistencias detectadas.</p> <p cl' \
    'ass="MsoNormal"> <span lang="EN-US"></span> </p> <p class="MsoNormal"> <span style="color:#1F497D"></span> </p> ' \
    '<br> <p class="MsoNormal"> <span style="color:black">Saludos cordiales,</span> </p> <p class="MsoNormal">' \
    '</p> </div> <br> <p class="MsoNormal"> <span style="color:#4A442A"></span> </p> <table class="MsoNormalTable" ' \
    'border="0" cellspacing="6" cellpadding="0" width="567" style="width:15.0cm"> <tbody> <tr style="height:22.5pt">' \
    ' <td width="142" rowspan="3" valign="top" style="width:106.5pt; padding:0cm 0cm 0cm 0cm; height:22.5pt"> <p ' \
    'class="MsoNormal"> <img width="100" height="88" id="Imagen_x0020_3" src="http://200.57.138.134/ITOC/images/tri' \
    'aralogo.jpg" alt="triaralogo.jpg"> </p> <p class="MsoNormal" align="center" style="text-align:left"> <span sty' \
    'le="font-size:8.0pt; color:gray">ISO 9001:2008</span> <span style="color:#4A442A"></span> </p> <p class="MsoNo' \
    'rmal" align="center" style="text-align:left"> <span style="font-size:8.0pt; color:gray">ISO 14001:2004</span>' \
    ' <span style="color:#4A442A"></span> </p> <p class="MsoNormal" align="center" style="text-align:left"> <span ' \
    'style="font-size:8.0pt; color:gray">ISO 27001:2013</span> <span style="color:#4A442A"></span> </p> <p class="M' \
    'soNormal" align="center" style="text-align:left"> <span style="font-size:8.0pt; color:gray">ISO 20000-1:2011</' \
    'span> <span style="color:#4A442A"></span> </p> <p class="MsoNormal" align="center" style="text-align:left"> <s' \
    'pan style="font-size:8.0pt; color:gray">ICREA-STD-131-2013</span> <span style="color:#4A442A"></span> </p> <p ' \
    'class="MsoNormal" align="center" style="text-align:left"> <span style="font-size:8.0pt; color:gray">ISAE3402/S' \
    'SAE16</span> <span style="color:#4A442A"></span> </p> </td> <td width="407" valign="top" style="width:305.25pt; ' \
    'padding:0cm 0cm 0cm 0cm; height:22.5pt"> <p class="MsoNormal"> <span style="font-size:7.5pt; font-family:" Ari' \
    'al?,?sans-serif?;color:#666666?=""></span> </p> <p class="MsoNormal"> <span style="font-size:9pt; font-family:"' \
    ' Arial?,?sans-serif?;color:#666666?="">Centro Integral de Monitoreo y Gestión ITOC</span> <span style="color:#' \
    '4A442A"></span> </p> </td> </tr> <tr style="height:41.25pt"> <td style="padding:0cm 0cm 0cm 0cm; height:41.25p' \
    't"> <p class="MsoNormal"> <span style="font-size:7.5pt; color:#666666">Triara Data Center</span> <span style=' \
    '"font-size:7.5pt; color:#1F497D"></span> <span style="color:#4A442A"></span> </p> <p class="MsoNormal"> <span ' \
    'style="font-size:7.5pt; color:#666666">Libramiento Santa Rosa 111</span> <span style="color:#4A442A"></span> ' \
    '</p> <p class="MsoNormal"> <span style="font-size:7.5pt; color:#666666">Col. Futuro Apodaca, Apodaca NL 66600' \
    '</span> <span style="font-size:7.5pt; color:#1F497D"></span> <span style="color:#4A442A"></span> </p> </td> ' \
    '</tr> <tr style="height:52.5pt"> <td valign="top" style="padding:0cm 0cm 0cm 0cm; height:52.5pt"> <p class="' \
    'MsoNormal"> <span style="font-size:7.5pt; color:#666666">Telefono: (81) 81962744</span> <span style="color:' \
    '#4A442A"></span> </p> <p class="MsoNormal"> <span style="font-size:7.5pt; color:#666666"> <br> Correo: </span> ' \
    '<u> <span style="font-size:7.5pt; color:blue">operacion.itoc@triara.com</span> </u> <span style="color:#4A442A">' \
    '</span> </p> </td> </tr> </tbody> </table> <p class="MsoNormal"> <img width="299" height="50" id="Imagen_x0020_2' \
    '" src="http://200.57.138.134/ITOC/images/telmexlogo.jpg" alt=" Description: Telmex estÃ¡ contigo"> </p> <p class' \
    '="MsoNormal"> <span style="color:#4A442A"></span> </p> <p class="MsoNormal"> <span style="color:#4A442A"></span>' \
    ' </p> <p class="MsoNormal"></p> </div> <font size="2" face="Arial">Aviso de Privacidad: http://www.telmex.com/' \
    'web/acerca-de-telmex/aviso-triara </font> </body></html>'

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
