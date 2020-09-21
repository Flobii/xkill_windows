# pylint: disable=C0114
# pylint: disable=W0312
# pylint: disable=C0103
# pylint: disable=W0401
# pylint: disable=R0913
# pylint: disable=C0330
# pylint: disable=C0200
# pylint: disable=W0105
# pylint: disable=E0611

from os import system
from win32gui import GetWindowText, GetForegroundWindow

cmd_name: str = 'xkill'

def kill_active_window() -> None:
	'''Kills the program in the foreground (the active window) if it is not
	the cmd it runs in.
	'''
	while True:
		active_window_title: str = GetWindowText(GetForegroundWindow())
		if active_window_title not in(cmd_name, ''):
			taskkill = (f'taskkill /F /FI "WINDOWTITLE eq {active_window_title}"')
			system(taskkill)
			break

def main():
	'''The main function, setting the cli up, etc.
	'''
	system('title {}'.format(cmd_name))
	system('cls')
	print('Click on the window you want to terminate!')
	kill_active_window()

if __name__ == '__main__':
	main()
