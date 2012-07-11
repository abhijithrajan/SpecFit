def main():
   import glob
   import numpy as np
   import matplotlib.pyplot as plt

   wcloudlst = glob.glob('Burrows/cloud*')
   wocloudlst = glob.glob('Burrows/clr*')
   fecloud = glob.glob('Burrows/Fe*')

   
   #for model in modellst:
      
   filelist = glob.glob(modellst[0]+'/*.21')
   filelist.sort()
   print filelist
   
   #for fname in filelist:
   fname = filelist[0]
   lam, flam = getData(fname)


   plt.figure()   
   plt.plot(lam, flam)
   plt.xlabel('Wavelength (microns)')
   plt.ylabel('Flam')
   plt.xlim(0,10)
   plt.show()

def getData(fname):
   import numpy as np
   inf = open(fname,'r')
   flines = inf.readlines()[2:]
   
   lam = np.empty(0)
   flam = np.empty(0)
   for lines in flines:
      lines = lines.split()
      #lam = np.append(lam,double(lines[2]))
      lam = np.append(lam,float(lines[2].replace('D','E')))
      flam = np.append(flam,float(lines[4].replace('D','E')))

   return ( lam, flam )

if __name__ == '__main__':
   main()
