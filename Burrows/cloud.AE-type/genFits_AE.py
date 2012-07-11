def main():
   import glob
   import numpy as np
   import pyfits as pf
   import matplotlib.pyplot as plt

   filelist = glob.glob('cloud.AE-type/*.21')
   filelist.sort()

   hdu = pf.PrimaryHDU(np.arange(100))
   hdulist = pf.HDUList([hdu])

   for fname in filelist:
      g, partsize, temperature, lam, flam = getData(fname)
      c1 = pf.Column(name='Wavelength',format='E',array=lam)
      c2 = pf.Column(name='Flux',format='E',array=flam)
      tbhdu = pf.new_table([c1,c2])
      tbhdu.header.update('SURFGRAV',g)
      tbhdu.header.update('TEMPERAT',temperature,'units K')
      tbhdu.header.update('PARTSIZE',partsize,'units microns')
      hdulist.append(tbhdu)
   
   hdulist.writeto('cloud.AE-type.fits')

   
#   plt.figure()   
#   plt.plot(lam, flam)
#   plt.xlabel('Wavelength (microns)')
#   plt.ylabel('Flam')
#   plt.xlim(0,10)
#   plt.show()


def getData(fname):
   import numpy as np

   params = fname.split('/')[1].split('g')
   g = params[1][:-3]
   restopars = params[0].split('.')
   partsize = restopars[0]
   temperature = restopars[1]
   
   inf = open(fname,'r')
   flines = inf.readlines()[2:]
   
   lam = np.empty(0)
   flam = np.empty(0)
   for lines in flines:
      lines = lines.split()
      lam = np.append(lam,float(lines[2].replace('D','E')))
      flam = np.append(flam,float(lines[4].replace('D','E')))

   return ( g, partsize, temperature, lam, flam )


if __name__ == '__main__':
   main()
