import os
BASE_DIRS = os.path.dirname(__file__)
# parameter
options = {
    "port": 7000,
}

# setting(配置)

settings = {
    "static_path":os.path.join(BASE_DIRS, "static"),
    "template_path": os.path.join(BASE_DIRS, "tornato_prac_templates"),
    "debug": True
}
