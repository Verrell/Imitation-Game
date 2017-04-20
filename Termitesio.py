import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import random
import math

class Food:
	Fcount=0
	def __init__(self,varx,vary):
		self.varx=varx
		self.vary=vary
		self.target=-1#cek sudah ada rayap lain yang menarget
		Food.Fcount+=1
	def setpos(self,varx,vary):
		self.varx=varx
		self.vary=vary
	#untuk random posisi lagi setelah dimakan
	def randompos(self):
		self.varx=random.randint(10,70)*1.0/10
		self.vary=random.randint(10,70)*1.0/10
		self.target=-1
	def settarget(self,x):
		self.target=x
	def getx(self):
		return self.varx
	def gety(self):
		return self.vary
	def gettarget(self):
		return self.target
	def displaypos(self):
		print ("Position X:%f Y:%f" %(self.varx,self.vary))

class Termites:
	Tcount=0
	def __init__(self,varx,vary):
		self.num=Termites.Tcount
		self.target=-1#cek apakah rayap sudah punya target
		self.trgtype='F'#untuk switch
		self.varx=varx
		self.vary=vary
		self.varpoint=0
		self.varlevel=0
		self.varspeed=0.1
		self.varmaxpoint=5
		self.varsize=40
		Termites.Tcount+=1
	def setpos(self,varx,vary):
		self.varx=varx
		self.vary=vary
	def settrgtype(self,x):
		self.trgtype=x
	def getx(self):
		return self.varx
	def gety(self):
		return self.vary
	def getsize(self):
		return self.varsize
	def getpoint(self):
		x=(10+(self.varlevel-1)*5)*self.varlevel/2
		return x
	def getlevel(self):
		return self.varlevel
	def getnum(self):
		return self.num
	def gettrgtype(self):
		return self.trgtype
	def gettarget(self):
		return self.target
	def displaypos(self):
		print ("Position X:%f Y:%f" %(self.varx,self.vary))
	#fungsi makan
	def eat(self):
		self.varpoint+=1
		self.target=-1
		if (self.varpoint == self.varmaxpoint):
			self.varpoint=0
			self.varmaxpoint+=5
			self.varlevel+=1
			self.varsize+=40
			# if (self.varspeed > 0.005):
			# 	self.varspeed-=0.01
	def eatter(self,x):
		self.varpoint+=vartermites[x].getpoint()
		self.target=-1
		self.trgtype='F'
		while (self.varpoint >= self.varmaxpoint):
			self.varpoint-=self.varmaxpoint
			self.varmaxpoint+=5
			self.varlevel+=1
			self.varsize+=40
			# if (self.varspeed > 0.005):
			# 	self.varspeed-=0.01
		varfood[vartermites[x].gettarget()].settarget(-1)
		vartermites.pop(x)
	#fungsi untuk bergerak mendekat ke makanan
	def move(self):
		enemies=[]
		varstat=0
		for i in range(len(vartermites)):
			if (self.num!=vartermites[i].getnum() and self.varlevel<vartermites[i].getlevel()):
				dist=math.sqrt((vartermites[i].getx()-self.varx)**2+(vartermites[i].gety()-self.vary)**2)
				if (dist<0.2):
					enemies.append(i)
					varstat=1
		if (varstat==1):
			self.flee(enemies)
		else:
			self.movetofood()

	def flee(self,en):
		varfood[self.target].settarget(-1)
		self.target=-1
		self.trgtype='F'
		bdist=0.0
		l=self.varspeed
		ang=0.0
		dang=0.1
		bang=ang
		dx=l*math.cos(ang)+self.varx
		dy=l*math.sin(ang)+self.vary
		for i in range(len(en)):
			dist=math.sqrt((vartermites[i].getx()-dx)**2+(vartermites[i].gety()-dy)**2)
			bdist+=dist
		ang+=dang
		while (ang<6.28):
			tbdist=0.0
			dx=l*math.cos(ang)+self.varx
			dy=l*math.sin(ang)+self.vary
			for i in range(len(en)):
				dist=math.sqrt((vartermites[i].getx()-dx)**2+(vartermites[i].gety()-dy)**2)
				tbdist+=dist
			if(tbdist>bdist):
				bdist=tbdist
				bang=ang
			ang+=dang
		dx=l*math.cos(bang)+self.varx
		dy=l*math.sin(bang)+self.vary
		if ((dx>=1 and dx<=7) and (dy>=1 and dy<=7)):
			print('Flee')
			self.varx=dx
			self.vary=dy

	def movetofood(self):
		#untuk menentukan makan mana
		F=0
		T=0
		#cek dengan makanan
		mindist=math.sqrt((self.varx-varfood[0].getx())**2+(self.vary-varfood[0].gety())**2)
		minfood=0
		for i in range(len(varfood)):
			dist=math.sqrt((self.varx-varfood[i].getx())**2+(self.vary-varfood[i].gety())**2)
			if (self.target!=-1):
				mindist=math.sqrt((self.varx-varfood[self.target].getx())**2+(self.vary-varfood[self.target].gety())**2)
			if (mindist > dist and varfood[i].gettarget()==-1):
				mindist=dist
				minfood=i
		#cek dengan rayap lain
		mindistT=999
		minfoodT=999
		for i in range(len(vartermites)):
			if (vartermites[i].getnum()!=self.num):
				distT=math.sqrt((self.varx-vartermites[i].getx())**2+(self.vary-vartermites[i].gety())**2)
				if (mindistT > distT and self.varlevel>vartermites[i].getlevel()):
					mindistT=distT
					minfoodT=i
		#bandingkan jarak makanan terdekat dengan rayap terdekat
		if (mindistT >= mindist):
			F=1
			if (self.trgtype=='T'):
				self.target=-1
			self.trgtype='F'
		else:
			T=1
			mindist=mindistT
			minfood=minfoodT

		if (F==1):
			if (self.target==-1):
				varfood[minfood].settarget(self.num)
				self.target=minfood
				dx=self.varspeed*(varfood[minfood].getx()-self.varx)/mindist
				dy=self.varspeed*(varfood[minfood].gety()-self.vary)/mindist
				self.varx+=dx
				self.vary+=dy
			else:
				minfood=self.target
				mindist=math.sqrt((self.varx-varfood[minfood].getx())**2+(self.vary-varfood[minfood].gety())**2)
				dx=self.varspeed*(varfood[minfood].getx()-self.varx)/mindist
				dy=self.varspeed*(varfood[minfood].gety()-self.vary)/mindist
				self.varx+=dx
				self.vary+=dy
		else:
			if (self.target==-1):
				self.trgtype='T'
				self.target=minfood
				dx=self.varspeed*(vartermites[minfood].getx()-self.varx)/mindist
				dy=self.varspeed*(vartermites[minfood].gety()-self.vary)/mindist
				self.varx+=dx
				self.vary+=dy
			else:
				if (self.trgtype=='F'):
					varfood[self.target].settarget(-1)
					self.trgtype='T'
				self.target=minfood
				mindist=math.sqrt((self.varx-vartermites[minfood].getx())**2+(self.vary-vartermites[minfood].gety())**2)
				dx=self.varspeed*(vartermites[minfood].getx()-self.varx)/mindist
				dy=self.varspeed*(vartermites[minfood].gety()-self.vary)/mindist
				self.varx+=dx
				self.vary+=dy

varfood=[]
vartermites=[]

for i in range(50):
	varfood.append(Food(random.randint(10,70)*1.0/10,random.randint(10,70)*1.0/10))

for i in range(20):
	vartermites.append(Termites(random.randint(10,70)*1.0/10,random.randint(10,70)*1.0/10))

tmax=500

for t in range(tmax):
	fig = plt.figure()
	plt.gca().set_xlim([0, 8])
	plt.gca().set_ylim([0, 8])
	for i in range (len(varfood)):
		plt.scatter(varfood[i].getx(),varfood[i].gety(),color='blue',marker='d',s=20)
	for i in range(len(vartermites)):
		plt.scatter(vartermites[i].getx(),vartermites[i].gety(),color='red',s=vartermites[i].getsize())
		vartermites[i].move()
	#pengecekan rayap makan makanan
	for i in range(len(varfood)):
		for j in range(len(vartermites)):
			if (vartermites[j].gettrgtype()=='F'):
				if (abs(vartermites[j].getx() - varfood[i].getx()) < 0.05 and abs(vartermites[j].gety() - varfood[i].gety()) < 0.05):
					vartermites[j].eat()
					varfood[i].randompos()
	#pengecekan rayap makan rayap
	C=0
	for i in range(len(vartermites)):
		C=0
		for j in range(len(vartermites)):
			if (vartermites[i].gettrgtype()=='T' and vartermites[i].getnum()!=vartermites[j].getnum() and vartermites[i].getlevel()>vartermites[j].getlevel()):
				if (abs(vartermites[i].getx() - vartermites[j].getx()) < 0.09 and abs(vartermites[i].gety() - vartermites[j].gety()) < 0.09):
					vartermites[i].eatter(j)
					print('Eat')
					C=1
					break
		if (C==1):
			break
	plt.title('{0:03d}'.format(t))
	filename = 'frame{0:03d}.png'.format(t)
	plt.savefig(filename, bbox_inches='tight')
	plt.close(fig)
	plt.cla()