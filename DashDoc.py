import sublime, sublime_plugin, webbrowser

class DashDocCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		selection = self.view.sel()[0]
		if len(selection) == 0:
			selection = self.view.word(selection)
		word = self.view.substr(selection)

		webbrowser.open_new_tab("dash://%s" % (word,))
