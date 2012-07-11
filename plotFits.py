def main():
    import glob
    import pyfits as pf
    import matplotlib.pyplot as plt
    import numpy as np

    abpic = np.loadtxt('BD_spectra/ABPicB-JHK-fc.txt')


    flist = glob.glob('Burrows/*cloud*.fits')
    flist.sort()

    for fname in flist:
        print fname
        hdulist = pf.open(fname)
        for extension in hdulist[1:]:
            temp = extension.header['TEMPERAT']
            logg = extension.header['LOGG']
            metal = extension.header['Z']
            partsize = extension.header['PARTSIZE']


            if temp == 1500 and logg == 4.0 and partsize == 'A' and metal == 'SOLAR':
                print temp, logg, metal, partsize

                tbdata = extension.data
                lam = tbdata.field(0)
                flam = tbdata.field(1)
            
                plt.plot(abpic[:,0],abpic[:,1])
                plt.plot(lam, (1.87**2/2)*flam/22.37)
                plt.title(fname)
                plt.title(fname[8:-5] + ', T = %i K, log(g) = %.1f, Z = %s, Size = %s' % (temp,logg, metal, partsize))
                plt.xlabel('Wavelength (microns)')
                plt.ylabel('Flam (W/m2/um)')
                plt.xlim(1,2.5)
                plt.savefig('Plots/%s_%i_%.1f_%s.pdf' % (fname[8:-5],temp,logg,partsize))
            #plt.savefig('Plots/%s_%i_%.1f_%s_%s.pdf' % (fname[8:-5],temp,logg, metal, partsize))
                plt.close()
            

if __name__ == '__main__':
   main()
