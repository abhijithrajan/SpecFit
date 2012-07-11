#=========================================================================#
# Script written to generate fits tables from Madhusudhan et al (2012)
# models
#
# Abhijith Rajan
# 06/05/2012
#=========================================================================#
def main():
   import glob
   import numpy as np
   import pyfits as pf
   import matplotlib.pyplot as plt

   dirlst = glob.glob('*cloud*')
   dirlst.sort()

   for dirname in dirlst:
      print dirname

      filelist = glob.glob(dirname+'/*.21')
      filelist.sort()

      hdu = pf.PrimaryHDU(np.arange(100))
      hdulist = pf.HDUList([hdu])

      for fname in filelist:
         logg, partsize, temperature, metal, lam, flam = getDataCloudy(fname)
         c1 = pf.Column(name='Wavelength',format='E',array=lam)
         c2 = pf.Column(name='Flux',format='E',array=flam)
         tbhdu = pf.new_table([c1,c2])
         tbhdu.header.update('LOGG',logg)
         tbhdu.header.update('TEMPERAT',temperature,'units K')
         tbhdu.header.update('PARTSIZE',partsize,'units microns')
         tbhdu.header.update('Z',metal)
         hdulist.append(tbhdu)
   
      hdulist.writeto(dirname+'.fits')

   dirlst = glob.glob('clr*')
   dirlst.sort()

   for dirname in dirlst:
      print dirname

      filelist = glob.glob(dirname+'/*.clr')
      filelist.sort()

      hdu = pf.PrimaryHDU(np.arange(100))
      hdulist = pf.HDUList([hdu])

      for fname in filelist:
         logg, temperature, eddy, metal, lam, flam = getDataClr(fname)
         c1 = pf.Column(name='Wavelength',format='E',array=lam)
         c2 = pf.Column(name='Flux',format='E',array=flam)
         tbhdu = pf.new_table([c1,c2])
         tbhdu.header.update('LOGG',logg)
         tbhdu.header.update('TEMPERAT',temperature,'units K')
         tbhdu.header.update('EDDYCOEF',eddy)
         tbhdu.header.update('Z',metal)
         hdulist.append(tbhdu)
   
      hdulist.writeto(dirname+'.fits')



#=========================================================================#
def getDataCloudy(fname):
   import numpy as np


   params = fname.split('/')[1].split('g')
   logg = float(params[1][:-3])
   restopars = params[0].split('.')
   partsize = restopars[0]
   temperature = float(restopars[1])
   if restopars[3] != '': 
      metal = restopars[3]
   else:
      metal = 'SOLAR'
   
   inf = open(fname,'r')
   flines = inf.readlines()[2:]
   
   lam = np.empty(0)
   flam = np.empty(0)
   for lines in flines:
      lines = lines.split()
      tlam = float(lines[2].replace('D','E'))
      mjy = float(lines[5].replace('D','E'))
# Conversion factor Jy to W/m2/um 
# 1 Jy = 3.3356E-12 W/m2/um / [X um]^2 
      lam = np.append(lam, tlam)
      flam = np.append(flam, (mjy*(1E-3)*(3.3356E-12)/(tlam**2)))

   return ( logg, partsize, temperature, metal, lam, flam )

#=========================================================================#
def getDataClr(fname):
   import numpy as np

   params = fname.split('/')[1].split('_')
   temperature = float(params[0][1:])
   if len(params) > 2:
      logg = float(params[1][1:])/10
      eddy = params[2][:-4]
   else:
      logg = float(params[1][1:-4])/10
      eddy = 'BLANK'
   metal = 'SOLAR'

   inf = open(fname,'r')
   flines = inf.readlines()[2:]
   
   lam = np.empty(0)
   flam = np.empty(0)
   for lines in flines:
      lines = lines.split()
      tlam = float(lines[2].replace('D','E'))
      mjy = float(lines[5].replace('D','E'))
# Conversion factor Jy to W/m2/um 
# 1 Jy = 3.3356E-12 W/m2/um / [X um]^2 
      lam = np.append(lam, tlam)
      flam = np.append(flam, (mjy*(1E-3)*(3.3356E-12)/(tlam**2)))

   return ( logg, temperature, eddy, metal, lam, flam )

#=========================================================================#
if __name__ == '__main__':
   main()
