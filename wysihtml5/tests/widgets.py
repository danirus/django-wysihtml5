#-*- coding: utf-8 -*-
try:
    from BeautifulSoup import BeautifulSoup, NavigableString
except ImportError:
    from beautifulsoup import BeautifulSoup, NavigableString

from django.forms.models import modelform_factory
from django.test import TestCase as DjangoTestCase
from django.utils.html import conditional_escape

from wysihtml5.tests.models import ModelTest
from wysihtml5.widgets import (Wysihtml5TextareaWidget,
                               render_cmd_icon, render_cmd_dialog)


class Wysihtml5ToolbarTestCase(DjangoTestCase):
    def setUp(self):
        ModelForm = modelform_factory(ModelTest)
        self.soup = BeautifulSoup(unicode(ModelForm()))

    def test_command_disabled_in_settings(self):        
        # check an active command and the disabled one
        cmd_format_block = self.soup.find('span', attrs={
                'data-wysihtml5-command-group': 'formatBlock'})
        cmd_fore_color = self.soup.find('span', attrs={
                'data-wysihtml5-command-group': 'foreColor'})
        self.assert_(cmd_format_block != None)
        self.assert_(cmd_fore_color == None) # tests.settings disabled

    def test_dialog_disabled_in_settings(self):        
        # check the active dialog and the disabled one
        dialog_insert_image = self.soup.find('div', attrs={
                'data-wysihtml5-dialog': 'insertImage'})
        dialog_create_link = self.soup.find('span', attrs={
                'data-wysihtml5-dialog': 'createLink'})
        self.assert_(dialog_insert_image != None)
        self.assert_(dialog_create_link == None) # tests.settings disabled


class Wysihtml5TextareaWidgetTestCase(DjangoTestCase):
    def test_render_wysihtml5admintextarea_widget(self):
        neilmsg = ModelTest.objects.create(
            first_text="One small step for man", 
            second_text="One giant leap for mankind")
        w = Wysihtml5TextareaWidget()
        rendered = conditional_escape(w.render("test", neilmsg.second_text))
        expected = u'\
<div style="display:inline-block"><div id="unknown-toolbar" class="wysihtml5-editor-toolbar">\
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
    <span data-wysihtml5-command="italic" title="Make text italic (CTRL + I)" class="command"></span>\
    <span data-wysihtml5-command="underline" title="Underline text (CTRL + U)" class="command"></span>\
    <span data-wysihtml5-command="justifyLeft" title="Paragraph left justified" class="command"></span>\
    <span data-wysihtml5-command="justifyCenter" title="Paragraph center justified" class="command"></span>\
    <span data-wysihtml5-command="justifyRight" title="Paragraph right justified" class="command"></span>\
    <span data-wysihtml5-command="insertOrderedList" title="Insert an ordered list" class="command"></span>\
    <span data-wysihtml5-command="insertUnorderedList" title="Insert an unordered list" class="command"></span>\
    <span data-wysihtml5-command="insertImage" title="Insert an image" class="command insert-image"></span>\
    <span data-wysihtml5-command="insertHTML" title="Insert a quote" class="command" data-wysihtml5-command-value="<blockquote>quote</blockquote>"></span>\
    <span data-wysihtml5-action="change_view" title="Show HTML" class="action" unselectable="on"></span>\
  </div>\
  <div class="wysihtml5-dialogs">\
    <div data-wysihtml5-dialog="insertImage" style="display:none">  <label>Image:</label>&nbsp;  <input data-wysihtml5-dialog-field="src" value="http://">  <a data-wysihtml5-dialog-action="save" class="button">Ok</a>&nbsp;  <a data-wysihtml5-dialog-action="cancel" class="button">Cancel</a></div>  </div></div><textarea rows="25" cols="40" name="test" class="vLargeTextField">One giant leap for mankind</textarea></div>\
<script>\
new wysihtml5.Editor("unknown",{ name: null, style: true, toolbar: "unknown-toolbar", autoLink: true, parserRules: wysihtml5ParserRules, parser: wysihtml5.dom.parse || Prototype.K, composerClassName: "wysihtml5-editor", bodyClassName: "wysihtml5-supported", useLineBreaks: true, stylesheets: ["/static/wysihtml5/css/stylesheet.css"], placeholderText: null, allowObjectResizing: true, supportTouchDevices: true });\
</script>'
        self.maxDiff = None
        self.assertHTMLEqual(expected, rendered)
