def main():
    import glob
    import pyfits as pf
    import matplotlib.pyplot as plt
    import numpy as np

    fitslst = glob.glob('*.fits')
    fitslst.sort()

    for i in xrange(len(fitslst)):
        
        hdulist = pf.open(fitslst[i])
        plt.figure(i)
    
        for extension in hdulist[1:]:
            temp = extension.header['TEMPERAT']
            logg = extension.header['LOGG']
            plt.plot(temp, logg, 'bo')
        plt.title(fitslst[i])
        plt.xlabel('Temperature')
        plt.ylabel('g')
        plt.xlim(500,1800)
        plt.ylim(3.4,5.6)
        plt.savefig('model-'+fitslst[i][:-4]+'png')
#        plt.show()

       


if __name__ == '__main__':
   main()
