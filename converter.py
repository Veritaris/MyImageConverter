# -----------------------------------Importing neccessary libraries---------------------------------
from tkinter import filedialog
import tkinter 
from PIL import Image
# -----------------------------------Initialising window object-------------------------------------
window = tkinter.Tk()
# -----------------------------------Window config--------------------------------------------------
app_width = 750 #App width
app_height = 400 #App height
resize_arg = False #Can user resize window
screen_height = int(window.winfo_screenheight()/4) #Top left corner y-position
screen_width = int((window.winfo_screenwidth()-app_width)/2) #Top left corner x-position
# -----------------------------------Other default settings-----------------------------------------
default_transforming_mode = 'Single'
default_font = 'Montserrat 16'
default_bg_color = '#0B61B4'
path = ''
# -----------------------------------Formatting window settings-------------------------------------
window.geometry('{}x{}+{}+{}'.format(app_width,app_height,screen_width,screen_height))
window.resizable(resize_arg, resize_arg)
window.title('Image converter')
window.config(bg = '#0B61B4')
# -----------------------------------List of available file extensions------------------------------
extension_list = [
				'.ico', 
				'.png',
				'.jpg(Not supperted now)',
				'.jpeg(Not supperted now)',
				'.bmp',
				'.gif'
				]
extension_dict = {
	'0':'.ico',
	'1':'.png',
	'2':'.jpg(Not supperted now)',
	'3':'.jpeg(Not supported now)',
	'4':'.bmp',
	'5':'.gif'
	}
# -----------------------------------Name-inpute entry----------------------------------------------
filename = tkinter.Entry(window)
filename.config(
	font = default_font,
	bd = 0)
# -----------------------------------Getting a path-------------------------------------------------	
def get_path():
	global path
	path = filedialog.askopenfilename()
	filename.insert(0,path.split('.')[0].split('/')[-1])
# -----------------------------------Asking a path to start file------------------------------------
choose_file = tkinter.Button(window)
choose_file['command'] = lambda:get_path()
choose_file.config(
	text = 'Choose file',
	font =  default_font,
	bg = 'yellow',
	bd = 0)
# -----------------------------------Swap transforming mode function--------------------------------
def swap_mode(mode, Button):
	if (mode == 'Single'):
		Button['text'] = 'Transform to many extensions'
		Button.mode = 'Multy'
		Button['bg'] = 'red'
		extension_multy.place(x = 440, y = 195)
		ext_single.place_forget()
	else:
		Button['bg'] = 'green'
		Button.mode = 'Single'
		Button['text'] = 'Transform to a single extension'
		extension_multy.place_forget()
		ext_single.place(x = 440, y = 195)
# -----------------------------------Swap transforming mode button----------------------------------
mode_button = tkinter.Button(window, command = lambda:swap_mode(mode_button.mode,mode_button))
mode_button.mode = default_transforming_mode
mode_button.config(
	font = default_font,
	text = 'Transform to a single extension',
	bg = 'green',
	activebackground = '#122952',
	bd = 0)
# -----------------------------------Transform to a single extension--------------------------------
extension_single = tkinter.StringVar(window)
extension_single.set(".jpg") # default value
ext_single = tkinter.OptionMenu(window, extension_single, *extension_list)
ext_single.config(
	font = default_font,
	bd = 0)
# -----------------------------------Transform to non-single extension------------------------------ 
extension_multy = tkinter.Listbox(window)
extension_multy.config(
	highlightbackground = default_bg_color,
	width = max(map(len,extension_list)),
	height = len(extension_list), 
	selectbackground = '#122952',
	selectmode = 'extended',
	activestyle = 'none',
	font = default_font, 
	bd = 0)
for ext in extension_list:
	extension_multy.insert(tkinter.END, ext)
# -----------------------------------Transforming function------------------------------------------
def transform(single,multy,mode):
	print(mode)
	if (mode == 'Single'):
		img = Image.open(path)
		img.save(path.split('.')[0]+single.get())
	else:
		extensions = list(map(str,multy.curselection()))
		img = Image.open(path)
		for ext in extensions:
			img.save(path.split('.')[0]+extension_dict[ext])
# -----------------------------------Transforming button--------------------------------------------
transorm_button = tkinter.Button(window)
transorm_button['command'] = lambda:transform(extension_single,extension_multy,mode_button.mode)
transorm_button.config(
	text = 'Transform image',
	font = default_font,
	bg = '#122952',
	bd = 0)
# -----------------------------------Initializing window elements-----------------------------------
mode_button.place(x = 230, y = 25)
choose_file.place(x = 320, y = 65)
transorm_button.place(x = 295, y = 100)
filename.place(x = 190, y = 200)
ext_single.place(x = 440, y = 195)
# -----------------------------------Initializing window--------------------------------------------
window.mainloop()