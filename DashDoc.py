import sublime, sublime_plugin

import os
import subprocess
import platform

try:
    from urllib import quote         # Python 2
except ImportError:
    from urllib.parse import quote   # Python 3


def syntax_name(view):
    syntax = os.path.basename(view.settings().get('syntax'))
    syntax = os.path.splitext(syntax)[0]
    return syntax


def docset_keys(view, syntax_docset_map):
    syntax = syntax_name(view)

    try:
        return syntax_docset_map[syntax]
    except KeyError:
        return []


def open_dash(query, keys, run_in_background):
    # background
    background_string = '&prevent_activation=true' if run_in_background else ''

    if platform.system() == 'Windows':
        # sending keys=<nothing> confuses some Windows doc viewers
        if keys:
            # ampersand must be escaped and ^ is the Windows shell escape char
            url = 'dash-plugin://keys=%s^&query=%s%s' % (','.join(keys), quote(query), background_string)
        else:
            url = 'dash-plugin://query=%s%s' % (quote(query), background_string)
        subprocess.call(['start', url], shell=True)
    elif platform.system() == 'Linux':
        if keys:
            subprocess.call([
                '/usr/bin/xdg-open',
                'dash-plugin:keys=%s&query=%s%s' % (','.join(keys), quote(query), background_string)
            ])
        else:
            subprocess.call([
                '/usr/bin/xdg-open',
                'dash-plugin:query=%s%s' % (quote(query), background_string)
            ])
    else:
        if keys:
            subprocess.call([
                '/usr/bin/open', '-g',
                'dash-plugin://keys=%s&query=%s%s' % (','.join(keys), quote(query), background_string)
            ])
        else:
            subprocess.call([
                '/usr/bin/open', '-g',
                'dash-plugin://query=%s%s' % (quote(query), background_string)
            ])


class DashDocCommand(sublime_plugin.TextCommand):
    def run(self, edit, flip_syntax_sensitive=False, run_in_background=False):
        # read global and (project-specific) local settings
        global_settings = sublime.load_settings('DashDoc.sublime-settings')
        settings  = self.view.settings()

        # syntax sensitivity is the default
        syntax_sensitive_as_default = \
            settings.get('syntax_sensitive_as_default',
                         global_settings.get('syntax_sensitive_as_default', True));

        # assemble docset mapping from global settings and project-specific
        # local settings (which take precedence)
        syntax_docset_map = dict(list(global_settings.get('syntax_docset_map', {}).items()) +
                                 list(       settings.get('syntax_docset_map', {}).items()))

        # query
        selection = self.view.sel()[0]
        if len(selection) == 0:
            selection = self.view.word(selection)
        query = self.view.substr(selection)

        # keys
        syntax_sensitive = flip_syntax_sensitive ^ syntax_sensitive_as_default
        keys = docset_keys(self.view, syntax_docset_map) if syntax_sensitive else []

        open_dash(query, keys, run_in_background)


class DashDocSearchCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_input_panel('Topic?', '', self.on_done, self.on_change, self.on_cancel)

    def on_change(self, name):
        pass

    def on_cancel(self, name):
        pass

    def on_done(self, topic):
        open_dash(topic, [], False)
