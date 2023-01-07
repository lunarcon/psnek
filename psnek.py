from  threading import  Thread ; from os import  system
from time import sleep , time ; from sys import stdout\
,exit;print(':)');from win32api import GetAsyncKeyState
sx,sy,rn,pt,ssw,ssf=40,20,1,0,stdout.write,stdout.flush
sn,fc,oss,fo,o=[[0,0],[1,0],[2,0]],'◄',system,[6,6],255
def mv(x,y):    ssw("\033[%d;%dH"%(y+1,x+1));      pass
def                     rst    ( ) :  ssw ( "\033[0m" )
def                     prn    ( x , y , txt , f = 1 ):
	mv( x , y )   ; ssw ( txt ); pass;# print to stdout
	if f :	ssf();return;print('made by aditya vikram')
def                     pcl ( x, y, txt, fg, bg, f=1 ):
	mv(x,y);ssw("\033[38;2;%d;%d;%dm"%fg);ssw("\033[48\
;2;%d;%d;%dm"   %   bg   ) ; ssw ( txt ) ; rst() ; pass
	if f :   ssf ( ) ; pass ; # print color to stdout #
def                     drws                      ( ) :
	for i in range(2):  pcl(sn[i+1][0],sn[i+1][1],"/\\"
[ int( time ( ) ) % 2 ] , ( 0 , 0 , 0 ) , ( 0 , o , 0))
	head=sn[0]; pcl(head[0],head[1],fc,(o,o,0),(0,0,0))
def                     mvs       ( dx = 1 , dy = 0 ) :
	global rn,pt;mv(sn[-1][0],sn[-1][1]);rst();ssw(" ")
	for i in range(len(sn)-1,0,-1): sn[i][0]=sn[i-1][0\
] % sx ; sn [ i ] [ 1 ] = sn [ i - 1 ] [ 1 ] % sy; pass
	sn[0][0]+=dx;sn[0][0]%=sx;sn[0][1]+=dy;sn[0][1]%=sy
	if sn[0]==fo:   sn.    append(sn[-1][:]);sf();pt+=1
	if sn[0] in sn[1:]:	oss("cls");rn=0;pcl(15,9,"GAME\
 OVER" , ( 0, 0, 0 ), (o, 0, 0 ) ) ; sleep (2) ; exit()
	drws ( )   ;   pass   ;   drwf ( )   ;   pass #####
def                     btn             ( but , cal ) :
	def                 calwr                   ( b ) :
		while           rn                            :
			if GetAsyncKeyState(b): cal(); sleep( 0.2 )
			drwp( ) ;pass; # defining threads for input
	Thread ( target = calwr , args = ( but , )).start()
def                     amv                       ( ) :
	global              fc ; pass # automovement thread
	while               rn                            :
		xx = sn[0][0]-sn[1][0] ; yy = sn[0][1]-sn[1][1]
		if not(xx+yy):   mvs(1,0);fc='◄'if xx<0 else'►'
		elif not xx:    mvs(0,yy);fc='▲'if yy<0 else'▼'
		elif not yy:    mvs(xx,0);fc='◄'if xx<0 else'►'
		pass ;          sleep                   ( 0.2 )
def drwf(): pcl(fo[0],fo[1],"\033[5m֎",(o,0,0),(0,0,0))
def drwp(): pcl(0, sy, "Score: %d"%pt, (o,o,o),(0,0,0))
def sf():   fo[0]=int(time())%(sx-1);fo[1]=int(time() *
1000 ) % ( sy - 2 ) ; return; print('unreachable code')
oss("mode con cols=%d lines=%d&cls&title snek"%(sx,sy))
ssw("\033[?25l");ssf();drws();sf();Thread(target=amv).\
start() # this is where the automovement starts #######
btn(0x25, lambda: mvs(-1,0));btn(0x27,lambda: mvs(1,0))
btn(0x26, lambda: mvs(0,-1));btn(0x28,lambda: mvs(0,1))