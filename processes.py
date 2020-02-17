import psutil
import os

def main():
    processes = []
    pidflag = 0

    for ps in psutil.process_iter( ['pid', 'name', 'username'] ):
        processes.append(ps)

    for ps in processes:
        print(ps.info)

    pid = input("\nPlease enter a pid to examine:\n")

    for ps in psutil.process_iter( ['pid', 'name', 'username'] ):
        processes.append(ps)

    print("\nThreads:")

    ps = psutil.Process( int(pid) )
    print(ps.threads())

    print("\nModules:")
    os.system('lsmod')


    print("\nExecutable Pages:")
    print("\n Written to file: expages.txt")

    o = open("expages.txt","w")

    for ps in psutil.process_iter( ['pid'] ):
        string = "/proc/" + str(ps.info['pid']) + "/maps"
        f = open(string,'r')
        o.write("pid: %d\n" % ps.info['pid'])
        fl = f.readlines()
        for l in fl:
            if l.split(" ")[1][2] == 'x':
                o.write(l)
        f.close()
    o.close()

if __name__== "__main__":
    main()
