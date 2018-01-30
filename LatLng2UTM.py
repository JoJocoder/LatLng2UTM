# -*- coding: utf-8 -*- 
import math

pi=math.pi
sm_a = 6378137.0
sm_b = 6356752.314
UTMScaleFactor = 0.9996



def LatLng2UTM(Lat,Lng):
	zone=math.floor((Lng+180.0)/6)+1
	cm=UTMCentralMeridian(zone)
	xy=MapLatLng2XY(Lat / 180.0 * pi, Lng / 180 * pi, cm)
	xy[0] = xy[0] * UTMScaleFactor + 500000.0
	xy[1] = xy[1] * UTMScaleFactor
	if xy[1]<0.0:
		xy[1]=xy[1]+10000000.0
	return[xy[0],xy[1],zone]

def UTMCentralMeridian (zone):
	deg=-183.0+zone*6.0
	cmeridian=deg/180.0*pi
	return cmeridian

def MapLatLng2XY(phi,lambda0,lambda1):
	ep2=(math.pow(sm_a,2.0)-math.pow(sm_b,2.0))/math.pow(sm_b,2.0)
	nu2=ep2*math.pow(math.cos(phi),2.0)
	N = math.pow(sm_a, 2.0) / (sm_b * math.sqrt(1 + nu2))
	t = math.tan (phi)
	t2=t*t
	tmp = (t2 * t2 * t2) - math.pow (t, 6.0)
	l=lambda0-lambda1
	l3coef = 1.0 - t2 + nu2
	l4coef = 5.0 - t2 + 9 * nu2 + 4.0 * (nu2 * nu2)
	l5coef = 5.0 - 18.0 * t2 + (t2 * t2) + 14.0 * nu2- 58.0 * t2 * nu2
	l6coef = 61.0 - 58.0 * t2 + (t2 * t2) + 270.0 * nu2- 330.0 * t2 * nu2
	l7coef = 61.0 - 479.0 * t2 + 179.0 * (t2 * t2) - (t2 * t2 * t2)
	l8coef = 1385.0 - 3111.0 * t2 + 543.0 * (t2 * t2) - (t2 * t2 * t2)
	x= N * math.cos (phi) * l\
                + (N / 6.0 * math.pow (math.cos (phi), 3.0) * l3coef * math.pow (l, 3.0))\
                + (N / 120.0 * math.pow(math.cos(phi), 5.0) * l5coef * math.pow(l, 5.0))\
                + (N / 5040.0 * math.pow(math.cos(phi), 7.0) * l7coef * math.pow(l, 7.0))
	y= ArcLengthOfMeridian (phi)\
                + (t / 2.0 * N * math.pow(math.cos(phi), 2.0) * math.pow(l, 2.0))\
                + (t / 24.0 * N * math.pow(math.cos(phi), 4.0) * l4coef * math.pow(l, 4.0))\
                + (t / 720.0 * N * math.pow(math.cos(phi), 6.0) * l6coef * math.pow(l, 6.0))\
                + (t / 40320.0 * N * math.pow(math.cos(phi), 8.0) * l8coef * math.pow(l, 8.0))
	return [x,y]
def ArcLengthOfMeridian(phi):
	n = (sm_a - sm_b) / (sm_a + sm_b)
	alpha = ((sm_a + sm_b) / 2.0)* (1.0 + (math.pow(n, 2.0) / 4.0) + (math.pow(n, 4.0) / 64.0))
	beta = (-3.0 * n / 2.0) + (9.0 * math.pow(n, 3.0) / 16.0)+ (-3.0 * math.pow(n, 5.0) / 32.0)
	gamma = (15.0 * math.pow(n, 2.0) / 16.0)+ (-15.0 * math.pow(n, 4.0) / 32.0)
	delta = (-35.0 * math.pow(n, 3.0) / 48.0)+ (105.0 * math.pow(n, 5.0) / 256.0)
	epsilon = (315.0 * math.pow(n, 4.0) / 512.0)
	result = alpha* (phi + (beta * math.sin (2.0 * phi))\
                    + (gamma * math.sin(4.0 * phi))\
                    + (delta * math.sin(6.0 * phi))\
                    + (epsilon * math.sin(8.0 * phi)))
	return result
if __name__ == '__main__':
	print(LatLng2UTM(32.089648,118.748517))
  #[665007.1204623702, 3551710.38908969, 50]





