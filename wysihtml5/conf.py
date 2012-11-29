#-*- coding: utf-8 -*-

from copy import deepcopy

from django.conf import settings


WYSIHTML5_TOOLBAR = getattr(settings, "WYSIHTML5_TOOLBAR", {})


TOOLBAR_CONF = {
    "formatBlockHeader": { 
        "active": True,
        "command_name": "formatBlock",
        "render_icon": "wysihtml5.widgets.render_formatBlockHeader_icon"
    },
    "formatBlockParagraph": { 
        "active": True,
        "command_name": "formatBlock",
        "render_icon": "wysihtml5.widgets.render_formatBlockParagraph_icon"
    },
    "bold": { 
        "active": True,
        "command_name": "bold",
        "render_icon": "wysihtml5.widgets.render_bold_icon"
    },
    "italic": { 
        "active": True,
        "command_name": "italic",
        "render_icon": "wysihtml5.widgets.render_italic_icon"
    },
    "underline": { 
        "active": True,
        "command_name": "underline",
        "render_icon": "wysihtml5.widgets.render_underline_icon"
    },
    "justifyLeft": { 
        "active": True,
        "command_name": "justifyLeft",
        "render_icon": "wysihtml5.widgets.render_justifyLeft_icon"
    },
    "justifyCenter": { 
        "active": True,
        "command_name": "justifyCenter",
        "render_icon": "wysihtml5.widgets.render_justifyCenter_icon"
    },
    "justifyRight": { 
        "active": True,
        "command_name": "justifyRight",
        "render_icon": "wysihtml5.widgets.render_justifyRight_icon"
    },
    "insertOrderedList": { 
        "active": True,
        "command_name": "insertOrderedList",
        "render_icon": "wysihtml5.widgets.render_insertOrderedList_icon"
    },
    "insertUnorderedList": { 
        "active": True,
        "command_name": "insertUnorderedList",
        "render_icon": "wysihtml5.widgets.render_insertUnorderedList_icon"
    },
    "insertImage": { 
        "active": True,
        "command_name": "insertImage",
        "render_icon": "wysihtml5.widgets.render_insertImage_icon",
        "render_dialog": "wysihtml5.widgets.render_insertImage_dialog"
    },
    "createLink": { 
        "active": True,
        "command_name": "createLink",
        "render_icon": "wysihtml5.widgets.render_createLink_icon",
        "render_dialog": "wysihtml5.widgets.render_createLink_dialog"
    },
    "insertHTML": { 
        "active": True,
        "command_name": "insertHTML",
        "command_value": "<blockquote>quote</blockquote>",
        "render_icon": "wysihtml5.widgets.render_insertHTML_icon"
    },
    "foreColor": { 
        "active": True,
        "command_name": "foreColor",
        "render_icon": "wysihtml5.widgets.render_foreColor_icon"
    },
    "changeView": { 
        "active": True,
        "command_name": "change_view",
        "render_icon": "wysihtml5.widgets.render_changeView_icon"
    },
}

def initialize_toolbar_conf():
    for key in WYSIHTML5_TOOLBAR:
        if key in TOOLBAR_CONF:
            for subkey in WYSIHTML5_TOOLBAR[key]:
                TOOLBAR_CONF[key][subkey] = WYSIHTML5_TOOLBAR[key][subkey]
        else:
            TOOLBAR_CONF[key] = WYSIHTML5_TOOLBAR[key]

initialize_toolbar_conf()
