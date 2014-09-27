import win32api, win32con, win32gui


def click(x, y):
	win32api.SetCursorPos((x, y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


while True:
	cl = input('Clicks: ')
	for i in range(0, cl):
		click(950, 480)
	
