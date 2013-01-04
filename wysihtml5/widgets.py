#-*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.admin.widgets import AdminTextareaWidget
from django.forms.util import flatatt
from django.utils.encoding import force_unicode
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _

from wysihtml5.conf import EDITOR_CONF, TOOLBAR_CONF
from wysihtml5.utils import get_function


render_cmd_icon = {}
render_cmd_dialog = {}

def render_blank(id):
    return u''

def render_createLink_dialog(id):
    return u'\
<div data-wysihtml5-dialog="createLink" style="display:none">\
  <label>%(_link_)s:</label>&nbsp;\
  <input data-wysihtml5-dialog-field="href" value="http://">\
  <a data-wysihtml5-dialog-action="save" class="button">%(_ok_)s</a>&nbsp;\
  <a data-wysihtml5-dialog-action="cancel" class="button">%(_cancel_)s</a>\
</div>' % { "_link_": _("Link"),
            "_ok_": _("Ok"),
            "_cancel_": _("Cancel")
        }


def render_insertImage_dialog(id):
    return u'\
<div data-wysihtml5-dialog="insertImage" style="display:none">\
  <label>%(_link_)s:</label>&nbsp;\
  <input data-wysihtml5-dialog-field="src" value="http://">\
  <a data-wysihtml5-dialog-action="save" class="button">%(_ok_)s</a>&nbsp;\
  <a data-wysihtml5-dialog-action="cancel" class="button">%(_cancel_)s</a>\
</div>' % { "_link_": _("Image"),
            "_ok_": _("Ok"),
            "_cancel_": _("Cancel")
        }


def render_formatBlockHeader_icon(id):
    return u'\
    <span data-wysihtml5-command-group="%(command_name)s" title="Format text header" class="heading-selector">\
      <div>\
        <span data-wysihtml5-command="%(command_name)s" data-wysihtml5-command-value="h1">H1</span>\
        <span data-wysihtml5-command="%(command_name)s" data-wysihtml5-command-value="h2">H2</span>\
        <span data-wysihtml5-command="%(command_name)s" data-wysihtml5-command-value="h3">H3</span>\
        <span data-wysihtml5-command="%(command_name)s" data-wysihtml5-command-value="h4">H4</span>\
        <span data-wysihtml5-command="%(command_name)s" data-wysihtml5-command-value="h5">H5</span>\
        <span data-wysihtml5-command="%(command_name)s" data-wysihtml5-command-value="h6">H6</span>\
      </div>\
    </span>' % { "command_name": TOOLBAR_CONF['formatBlockHeader']['command_name'] }

def render_formatBlockParagraph_icon(id):
    return u'<span data-wysihtml5-command="%(command_name)s" title="Make a paragraph block" data-wysihtml5-command-value="p" class="command format-block-p"></span>' % { "command_name": TOOLBAR_CONF['formatBlockParagraph']['command_name'] }

def render_bold_icon(id):
    return u'<span data-wysihtml5-command="%(command_name)s" title="Make text bold (CTRL + B)" class="command"></span>' % { "command_name": TOOLBAR_CONF['bold']['command_name'] }

def render_italic_icon(id):
    return u'<span data-wysihtml5-command="%(command_name)s" title="Make text italic (CTRL + I)" class="command"></span>' % { "command_name": TOOLBAR_CONF['italic']['command_name'] }

def render_underline_icon(id):
    return u'<span data-wysihtml5-command="%(command_name)s" title="Underline text (CTRL + U)" class="command"></span>' % { "command_name": TOOLBAR_CONF['underline']['command_name'] }

def render_justifyLeft_icon(id):
    return u'<span data-wysihtml5-command="%(command_name)s" title="Paragraph left justified" class="command"></span>' % { "command_name": TOOLBAR_CONF['justifyLeft']['command_name'] }

def render_justifyCenter_icon(id):
    return u'<span data-wysihtml5-command="%(command_name)s" title="Paragraph center justified" class="command"></span>' % { "command_name": TOOLBAR_CONF['justifyCenter']['command_name'] }

def render_justifyRight_icon(id):
    return u'<span data-wysihtml5-command="%(command_name)s" title="Paragraph right justified" class="command"></span>' % { "command_name": TOOLBAR_CONF['justifyRight']['command_name'] }

def render_insertOrderedList_icon(id):
    return u'<span data-wysihtml5-command="%(command_name)s" title="Insert an ordered list" class="command"></span>' % { "command_name": TOOLBAR_CONF['insertOrderedList']['command_name'] }

def render_insertUnorderedList_icon(id):
    return u'<span data-wysihtml5-command="%(command_name)s" title="Insert an unordered list" class="command"></span>' % { "command_name": TOOLBAR_CONF['insertUnorderedList']['command_name'] }

def render_insertImage_icon(id):
    return u'<span data-wysihtml5-command="%(command_name)s" title="Insert an image" class="command insert-image"></span>' % { 'command_name': TOOLBAR_CONF['insertImage']['command_name'] }

def render_createLink_icon(id):
    return u'<span data-wysihtml5-command="%(command_name)s" title="Insert a link" class="command create-link"></span>' % { 'command_name': TOOLBAR_CONF['createLink']['command_name'] }

def render_insertHTML_icon(id):
    return u'<span data-wysihtml5-command="%(command_name)s" title="Insert a quote" class="command" data-wysihtml5-command-value="%(command_value)s"></span>'  % {  'command_name': TOOLBAR_CONF['insertHTML']['command_name'] , 'command_value': TOOLBAR_CONF['insertHTML']['command_value'] }

def render_foreColor_icon(id):
    return u'\
      <span data-wysihtml5-command-group="%(command_name)s" title="Color the selected text" class="fore-color">\
      <div>\
        <span data-wysihtml5-command="%(command_name)s" data-wysihtml5-command-value="silver" unselectable="on"></span>\
        <span data-wysihtml5-command="%(command_name)s" data-wysihtml5-command-value="gray" unselectable="on"></span>\
        <span data-wysihtml5-command="%(command_name)s" data-wysihtml5-command-value="maroon" unselectable="on"></span>\
        <span data-wysihtml5-command="%(command_name)s" data-wysihtml5-command-value="red" unselectable="on"></span>\
        <span data-wysihtml5-command="%(command_name)s" data-wysihtml5-command-value="purple" unselectable="on"></span>\
        <span data-wysihtml5-command="%(command_name)s" data-wysihtml5-command-value="green" unselectable="on"></span>\
        <span data-wysihtml5-command="%(command_name)s" data-wysihtml5-command-value="olive" unselectable="on"></span>\
        <span data-wysihtml5-command="%(command_name)s" data-wysihtml5-command-value="navy" unselectable="on"></span>\
        <span data-wysihtml5-command="%(command_name)s" data-wysihtml5-command-value="blue" unselectable="on"></span>\
      </div>\
    </span>' % { 'command_name': TOOLBAR_CONF['foreColor']['command_name'] }

def render_changeView_icon(id):
    return '<span data-wysihtml5-action="%(command_name)s" title="Show HTML" class="action" unselectable="on"></span>' % { 'command_name': TOOLBAR_CONF['changeView']['command_name'] }

def render_toolbar_widget(id):
    widget = u'\
<div id="%(id)s-toolbar" class="wysihtml5-editor-toolbar">\
  <div class="commands">' % { "id": id }
    widget += get_function(render_cmd_icon['formatBlockHeader'])(id)
    widget += get_function(render_cmd_icon['formatBlockParagraph'])(id)
    widget += get_function(render_cmd_icon['bold'])(id)
    widget += get_function(render_cmd_icon['italic'])(id)
    widget += get_function(render_cmd_icon['underline'])(id)
    widget += get_function(render_cmd_icon['justifyLeft'])(id)
    widget += get_function(render_cmd_icon['justifyCenter'])(id)
    widget += get_function(render_cmd_icon['justifyRight'])(id)
    widget += get_function(render_cmd_icon['insertOrderedList'])(id)
    widget += get_function(render_cmd_icon['insertUnorderedList'])(id)
    widget += get_function(render_cmd_icon['insertImage'])(id)
    widget += get_function(render_cmd_icon['createLink'])(id)
    widget += get_function(render_cmd_icon['insertHTML'])(id)
    widget += get_function(render_cmd_icon['foreColor'])(id)
    widget += get_function(render_cmd_icon['changeView'])(id)
    widget += u'\
  </div>\
  <div class="wysihtml5-dialogs">'
    widget += get_function(render_cmd_dialog['createLink'])(id)
    widget += get_function(render_cmd_dialog['insertImage'])(id)
    widget += u'\
  </div>\
</div>'
    return widget

def render_js_init_widget(id, config):
    options = {"id": id}
    options.update(config)
    if options.get('toolbar', 'null') == 'null':
        options['toolbar'] = '"%s-toolbar"' % id
    widget = u'''
<script>
  var editor = new wysihtml5.Editor("%(id)s",{
    name:                 %(name)s,
    style:                %(style)s,
    toolbar:              %(toolbar)s,
    autoLink:             %(autoLink)s,
    parserRules:          %(parserRules)s,
    parser:               %(parser)s,
    composerClassName:    %(composerClassName)s,
    bodyClassName:        %(bodyClassName)s,
    stylesheets:          %(stylesheets)s,
    placeholderText:      %(placeholderText)s,
    allowObjectResizing:  %(allowObjectResizing)s,
    supportTouchDevices:  %(supportTouchDevices)s
  });
</script>''' % options
    return widget

class Wysihtml5AdminTextareaWidget(AdminTextareaWidget):

    class Media:
        css = {
            'all': (settings.STATIC_URL + "admin/wysihtml5/css/toolbar.css",)
        }
        js = (settings.STATIC_URL + "admin/wysihtml5/js/advanced.js",
              settings.STATIC_URL + "admin/wysihtml5/js/wysihtml5-0.4.0pre.min.js")

    def __init__(self, attrs=None):
        if not attrs:
            attrs = {"rows": 25}
        elif not attrs.get("rows", False):
            attrs.update({"rows": 25})
        super(Wysihtml5AdminTextareaWidget, self).__init__(attrs=attrs)

    def render(self, name, value, attrs=None):
        if value is None: value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        textarea_widget = u'<textarea%s>%s</textarea>' % (
            flatatt(final_attrs),
            conditional_escape(force_unicode(value)))
        toolbar_widget = render_toolbar_widget(final_attrs.get("id", "unknown"))
        js_init_widget = render_js_init_widget(final_attrs.get("id", "unknown"),
                                               EDITOR_CONF)
        return mark_safe(u'<div style="display:inline-block">' +
                         toolbar_widget + 
                         textarea_widget + 
                         u'</div>' +
                         js_init_widget)


def initialize_widget_conf():
    global render_cmd_icon, render_cmd_dialog
    for key in TOOLBAR_CONF.keys():
        if TOOLBAR_CONF[key].get("active", False):
            render_cmd_icon[key] = TOOLBAR_CONF[key].get(
                "render_icon", "wysihtml5.widgets.render_blank")
            if TOOLBAR_CONF[key].get("render_dialog", False):
                render_cmd_dialog[key] = TOOLBAR_CONF[key]["render_dialog"]
        else: render_cmd_icon[key] = "wysihtml5.widgets.render_blank"

initialize_widget_conf()
