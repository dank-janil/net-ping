import pyping
import ipaddress
import multiprocessing


def scan_worker(ip):
    try:
        s = pyping.ping(str(ip))
    except ZeroDivisionError:
        return

    if s.ret_code == 0:
        print '> %s Aktif' %ip
        return
    else:
        return

def scan_multi(network_with_subnet):
    try:
        network = ipaddress.ip_network(unicode(str(network_with_subnet), "utf-8"))
    except ValueError:
        print("Network atau subnet tidak valid")
        exit()
    jobs = []
    print ("Total Host & Proses : " + str(len(list(network.hosts()))) + "/" + str(len(list(network.hosts()))))
    print("===============================================")
    for ip in network.hosts():
        p = multiprocessing.Process(target=scan_worker,args=(ip,))
        jobs.append(p)
        p.start()
