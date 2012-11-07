#-*- coding: utf-8 -*-

from django.conf import settings
from django.test import TestCase as DjangoTestCase
from django.utils.html import conditional_escape

from wysihtml5.widgets import Wysihtml5AdminTextareaWidget
from wysihtml5.tests.models import ModelTest


class Wysihtml5AdminTextareaWidgetTestCase(DjangoTestCase):

    def test_render_wysihtml5admintextarea_widget(self):
        neilmsg = ModelTest.objects.create(
            first_text="One small step for man", 
            second_text="One giant leap for mankind")
        w = Wysihtml5AdminTextareaWidget()
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
    <div data-wysihtml5-dialog="createLink" style="display:none">  <label>Link:</label>&nbsp;  <input data-wysihtml5-dialog-field="href" value="http://">  <a data-wysihtml5-dialog-action="save" class="button">Ok</a>&nbsp;  <a data-wysihtml5-dialog-action="cancel" class="button">Cancel</a></div> <div data-wysihtml5-dialog="insertImage" style="display:none">  <label>Image:</label>&nbsp;  <input data-wysihtml5-dialog-field="src" value="http://">  <a data-wysihtml5-dialog-action="save" class="button">Ok</a>&nbsp;  <a data-wysihtml5-dialog-action="cancel" class="button">Cancel</a></div>  </div></div><textarea rows="15" cols="40" name="test" class="vLargeTextField">One giant leap for mankind</textarea></div><script>var editor = new wysihtml5.Editor("unknown",{toolbar:"unknown-toolbar", parserRules: wysihtml5ParserRules, placeholderText: "Use the toolbar below to edit the content here", stylesheets: "/static/wysihtml5/css/stylesheet.css"});</script>'
        self.assertTrue(expected == rendered)
