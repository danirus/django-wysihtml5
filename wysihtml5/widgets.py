#-*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.admin.widgets import AdminTextareaWidget
from django.forms.util import flatatt
from django.utils.encoding import force_unicode
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _

from wysihtml5.utils import get_function

# Defaulted to Django 1.4 path
ADMIN_IMAGES_PATH = getattr(settings, "ADMIN_IMAGES_PATH", "%s/admin/img" % settings.STATIC_URL)


def render_create_link_dialog(id):
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


def render_insert_image_dialog(id):
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


create_link_dialog = getattr(
    settings,
    "WYSIHTML5_FUNC_CREATE_LINK_DIALOG",
    "wysihtml5.widgets.render_create_link_dialog")

insert_image_dialog = getattr(
    settings,
    "WYSIHTML5_FUNC_INSERT_IMAGE_DIALOG",
    "wysihtml5.widgets.render_insert_image_dialog")


def render_toolbar_widget(id):
    widget = u'\
<div id="%(id)s-toolbar" class="wysihtml5-editor-toolbar">\
  <div class="commands">\
    <span data-wysihtml5-command-group="formatBlock" title="Format text header" class="heading-selector">\
      <div>\
        <span data-wysihtml5-command="formatBlock" data-wysihtml5-command-value="h1">H1</span>\
        <span data-wysihtml5-command="formatBlock" data-wysihtml5-command-value="h2">H2</span>\
        <span data-wysihtml5-command="formatBlock" data-wysihtml5-command-value="h3">H3</span>\
        <span data-wysihtml5-command="formatBlock" data-wysihtml5-command-value="h4">H4</span>\
        <span data-wysihtml5-command="formatBlock" data-wysihtml5-command-value="h5">H5</span>\
        <span data-wysihtml5-command="formatBlock" data-wysihtml5-command-value="h6">H6</span>\
      </div>\
    </span>\
    <span data-wysihtml5-command="formatBlock" title="Make a paragraph block" data-wysihtml5-command-value="p" class="command format-block-p"></span>\
    <span data-wysihtml5-command="bold" title="Make text bold (CTRL + B)" class="command"></span>\
    <span data-wysihtml5-command="italic" title="Make text bold (CTRL + I)" class="command"></span>\
    <span data-wysihtml5-command="underline" title="Make text bold (CTRL + U)" class="command"></span>\
    <span data-wysihtml5-command="justifyLeft" title="Paragraph left justified" class="command"></span>\
    <span data-wysihtml5-command="justifyCenter" title="Paragraph center justified" class="command"></span>\
    <span data-wysihtml5-command="justifyRight" title="Paragraph right justified" class="command"></span>\
    <span data-wysihtml5-command="insertOrderedList" title="Insert an ordered list" class="command"></span>\
    <span data-wysihtml5-command="insertUnorderedList" title="Insert an unordered list" class="command"></span>\
    <span data-wysihtml5-command="insertImage" title="Insert an image" class="command"></span>\
    <span data-wysihtml5-command="createLink" title="Insert a link" class="command"></span>\
    <span data-wysihtml5-command="insertHTML" title="Insert a quote" class="command" data-wysihtml5-command-value="<blockquote>quote</blockquote>"></span>\
    <span data-wysihtml5-command-group="foreColor" title="Color the selected text" class="fore-color">\
      <div>\
        <span data-wysihtml5-command="foreColor" data-wysihtml5-command-value="silver" unselectable="on"></span>\
        <span data-wysihtml5-command="foreColor" data-wysihtml5-command-value="gray" unselectable="on"></span>\
        <span data-wysihtml5-command="foreColor" data-wysihtml5-command-value="maroon" unselectable="on"></span>\
        <span data-wysihtml5-command="foreColor" data-wysihtml5-command-value="red" unselectable="on"></span>\
        <span data-wysihtml5-command="foreColor" data-wysihtml5-command-value="purple" unselectable="on"></span>\
        <span data-wysihtml5-command="foreColor" data-wysihtml5-command-value="green" unselectable="on"></span>\
        <span data-wysihtml5-command="foreColor" data-wysihtml5-command-value="olive" unselectable="on"></span>\
        <span data-wysihtml5-command="foreColor" data-wysihtml5-command-value="navy" unselectable="on"></span>\
        <span data-wysihtml5-command="foreColor" data-wysihtml5-command-value="blue" unselectable="on"></span>\
      </div>\
    </span>\
    <span data-wysihtml5-action="change_view" title="Show HTML" class="action" unselectable="on"></span>\
  </div>\
  <div class="wysihtml5-dialogs">\
    %(createLinkDialog)s %(insertImageDialog)s\
  </div>\
</div>' % { "id": id, 
            "createLinkDialog": get_function(create_link_dialog)(id), 
            "insertImageDialog": get_function(insert_image_dialog)(id) }
    return widget

def render_js_init_widget(id):
    widget = u'<script>var editor = new wysihtml5.Editor("%(id)s",{toolbar:"%(id)s-toolbar", parserRules: wysihtml5ParserRules, placeholderText: "%(placeholder)s", stylesheets: "%(cssfile)s"});</script>' % {"id": id, "placeholder": _("Use the toolbar below to edit the content here"), "cssfile": settings.STATIC_URL + "wysihtml5/css/stylesheet.css"}
    return widget

class Wysihtml5AdminTextareaWidget(AdminTextareaWidget):

    class Media:
        css = {
            'all': (settings.STATIC_URL + "admin/wysihtml5/css/toolbar.css",)
        }
        js = (settings.STATIC_URL + "admin/wysihtml5/js/advanced.js",
              settings.STATIC_URL + "admin/wysihtml5/js/wysihtml5-0.3.0.min.js")

    def __init__(self, attrs=None):
        if not attrs:
            attrs = {"rows": 15}
        elif not attrs.get("rows", False):
            attrs.update({"rows": 15})
        super(Wysihtml5AdminTextareaWidget, self).__init__(attrs=attrs)

    def render(self, name, value, attrs=None):
        if value is None: value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        textarea_widget = u'<textarea%s>%s</textarea>' % (
            flatatt(final_attrs),
            conditional_escape(force_unicode(value)))
        toolbar_widget = render_toolbar_widget(final_attrs.get("id", "unknown"))
        js_init_widget = render_js_init_widget(final_attrs.get("id", "unknown"))
        return mark_safe(u'<div style="display:inline-block">' +
                         toolbar_widget + 
                         textarea_widget + 
                         u'</div>' +
                         js_init_widget)
