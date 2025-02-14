# coding=utf8
import sublime_plugin
import os
import re

from SideBarSelection import SideBarSelection
from SideBarGit import SideBarGit
from Utils import Object

#run last command again on a focused tab when pressing F5

class SideBarGitRefreshTabContentsByRunningCommandAgain(sublime_plugin.TextCommand):
	def run(self, edit):
		if self.view.settings().has('SideBarGitIsASideBarGitTab'):
			SideBarGit().run(
												[],
												self.view.settings().get('SideBarGitModal'),
												self.view.settings().get('SideBarGitBackground'),
												self.view,
												self.view.settings().get('SideBarGitCommand'),
												self.view.settings().get('SideBarGitItem'),
												self.view.settings().get('SideBarGitToStatusBar'),
												self.view.settings().get('SideBarGitTitle'),
												self.view.settings().get('SideBarGitNoResults'),
												self.view.settings().get('SideBarGitSyntaxFile')
												)

#Following code for selected files or folders

class SideBarGitDiffAllChangesSinceLastCommitCommand(sublime_plugin.WindowCommand):
	def run(self, paths = []):
		for item in SideBarSelection(paths).getSelectedItems():
			object = Object()
			object.item = item
			object.command = ['git', 'diff', 'HEAD', '--no-color', '--', item.forCwdSystemName()]
			object.title = 'Diff: '+item.name()+'.diff'
			object.no_results = 'No differences to show'
			object.syntax_file = 'Packages/Diff/Diff.tmLanguage'
			object.word_wrap = False
			SideBarGit().run(object)
	def is_enabled(self, paths = []):
		return SideBarSelection(paths).len() > 0

class SideBarGitDiffChangesNotStagedCommand(sublime_plugin.WindowCommand):
	def run(self, paths = []):
		for item in SideBarSelection(paths).getSelectedItems():
			object = Object()
			object.item = item
			object.command = ['git', 'diff', '--no-color', '--', item.forCwdSystemName()]
			object.title = 'Diff: '+item.name()+'.diff'
			object.no_results = 'No differences to show'
			object.syntax_file = 'Packages/Diff/Diff.tmLanguage'
			object.word_wrap = False
			SideBarGit().run(object)
	def is_enabled(self, paths = []):
		return SideBarSelection(paths).len() > 0

class SideBarGitDiffChangesStagedNotCommitedCommand(sublime_plugin.WindowCommand):
	def run(self, paths = []):
		for item in SideBarSelection(paths).getSelectedItems():
			object = Object()
			object.item = item
			object.command = ['git', 'diff', '--no-color', '--staged', '--', item.forCwdSystemName()]
			object.title = 'Diff: '+item.name()+'.diff'
			object.no_results = 'No differences to show'
			object.syntax_file = 'Packages/Diff/Diff.tmLanguage'
			object.word_wrap = False
			SideBarGit().run(object)
	def is_enabled(self, paths = []):
		return SideBarSelection(paths).len() > 0

class SideBarGitDiffBetweenIndexAndLastCommitCommand(sublime_plugin.WindowCommand):
	def run(self, paths = []):
		for item in SideBarSelection(paths).getSelectedItems():
			object = Object()
			object.item = item
			object.command = ['git', 'diff', '--no-color', '--cached', '--', item.forCwdSystemName()]
			object.title = 'Diff: '+item.name()+'.diff'
			object.no_results = 'No differences to show'
			object.syntax_file = 'Packages/Diff/Diff.tmLanguage'
			object.word_wrap = False
			SideBarGit().run(object)
	def is_enabled(self, paths = []):
		return SideBarSelection(paths).len() > 0

class SideBarGitDiffBetweenRemoteAndLastLocalCommitCommand(sublime_plugin.WindowCommand):
	def run(self, paths = []):
		for item in SideBarSelection(paths).getSelectedItems():
			object = Object()
			object.item = item
			object.command = ['git', 'diff', '--no-color', 'origin/master..', '--', item.forCwdSystemName()]
			object.title = 'Diff: '+item.name()+'.diff'
			object.no_results = 'No differences to show'
			object.syntax_file = 'Packages/Diff/Diff.tmLanguage'
			object.word_wrap = False
			SideBarGit().run(object)
	def is_enabled(self, paths = []):
		return SideBarSelection(paths).len() > 0

class SideBarGitDiffBetweenLastLocalCommitAndRemoteCommand(sublime_plugin.WindowCommand):
	def run(self, paths = []):
		for item in SideBarSelection(paths).getSelectedItems():
			object = Object()
			object.item = item
			object.command = ['git', 'diff', '--no-color', '..origin/master', '--', item.forCwdSystemName()]
			object.title = 'Diff: '+item.name()+'.diff'
			object.no_results = 'No differences to show'
			object.syntax_file = 'Packages/Diff/Diff.tmLanguage'
			object.word_wrap = False
			SideBarGit().run(object)
	def is_enabled(self, paths = []):
		return SideBarSelection(paths).len() > 0

class SideBarGitLogStatShortLatestCommand(sublime_plugin.WindowCommand):
	def run(self, paths = []):
		for item in SideBarSelection(paths).getSelectedItems():
			object = Object()
			object.item = item
			object.command = ['git', 'log', '-n', '30', '--pretty=short', '--decorate', '--graph', '--no-color', '--', item.forCwdSystemName()]
			object.title = 'Log: '+item.name()
			object.no_results = 'No log to show'
			object.syntax_file = 'Packages/Git/Git Graph.tmLanguage'
			SideBarGit().run(object)
	def is_enabled(self, paths = []):
		return SideBarSelection(paths).len() > 0

class SideBarGitLogStatShortFullCommand(sublime_plugin.WindowCommand):
	def run(self, paths = []):
		for item in SideBarSelection(paths).getSelectedItems():
			object = Object()
			object.item = item
			object.command = ['git', 'log', '--pretty=short', '--decorate', '--graph', '--no-color', '--', item.forCwdSystemName()]
			object.title = 'Log: '+item.name()
			object.no_results = 'No log to show'
			object.syntax_file = 'Packages/Git/Git Graph.tmLanguage'
			SideBarGit().run(object)
	def is_enabled(self, paths = []):
		return SideBarSelection(paths).len() > 0

class SideBarGitLogStatLatestCommand(sublime_plugin.WindowCommand):
	def run(self, paths = []):
		for item in SideBarSelection(paths).getSelectedItems():
			object = Object()
			object.item = item
			object.command = ['git', 'log', '-n', '30', '--stat', '--graph', '--decorate', '--no-color', '--', item.forCwdSystemName()]
			object.title = 'Log: '+item.name()
			object.no_results = 'No log to show'
			object.syntax_file = 'Packages/Git/Git Graph.tmLanguage'
			SideBarGit().run(object)
	def is_enabled(self, paths = []):
		return SideBarSelection(paths).len() > 0

class SideBarGitLogStatFullCommand(sublime_plugin.WindowCommand):
	def run(self, paths = []):
		for item in SideBarSelection(paths).getSelectedItems():
			object = Object()
			object.item = item
			object.command = ['git', 'log', '--stat', '--graph', '--decorate', '--no-color', '--', item.forCwdSystemName()]
			object.title = 'Log: '+item.name()
			object.no_results = 'No log to show'
			object.syntax_file = 'Packages/Git/Git Graph.tmLanguage'
			SideBarGit().run(object)
	def is_enabled(self, paths = []):
		return SideBarSelection(paths).len() > 0

class SideBarGitLogStatListLatestCommand(sublime_plugin.WindowCommand):
	def run(self, paths = []):
		import sys
		for item in SideBarSelection(paths).getSelectedItems():
			object = Object()
			object.item = item
			object.command = ['git', 'log', '-n', '50', '--pretty=format:%s'.encode(sys.getfilesystemencoding()),  '--no-color', '--', item.forCwdSystemName()]
			object.title = 'Log: '+item.name()
			object.no_results = 'No log to show'
			object.syntax_file = 'Packages/Git/Git Graph.tmLanguage'
			SideBarGit().run(object)
	def is_enabled(self, paths = []):
		return SideBarSelection(paths).len() > 0

class SideBarGitLogStatListCommitLatestCommand(sublime_plugin.WindowCommand):
	def run(self, paths = []):
		import sys
		for item in SideBarSelection(paths).getSelectedItems():
			object = Object()
			object.item = item
			object.command = ['git', 'log', '-n', '50', '--pretty=format:%h %s'.encode(sys.getfilesystemencoding()), '--no-color', '--', item.forCwdSystemName()]
			object.title = 'Log: '+item.name()
			object.no_results = 'No log to show'
			object.syntax_file = 'Packages/Git/Git Graph.tmLanguage'
			SideBarGit().run(object)
	def is_enabled(self, paths = []):
		return SideBarSelection(paths).len() > 0

class SideBarGitLogExtendedLatestCommand(sublime_plugin.WindowCommand):
	def run(self, paths = []):
		for item in SideBarSelection(paths).getSelectedItems():
			object = Object()
			object.item = item
			object.command = ['git', 'log', '-n', '30', '-p', '--decorate', '--no-color', '--', item.forCwdSystemName()]
			object.title = 'Log: '+item.name()
			object.no_results = 'No log to show'
			object.syntax_file = 'Packages/Diff/Diff.tmLanguage'
			object.word_wrap = False
			SideBarGit().run(object)
	def is_enabled(self, paths = []):
		return SideBarSelection(paths).len() > 0

class SideBarGitLogExtendedFullCommand(sublime_plugin.WindowCommand):
	def run(self, paths = []):
		for item in SideBarSelection(paths).getSelectedItems():
			object = Object()
			object.item = item
			object.command = ['git', 'log', '-p', '--decorate', '--no-color', '--', item.forCwdSystemName()]
			object.title = 'Log: '+item.name()
			object.no_results = 'No log to show'
			object.syntax_file = 'Packages/Diff/Diff.tmLanguage'
			object.word_wrap = False
			SideBarGit().run(object)
	def is_enabled(self, paths = []):
		return SideBarSelection(paths).len() > 0

class SideBarGitLogSinceLatestPushCommand(sublime_plugin.WindowCommand):
	def run(self, paths = []):
		for item in SideBarSelection(paths).getSelectedItems():
			object = Object()
			object.item = item
			object.command = ['git', 'log', 'origin/master..', '--stat', '--graph', '--decorate', '--no-color', '--', item.forCwdSystemName()]
			object.title = 'Log: '+item.name()
			object.no_results = 'No log to show'
			object.syntax_file = 'Packages/Git/Git Graph.tmLanguage'
			object.word_wrap = False
			SideBarGit().run(object)
	def is_enabled(self, paths = []):
		return SideBarSelection(paths).len() > 0

class SideBarGitReflogCommand(sublime_plugin.WindowCommand):
	def run(self, paths = []):
		for item in SideBarSelection(paths).getSelectedItems():
			object = Object()
			object.item = item
			object.command = ['git', 'reflog', '--no-color', '--', item.forCwdSystemName()]
			object.title = 'Reflog: '+item.name()
			object.syntax_file = 'Packages/Git/Git Graph.tmLanguage'
			SideBarGit().run(object)
	def is_enabled(self, paths = []):
		return SideBarSelection(paths).len() > 0

class SideBarGitBlameCommand(sublime_plugin.WindowCommand):
	def run(self, paths = []):
		for item in SideBarSelection(paths).getSelectedItems():
			object = Object()
			object.item = item
			object.command = ['/usr/local/bin/git', 'blame', '--no-color', '--', item.forCwdSystemName()]
			object.title = 'Blame: '+item.name()
			object.syntax_file = 'Packages/Git/Git Blame.tmLanguage'
			object.word_wrap = False
			SideBarGit().run(object)
	def is_enabled(self, paths = []):
		return SideBarSelection(paths).hasFiles()

class SideBarGitStatusCommand(sublime_plugin.WindowCommand):
	def run(self, paths = []):
		for item in SideBarSelection(paths).getSelectedItems():
			object = Object()
			object.item = item
			object.command = ['git', 'status', '--untracked-files=all', '--ignored', '--', item.forCwdSystemName()]
			object.title = 'Status: '+item.name()
			object.syntax_file = 'Packages/Git/Git Graph.tmLanguage'
			SideBarGit().run(object)
	def is_enabled(self, paths = []):
		return SideBarSelection(paths).len() > 0

class SideBarGitRevertTrackedCommand(sublime_plugin.WindowCommand):
	def run(self, paths = [], confirm = False, drop_me = ''):
		failed = False
		if confirm == False:
			SideBarGit().confirm('Discard changes to tracked on selected items? ', self.run, paths)
		else:
			for item in SideBarSelection(paths).getSelectedItems():
				object = Object()
				object.item = item
				object.command = ['git', 'checkout', 'HEAD', '--', item.forCwdSystemName()]
				if not SideBarGit().run(object):
					failed = True
			if not failed:
				SideBarGit().status('Discarded changes to tracked on selected items')
	def is_enabled(self, paths = []):
		return SideBarSelection(paths).len() > 0

class SideBarGitRevertTrackedCleanUntrackedCommand(sublime_plugin.WindowCommand):
	def run(self, paths = [], confirm = False, drop_me = ''):
		failed = False
		if confirm == False:
			SideBarGit().confirm('Discard changes to tracked and clean untracked on selected items? ', self.run, paths)
		else:
			for item in SideBarSelection(paths).getSelectedItems():
				object = Object()
				object.item = item
				object.command = ['git', 'checkout', 'HEAD', '--', item.forCwdSystemName()]
				if not SideBarGit().run(object):
					failed = True
				object = Object()
				object.item = item
				object.command = ['git', 'clean', '-f', '-d', '--', item.forCwdSystemName()]
				if not SideBarGit().run(object):
					failed = True
			if not failed:
				SideBarGit().status('Discarded changes to tracked and cleaned untracked on selected items')

	def is_enabled(self, paths = []):
		return SideBarSelection(paths).len() > 0

class SideBarGitRevertTrackedCleanUntrackedUnstageCommand(sublime_plugin.WindowCommand):
	def run(self, paths = [], confirm = False, drop_me = ''):
		failed = False
		if confirm == False:
			SideBarGit().confirm('Discard changes to tracked, clean untracked and unstage on selected items? ', self.run, paths)
		else:
			for item in SideBarSelection(paths).getSelectedItems():
				object = Object()
				object.item = item
				object.command = ['git', 'checkout', 'HEAD', '--', item.forCwdSystemName()]
				if not SideBarGit().run(object):
					failed = True
				object = Object()
				object.item = item
				object.command = ['git', 'clean', '-f', '-d', '--', item.forCwdSystemName()]
				if not SideBarGit().run(object):
					failed = True
				object = Object()
				object.item = item
				object.command = ['git', 'reset', 'HEAD', '--', item.forCwdSystemName()]
				if not SideBarGit().run(object):
					failed = True
			if not failed:
				SideBarGit().status('Discarded changes to tracked, cleaned untracked and unstage on selected items')

	def is_enabled(self, paths = []):
		return SideBarSelection(paths).len() > 0

class SideBarGitRevertTrackedUnstageCleanUntrackedCommand(sublime_plugin.WindowCommand):
	def run(self, paths = [], confirm = False, drop_me = ''):
		failed = False
		if confirm == False:
			SideBarGit().confirm('Discard changes to tracked, unstage and clean untracked on selected items? ', self.run, paths)
		else:
			for item in SideBarSelection(paths).getSelectedItems():
				object = Object()
				object.item = item
				object.command = ['git', 'checkout', 'HEAD', '--', item.forCwdSystemName()]
				if not SideBarGit().run(object):
					failed = True
				object = Object()
				object.item = item
				object.command = ['git', 'reset', 'HEAD', '--', item.forCwdSystemName()]
				if not SideBarGit().run(object):
					failed = True
				object = Object()
				object.item = item
				object.command = ['git', 'clean', '-f', '-d', '--', item.forCwdSystemName()]
				if not SideBarGit().run(object):
					failed = True
			if not failed:
				SideBarGit().status('Discarded changes to tracked, unstage and cleaned untracked on selected items')

	def is_enabled(self, paths = []):
		return SideBarSelection(paths).len() > 0

class SideBarGitRevertUnstageCommand(sublime_plugin.WindowCommand):
	def run(self, paths = [], confirm = False, drop_me = ''):
		failed = False
		if confirm == False:
			SideBarGit().confirm('Unstage selected items? ', self.run, paths)
		else:
			for item in SideBarSelection(paths).getSelectedItems():
				object = Object()
				object.item = item
				object.command = ['git', 'reset', 'HEAD', '--', item.forCwdSystemName()]
				if not SideBarGit().run(object):
					failed = True
			if not failed:
				SideBarGit().status('Unstage selected items')

	def is_enabled(self, paths = []):
		return SideBarSelection(paths).len() > 0

class SideBarGitCheckoutToCommand(sublime_plugin.WindowCommand):
	def run(self, paths = [], input = False, content = ''):
		failed = False
		if input == False:
			SideBarGit().prompt('Checkout selected items to object: ', '', self.run, paths)
		elif content != '':
			import sys
			for item in SideBarSelection(paths).getSelectedItems():
				object = Object()
				object.item = item
				object.command = ['git', 'checkout', content.encode(sys.getfilesystemencoding()), '--', item.forCwdSystemName()]
				if not SideBarGit().run(object):
					failed = True
			if not failed:
				SideBarGit().status('Checkout selected items to "'+content+'"')

	def is_enabled(self, paths = []):
		return SideBarSelection(paths).len() > 0

class SideBarGitIgnoreOpenCommand(sublime_plugin.WindowCommand):
	def run(self, paths = []):
		for item in SideBarSelection(paths).getSelectedItems():
			item.path(item.dirname())
			while not os.path.exists(item.join('.git')):
				if os.path.exists(item.join('.gitignore')):
					break;
				if item.dirname() == item.path():
					break;
				item.path(item.dirname())

			if os.path.exists(item.join('.gitignore')):
				item.path(item.join('.gitignore'))
			else:
				item.path(item.join('.gitignore'))
				item.create()
			item.edit()

	def is_enabled(self, paths = []):
		return SideBarSelection(paths).len() > 0

class SideBarGitIgnoreAddCommand(sublime_plugin.WindowCommand):
	def run(self, paths = []):
		for item in SideBarSelection(paths).getSelectedItems():
			original = item.path()
			originalIsDirectory = item.isDirectory()
			item.path(item.dirname())
			while not os.path.exists(item.join('.git')):
				if os.path.exists(item.join('.gitignore')):
					break;
				if item.dirname() == item.path():
					break;
				item.path(item.dirname())

			if os.path.exists(item.join('.gitignore')):
				item.path(item.join('.gitignore'))
			else:
				if os.path.exists(item.join('.git')):
					item.path(item.join('.gitignore'))
					item.create()
				else:
					SideBarGit().status('Unable to found repository for "'+original.encode('utf-8')+'"')
					continue
			ignore_entry = re.sub('^/+', '', original.replace(item.dirname(), '').replace('\\', '/'))
			if originalIsDirectory:
				ignore_entry += '/*'
			item.write(item.contentUTF8().strip()+'\n'+ignore_entry)
			SideBarGit().status('Ignored file "'+ignore_entry+'" on '+item.path())

	def is_enabled(self, paths = []):
		return SideBarSelection(paths).len() > 0

# Following code for selected folders. Dirname for when a file is selected.

class SideBarGitInitCommand(sublime_plugin.WindowCommand):
	def run(self, paths = []):
		for item in SideBarSelection(paths).getSelectedDirectoriesOrDirnames():
			object = Object()
			object.item = item
			object.command = ['git', 'init']
			object.to_status_bar = True
			SideBarGit().run(object)

	def is_enabled(self, paths = []):
		return SideBarSelection(paths).len() > 0

class SideBarGitCloneCommand(sublime_plugin.WindowCommand):
	def run(self, paths = [], input = False, content = ''):
		failed = False
		if input == False:
			SideBarGit().prompt('Enter URL to clone: ', '', self.run, paths)
		elif content != '':
			import sys
			for item in SideBarSelection(paths).getSelectedDirectoriesOrDirnames():
				object = Object()
				object.item = item
				object.command = ['git', 'clone', '--recursive', content.encode(sys.getfilesystemencoding())]
				object.to_status_bar = True
				if not SideBarGit().run(object, True):
					failed = True
			if not failed:
				SideBarGit().status('Cloned URL "'+content+'"')

	def is_enabled(self, paths = []):
		return SideBarSelection(paths).len() > 0

class SideBarGitGuiCommand(sublime_plugin.WindowCommand):
	def run(self, paths = []):
		for item in SideBarSelection(paths).getSelectedDirectoriesOrDirnames():
			object = Object()
			object.item = item
			object.command = ['git','gui']
			SideBarGit().run(object, False, True)

	def is_enabled(self, paths = []):
		return SideBarSelection(paths).len() > 0

class SideBarGitGitkCommand(sublime_plugin.WindowCommand):
	def run(self, paths = [], input = False):
		for item in SideBarSelection(paths).getSelectedDirectoriesOrDirnames():
			object = Object()
			object.item = item
			object.command = ['gitk']
			SideBarGit().run(object, False, True)

	def is_enabled(self, paths = []):
		return SideBarSelection(paths).len() > 0

# Following code for unique selected repos found on items selected

class SideBarGitCheckoutRepositoryToCommand(sublime_plugin.WindowCommand):
	def run(self, paths = [], input = False, content = ''):
		failed = False
		if input == False:
			SideBarGit().prompt('Checkout repository to object: ', '', self.run, paths)
		elif content != '':
			import sys
			for item in SideBarGit().getSelectedRepos(SideBarSelection(paths).getSelectedItems()):
				object = Object()
				object.item = item.repository
				object.command = ['git', 'checkout', content.encode(sys.getfilesystemencoding())]
				if not SideBarGit().run(object):
					failed = True
			if not failed:
				SideBarGit().status('Checkout repository to "'+content+'"')

	def is_enabled(self, paths = []):
		return SideBarSelection(paths).len() > 0

class SideBarGitPushCommand(sublime_plugin.WindowCommand):
	def run(self, paths = []):
		for item in SideBarGit().getSelectedRepos(SideBarSelection(paths).getSelectedItems()):
			object = Object()
			object.item = item.repository
			object.command = ['git','push']
			object.to_status_bar = True
			SideBarGit().run(object, True)

	def is_enabled(self, paths = []):
		return SideBarSelection(paths).len() > 0

class SideBarGitPushWithOptionsCommand(sublime_plugin.WindowCommand):
	def run(self, paths = [], input = False, content = ''):
		if input == False:
			SideBarGit().prompt('Push with options: ', "git push aRemoteName aLocalBranch:aRemoteBranch", self.run, paths)
		elif content != '':
			import sys
			for item in SideBarGit().getSelectedRepos(SideBarSelection(paths).getSelectedItems()):
				object = Object()
				object.item = item.repository
				object.command = content.encode(sys.getfilesystemencoding()).split(' ')
				object.to_status_bar = True
				SideBarGit().run(object, True)

	def is_enabled(self, paths = []):
		return SideBarSelection(paths).len() > 0

class SideBarGitPushAndPushTagsCommand(sublime_plugin.WindowCommand):
	def run(self, paths = []):
		for item in SideBarGit().getSelectedRepos(SideBarSelection(paths).getSelectedItems()):
			object = Object()
			object.item = item.repository
			object.command = ['git','push','&&','git','push','--tags']
			object.to_status_bar = True
			SideBarGit().run(object, True)

	def is_enabled(self, paths = []):
		return SideBarSelection(paths).len() > 0

class SideBarGitPushTagsCommand(sublime_plugin.WindowCommand):
	def run(self, paths = []):
		for item in SideBarGit().getSelectedRepos(SideBarSelection(paths).getSelectedItems()):
			object = Object()
			object.item = item.repository
			object.command = ['git','push','--tags']
			object.to_status_bar = True
			SideBarGit().run(object, True)

	def is_enabled(self, paths = []):
		return SideBarSelection(paths).len() > 0

class SideBarGitPullCommand(sublime_plugin.WindowCommand):
	def run(self, paths = [], confirm = False, drop_me = ''):
		if confirm == False:
			SideBarGit().confirm('Pull from default? ', self.run, paths)
		else:
			for item in SideBarGit().getSelectedRepos(SideBarSelection(paths).getSelectedItems()):
				object = Object()
				object.item = item.repository
				object.command = ['git','pull']
				SideBarGit().run(object, True)

	def is_enabled(self, paths = []):
		return SideBarSelection(paths).len() > 0

class SideBarGitPullWithOptionsCommand(sublime_plugin.WindowCommand):
	def run(self, paths = [], input = False, content = ''):
		if input == False:
			SideBarGit().prompt('Pull with options: ', "git pull", self.run, paths)
		elif content != '':
			import sys
			for item in SideBarGit().getSelectedRepos(SideBarSelection(paths).getSelectedItems()):
				object = Object()
				object.item = item.repository
				object.command = content.encode(sys.getfilesystemencoding()).split(' ')
				SideBarGit().run(object, True)

	def is_enabled(self, paths = []):
		return SideBarSelection(paths).len() > 0

class SideBarGitFetchCommand(sublime_plugin.WindowCommand):
	def run(self, paths = [], confirm = False, drop_me = ''):
		if confirm == False:
			SideBarGit().confirm('Fetch from default? ', self.run, paths)
		else:
			for item in SideBarGit().getSelectedRepos(SideBarSelection(paths).getSelectedItems()):
				object = Object()
				object.item = item.repository
				object.command = ['git','fetch']
				SideBarGit().run(object, True)

	def is_enabled(self, paths = []):
		return SideBarSelection(paths).len() > 0

class SideBarGitFetchWithOptionsCommand(sublime_plugin.WindowCommand):
	def run(self, paths = [], input = False, content = ''):
		if input == False:
			SideBarGit().prompt('Fetch with options: ', "git fetch aRemoteName aRemoteBranch:aLocalBranch", self.run, paths)
		elif content != '':
			import sys
			for item in SideBarGit().getSelectedRepos(SideBarSelection(paths).getSelectedItems()):
				object = Object()
				object.item = item.repository
				object.command = content.encode(sys.getfilesystemencoding()).split(' ')
				SideBarGit().run(object, True)

	def is_enabled(self, paths = []):
		return SideBarSelection(paths).len() > 0

class SideBarGitCommitUndoCommand(sublime_plugin.WindowCommand):
	def run(self, paths = [], confirm = False, drop_me = ''):
		if confirm == False:
			SideBarGit().confirm('Undo Commit? ', self.run, paths)
		else:
			for item in SideBarGit().getSelectedRepos(SideBarSelection(paths).getSelectedItems()):
				object = Object()
				object.item = item.repository
				object.command = ['git', 'reset', '--soft', 'HEAD^']
				SideBarGit().run(object)

	def is_enabled(self, paths = []):
		return SideBarSelection(paths).len() > 0

# Following code for files and folders for each unique selected repos

class SideBarGitCommitCommand(sublime_plugin.WindowCommand):
	def run(self, paths = [], input = False, content = ''):
		if input == False:
			SideBarGit().prompt('Enter a commit message: ', '', self.run, paths)
		elif content != '':
			import sys
			content = (content[0].upper() + content[1:]).encode(sys.getfilesystemencoding())
			for repo in SideBarGit().getSelectedRepos(SideBarSelection(paths).getSelectedItems()):
				commitCommand = ['git', 'commit', '-m', content, '--']
				for item in repo.items:
					commitCommand.append(item.forCwdSystemPathRelativeFrom(repo.repository.path()))
				object = Object()
				object.item = repo.repository
				object.to_status_bar = True
				object.command = commitCommand
				SideBarGit().run(object)

	def is_enabled(self, paths = []):
		return SideBarSelection(paths).len() > 0

class SideBarGitCommitAllCommand(sublime_plugin.WindowCommand):
	def run(self, paths = [], input = False, content = ''):
		if input == False:
			SideBarGit().prompt('Enter a commit message: ', '', self.run, paths)
		elif content != '':
			import sys
			content = (content[0].upper() + content[1:]).encode(sys.getfilesystemencoding())
			for item in SideBarGit().getSelectedRepos(SideBarSelection(paths).getSelectedItems()):
				object = Object()
				object.item = item.repository
				object.to_status_bar = True
				object.command = ['git', 'commit', '-a', '-m', content]
				SideBarGit().run(object)

	def is_enabled(self, paths = []):
		return SideBarSelection(paths).len() > 0

class SideBarGitCommitAmendCommand(sublime_plugin.WindowCommand):
	def run(self, paths = []):
		for repo in SideBarGit().getSelectedRepos(SideBarSelection(paths).getSelectedItems()):
			commitCommand = ['git', 'commit', '--amend', '-C', 'HEAD', '--']
			for item in repo.items:
				commitCommand.append(item.forCwdSystemPathRelativeFrom(repo.repository.path()))
			object = Object()
			object.item = repo.repository
			object.to_status_bar = True
			object.command = commitCommand
			SideBarGit().run(object)

	def is_enabled(self, paths = []):
		return SideBarSelection(paths).len() > 0

class SideBarGitAddCommitCommand(sublime_plugin.WindowCommand):
	def run(self, paths = [], input = False, content = ''):
		if input == False:
			SideBarGit().prompt('Enter a commit message: ', '', self.run, paths)
		elif content != '':
			import sys
			content = (content[0].upper() + content[1:]).encode(sys.getfilesystemencoding())
			for repo in SideBarGit().getSelectedRepos(SideBarSelection(paths).getSelectedItems()):
				commitCommandAdd = ['git', 'add', '--']
				commitCommandCommit = ['git', 'commit', '-m', content, '--']
				for item in repo.items:
					commitCommandAdd.append(item.forCwdSystemPathRelativeFromRecursive(repo.repository.path()))
					commitCommandCommit.append(item.forCwdSystemPathRelativeFrom(repo.repository.path()))
				object = Object()
				object.item = repo.repository
				object.command = commitCommandAdd
				SideBarGit().run(object)
				object = Object()
				object.item = repo.repository
				object.to_status_bar = True
				object.command = commitCommandCommit
				SideBarGit().run(object)

	def is_enabled(self, paths = []):
		return SideBarSelection(paths).len() > 0

class SideBarGitAddCommitPushCommand(sublime_plugin.WindowCommand):
	def run(self, paths = [], input = False, content = ''):
		if input == False:
			SideBarGit().prompt('Enter a commit message: ', '', self.run, paths)
		elif content != '':
			import sys
			content = (content[0].upper() + content[1:]).encode(sys.getfilesystemencoding())
			for repo in SideBarGit().getSelectedRepos(SideBarSelection(paths).getSelectedItems()):
				commitCommandAdd = ['git', 'add', '--']
				commitCommandCommit = ['git', 'commit', '-m', content, '--']
				for item in repo.items:
					commitCommandAdd.append(item.forCwdSystemPathRelativeFromRecursive(repo.repository.path()))
					commitCommandCommit.append(item.forCwdSystemPathRelativeFrom(repo.repository.path()))
				object = Object()
				object.item = repo.repository
				object.command = commitCommandAdd
				SideBarGit().run(object)
				object = Object()
				object.item = repo.repository
				object.to_status_bar = True
				object.command = commitCommandCommit
				SideBarGit().run(object)
				object = Object()
				object.item = repo.repository
				object.command = ['git','push']
				SideBarGit().run(object, True)

class SideBarGitAddCommand(sublime_plugin.WindowCommand):
	def run(self, paths = []):
		for repo in SideBarGit().getSelectedRepos(SideBarSelection(paths).getSelectedItems()):
			command = ['git', 'add', '--']
			for item in repo.items:
				command.append(item.forCwdSystemPathRelativeFromRecursive(repo.repository.path()))
			object = Object()
			object.item = repo.repository
			object.command = command
			SideBarGit().run(object)

	def is_enabled(self, paths = []):
		return SideBarSelection(paths).len() > 0

class SideBarGitRemoveKeepLocalCommand(sublime_plugin.WindowCommand):
	def run(self, paths = [], confirm = False, drop_me = ''):
		if confirm == False:
			SideBarGit().confirm('Remove from repository, keep local copies? ', self.run, paths)
		else:
			for repo in SideBarGit().getSelectedRepos(SideBarSelection(paths).getSelectedItems()):
				command = ['git', 'rm', '-r', '--cached', '--']
				for item in repo.items:
					command.append(item.forCwdSystemPathRelativeFrom(repo.repository.path()))
				object = Object()
				object.item = repo.repository
				object.command = command
				object.to_status_bar = True
				SideBarGit().run(object)

	def is_enabled(self, paths = []):
		return SideBarSelection(paths).len() > 0

class SideBarGitRemoveCommand(sublime_plugin.WindowCommand):
	def run(self, paths = [], confirm = False, drop_me = ''):
		if confirm == False:
			SideBarGit().confirm('Remove from repository, and remove local copies? ', self.run, paths)
		else:
			for repo in SideBarGit().getSelectedRepos(SideBarSelection(paths).getSelectedItems()):
				command = ['git', 'rm', '-r', '-f', '--']
				for item in repo.items:
					command.append(item.forCwdSystemPathRelativeFrom(repo.repository.path()))
				object = Object()
				object.item = repo.repository
				object.command = command
				SideBarGit().run(object)

	def is_enabled(self, paths = []):
		return SideBarSelection(paths).len() > 0

class SideBarGitLiberalCommand(sublime_plugin.WindowCommand):
	def run(self, paths = [], input = False, content = ''):
		if input == False:
			SideBarGit().prompt('[SideBarGit@SublimeText ./]:', 'git ', self.run, paths)
		elif content != '':
			import sys
			for item in SideBarSelection(paths).getSelectedDirectoriesOrDirnames():
				object = Object()
				object.item = item
				object.command = content.encode(sys.getfilesystemencoding()).split(' ')
				object.title = content
				object.no_results = 'No output'
				object.syntax_file = 'Packages/Diff/Diff.tmLanguage'
				SideBarGit().run(object)

	def is_enabled(self, paths = []):
		return SideBarSelection(paths).len() > 0

 #  }
 #  this.remoteAdd = function(event)
 #  {
	# var aMsg = this.s.prompt('Enter name and URL of remote…');
	# if(aMsg != '')
	# {
	#   var repos = this.getSelectedRepos(event);
	#   var commands = '';
	#   for(var id in repos.r)
	#   {
	# 	commands += 'cd '+repos.r[id].cwd+'';
	# 	commands += '\n';
	# 	commands += 'git remote add '+aMsg+' >>'+repos.obj.output+' 2>&1';
	# 	commands += '\n';
	#   }
	#   this.s.fileWrite(repos.obj.sh, commands);
	#   this.run(repos.obj.sh, repos.obj.outputFile, '', false, true);
	# }
 #  }
 #  this.configDefaultRemote = function(event)
 #  {
	# var aBranch = this.s.prompt('Enter the name of your local branch…');
	# if(aBranch != '')
	#   var aRemote = this.s.prompt('Enter the name of the remote…');
	# if(aBranch != '' && aRemote != '')
	# {
	#   var repos = this.getSelectedRepos(event);
	#   var commands = '';
	#   for(var id in repos.r)
	#   {
	# 	commands += 'cd '+repos.r[id].cwd+'';
	# 	commands += '\n';
	# 	commands += 'git config branch.'+aBranch+'.remote '+aRemote+' >>'+repos.obj.output+' 2>&1';
	# 	commands += '\n';
	#   }
	#   this.s.fileWrite(repos.obj.sh, commands);
	#   this.run(repos.obj.sh, repos.obj.outputFile, '', false, true);
	# }
 #  }
 #  this.command = function(event)
 #  {
	# var selected = this.getSelectedPathFolder(event);
	# var obj = this.getPaths(selected);

	# var aMsg = this.s.prompt('[komodin@komodo '+obj.cwdSelected+'] $ ', 'git ');
	# if(aMsg != '')
	# {
	#   this.s.fileWrite(obj.sh, 'cd '+obj.cwdSelected+' \n'+aMsg+' >>'+obj.output+' 2>&1');
	#   this.loadingSet();
	#   this.s.execute(this.gitPath, obj.sh, obj.outputFile, function(a,b){ kgit.executeObserver(a,b,true)});
	# }
 #  }

 #  }
 #  this.tagAdd = function(event)
 #  {
	# var aMsg = this.s.prompt('Enter tag name to add…', '');
	# if(aMsg != '')
	# {
	#   var repos = this.getSelectedRepos(event);
	#   var commands = '';
	#   for(var id in repos.r)
	#   {
	# 	commands += 'cd '+repos.r[id].cwd+'';
	# 	commands += '\n';
	# 	commands += 'git tag "'+this.s.filePathEscape(aMsg)+'" >>'+repos.obj.output+' 2>&1';
	# 	commands += '\n';
	#   }
	#   this.s.fileWrite(repos.obj.sh, commands);
	#   this.run(repos.obj.sh, repos.obj.outputFile, 'Tag "'+aMsg+'" added', false, true);
	# }
 #  }
 #  this.tagRemove = function(event)
 #  {
	# var aMsg = this.s.prompt('Enter tag name to remove…', '');
	# if(aMsg != '')
	# {
	#   var repos = this.getSelectedRepos(event);
	#   var commands = '';
	#   for(var id in repos.r)
	#   {
	# 	commands += 'cd '+repos.r[id].cwd+'';
	# 	commands += '\n';
	# 	commands += 'git tag -d "'+this.s.filePathEscape(aMsg)+'" >>'+repos.obj.output+' 2>&1';
	# 	commands += '\n';
	#   }
	#   this.s.fileWrite(repos.obj.sh, commands);
	#   this.run(repos.obj.sh, repos.obj.outputFile, '', false, true);
	# }
 #  }
 #  this.tagAuto = function(event)
 #  {
	# var repos = this.getSelectedRepos(event);
	# var commands = '';
	# for(var id in repos.r)
	# {
	#   var version = this.repositoryPreference(id, 'version') || 0;
	# 	  version++;
	#   this.repositoryPreference(id, 'version', version);

	#   commands += 'cd '+repos.r[id].cwd+'';
	#   commands += '\n';
	#   commands += 'git tag "'+this.s.filePathEscape(this.s.now().replace(/-/g, '').substr(2, 6)+'.'+version)+'" >>'+repos.obj.output+' 2>&1';
	#   commands += '\n';
	# }
	# this.s.fileWrite(repos.obj.sh, commands);
	# this.run(repos.obj.sh, repos.obj.outputFile, 'Tag '+this.s.now().replace(/-/g, '').substr(2, 6)+' added', false, true);
 #  }
 #  this.tagList = function(event)
 #  {
	# var repos = this.getSelectedRepos(event);
	# var commands = '';
	# for(var id in repos.r)
	# {
	#   commands += 'cd '+repos.r[id].cwd+'';
	#   commands += '\n';
	#   commands += 'git tag -l >>'+repos.obj.output+' 2>&1';
	#   commands += '\n';
	# }
	# this.s.fileWrite(repos.obj.sh, commands);
	# this.run(repos.obj.sh, repos.obj.outputFile, '', true, false);
 #  }
 #  this.tagsGetFromRepo = function(aObj)
 #  {
	# var sh = this.s.fileCreateTemporal('kGit.sh', '');

	# this.s.fileWrite(sh, 'cd '+aObj.cwd+' \n echo `git for-each-ref refs/tags --sort=-authordate` \n');

	# var tags = this.run(sh, sh+'.diff', '', false, false, true).split('\n');
	# 	tags.shift();
	# 	tags.shift();
	# 	tags.shift();
	# 	tags.shift();
	# 	tags.shift();
	# 	tags = tags.join('');
	# 	tags = tags.split('refs/tags/');
	# 	tags.shift();
	# 	for(var id in tags)
	# 	  tags[id] = tags[id].split(' ')[0];
	# 	tags.reverse();
	# return tags;
 #  }


#  //TODO: hardcoded branch name

 #  }
 #  this.diffBetweenLatestTagAndLastCommit = function(event)
 #  {
	# var selected = this.getSelectedPaths(event);
	# for(var id in selected)
	# {
	#   var obj = this.getPaths(selected[id]);
	#   var tags = this.tagsGetFromRepo(obj);
	#   this.s.fileWrite(obj.sh, 'cd '+obj.cwd+'\ngit diff "'+(tags.pop() || '')+'"... -- '+obj.selected+' >>'+obj.output+' 2>&1\n');
	#   this.run(obj.sh, obj.outputFile, 'No difference found', true);
	# }
 #  }
 #  this.diffBetweenTheTwoLatestTags = function(event)
 #  {
	# var selected = this.getSelectedPaths(event);
	# for(var id in selected)
	# {
	#   var obj = this.getPaths(selected[id]);
	#   var tags = this.tagsGetFromRepo(obj);
	#   this.s.fileWrite(obj.sh, 'cd '+obj.cwd+'\ngit diff "'+(tags[tags.length-2] || '')+'".."'+(tags[tags.length-1] || '')+'" -- '+obj.selected+' >>'+obj.output+' 2>&1\n');
	#   this.run(obj.sh, obj.outputFile, 'No difference found', true);
	# }
 #  }
 #  this.logSinceLatestTag = function(event)
 #  {
	# var selected = this.getSelectedPaths(event);
	# for(var id in selected)
	# {
	#   var obj = this.getPaths(selected[id]);
	#   var tags = this.tagsGetFromRepo(obj);
	#   this.s.fileWrite(obj.sh, 'cd '+obj.cwd+'\n echo "log:'+this.s.filePathEscape(this.s.pathToNix(obj.selectedFile))+'" >> '+obj.output+' \n git log "'+(tags.pop() || '')+'"... --stat --graph -- '+obj.selected+' >>'+obj.output+' 2>&1\n');
	#   this.run(obj.sh, obj.outputFile, 'No log to show', true);
	# }

 #  this.logBetweenTheTwoLatestTags = function(event)
 #  {
	# var selected = this.getSelectedPaths(event);
	# for(var id in selected)
	# {
	#   var obj = this.getPaths(selected[id]);
	#   var tags = this.tagsGetFromRepo(obj);
	#   this.s.fileWrite(obj.sh, 'cd '+obj.cwd+' echo "log:'+this.s.filePathEscape(this.s.pathToNix(obj.selectedFile))+'" >> '+obj.output+' \n git log "'+(tags[tags.length-2] || '')+'".."'+(tags[tags.length-1] || '')+'" --stat --graph -- '+obj.selected+' >>'+obj.output+' 2>&1\n');
	#   this.run(obj.sh, obj.outputFile, 'No log to show', true);
	# }
 #  }