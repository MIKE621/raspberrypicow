import network
from time import sleep


class WifiConnect():
    def connect():
        try:
            wifi = network.WLAN(network.STA_IF)
            wifi.active(True)
            wifi.connect('NAMESSID', 'PASSWORD')
            while wifi.isconnected() == False:
                print('Wifi esta esperando conexión...')
                sleep(1)
            
            ip = wifi.ifconfig()[0]
            print(f'Wifi conexión establecida! IP:{ip}')
            return True
        except:
            print('Algo anda mal!')
            return False
            
            
    def wifiscan():
        try:
            wifi = network.WLAN(network.STA_IF)
            wifi.active(True)
            nets = wifi.scan()
            print('Lista de señales detectadas:')
            for router in nets:
                print('SSID:'+ str(router[0]))
        except:
            print('Algo anda mal!')
        
            
#try:
#    WifiConnect.connect('CLARO_9Wj2hd', 'fuentesgomez2022')
#except keyboardinterrupt:
#    machine.reset()
