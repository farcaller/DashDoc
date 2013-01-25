import sublime
import sublime_plugin
import os
import subprocess


def syntax_name(view):
    syntax = os.path.basename(view.settings().get('syntax'))
    syntax = os.path.splitext(syntax)[0]
    return syntax


def docset_prefix(view, settings):
    syntax_docset_map = settings.get('syntax_docset_map', {})
    syntax = syntax_name(view)

    if syntax in syntax_docset_map:
        return syntax_docset_map[syntax] + ':'

    return None


class DashDocCommand(sublime_plugin.TextCommand):
    def run(self, edit, syntax_sensitive=False):
        selection = self.view.sel()[0]
        if len(selection) == 0:
            selection = self.view.word(selection)
        word = self.view.substr(selection)

        settings = sublime.load_settings('DashDoc.sublime-settings')
        if syntax_sensitive or settings.get('syntax_sensitive', False):
            docset = docset_prefix(self.view, settings)
        else:
            docset = None

        subprocess.call(["open", "dash://%s%s" % (docset or '', word)])
