import os,platform
os.system('fmz.py')
 
trt=platform.architecture()[0]
if trt=="32bit":
    print('Sorry 32 Bit Not Supported...')
elif trt=="64bit":
    __import__("1fmz.py")
