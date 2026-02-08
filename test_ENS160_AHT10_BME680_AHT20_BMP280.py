"""
    ENS160 + AHT10:
        SCL=Pin(9)
        SDA = Pin(8)
    
    BME680 :
        SDA=Pin(10)
        SCL=Pin(11)
    
    AHT20+BMP280:
        SDA=Pin(20)
        SCL=Pin(21)
    
"""
from machine import Pin, SoftI2C
from time import sleep
import network
from microdot import Microdot
import ens160, ahtx0, bme680, bmp280

from ahtx0 import AHT10, AHT20

i2c_ens_aht=SoftI2C(sda=Pin(10), scl=Pin(11), freq=100000)
senzor_ens=ens160.ENS160(i2c_ens_aht)
senzor_aht10=AHT10(i2c_ens_aht)


i2c_bme680=SoftI2C(sda=Pin(14), scl=Pin(15), freq=100000)
senzor_bme680=bme680.BME680_I2C(i2c_bme680)


i2c_aht_bmp=SoftI2C(sda=Pin(16), scl=Pin(17), freq=100000)
senzor_bmp280=bmp280.BMP280(i2c_aht_bmp, 0x77)
senzor_aht20=AHT20(i2c_aht_bmp, 0x38)


def conectare(nume, parola):
    ap_if=network.WLAN(network.AP_IF)
    ap_if.active(True)
    ap_if.config(essid=nume, password=parola)
    return ap_if.ifconfig()[0]

pagina="""
    <!doctype html>
    <meta http-equiv="refresh" content="10">
    <html>
        <head>
            <title> Titlu </title>
        </head>
        <body bgcolor="aqua">
            <br><br>
            <h1 align="center"> DATE SENZORI  {nume_senzor}</h1>
            <br><br><br><br><br><br><br><br><br>
            <h1 align="center"> ***** </h1>
            
            <h2 align="center">  ENS160 + AHT10 </h2> 
            <h2 align="center">  BME680 </h2> 
            <h2 align="center">  AHT20 + BMP280 </h2>
            
            <h1 align="center"> ***** </h1>
            
           <table align="center" width="50%" height="50%" border="1">
            <br><br><br><br><br>
            <br><br><br><br><br>  
            
            <tr bgcolor="LawnGreen">
                <td align="center"> <a href="/buton?v=1"><button> ENS160+AHT10 </button></a></td>
                <td align="center"><a href="/buton?v=2"><button> BME680 </button></a></td>
                <td align="center"><a href="/buton?v=3"><button> AHT20+BMP280 </button></a></td>
                <td align="center"><a href="/"><button> Pagina principala </button></a></td>
            </tr>
           
           </table>
        </body>
    </html>
    """


pagina_ens_aht="""
    <!doctype html>
    <meta http-equiv="refresh" content="10">
    <html>
        <head>
            <title> Titlu </title>
        </head>
        <body bgcolor="aqua">
            <h1 align="center"> Date senzor {nume_senzor}</h1> <br>
           <br><br><br><br><br>
            <table align="center" width="50%" height="50%" border="1" bgcolor="white">
            <tr>
                <td align="center"> Temperatura : {senzor_aht_temp}</td>
            </tr>
            <tr>
                <td align="center"> Umiditate : {senzor_aht_rel_humi}</td>
            </tr>
            <tr>
                <td align="center"> CO2 : {senzor_ens_eco2}</td>
            </tr>
            <tr>
                <td align="center"> TVOC : {senzor_ens_tvoc}</td>
            </tr>
            </table>
            <table align="center" width="50%" height="50%" border="1">
            <br><br><br><br><br><br><br><br><br><br><br>       
            <br><br><br><br><br><br><br><br><br><br><br><br><br>       
            
            <tr bgcolor="IndianRed">
                <td align="center"> <a href="/buton?v=1"><button> ENS160+AHT10 </button></a></td>
                <td align="center"><a href="/buton?v=2"><button> BME680 </button></a></td>
                <td align="center"><a href="/buton?v=3"><button> AHT20+BMP280 </button></a></td>
                <td align="center"><a href="/"><button> Pagina principala </button></a></td>
            </tr>
           
           </table>
        
        </body>
    </html>
    """

pagina_bme="""
    <!doctype html>
    <meta http-equiv="refresh" content="10">
    <html>
        <head>
            <title> Titlu </title>
        </head>
        <body bgcolor="aqua">
            <h1 align="center"> Date senzor {nume_senzor}</h1>
            <br><br><br><br><br> 
            <table align="center" width="50%" height="50%" border="1" bgcolor="white">
            <tr>
                <td align="center"> Temperatura : {bme_temp}</td>
            </tr>
            <tr>
                <td align="center"> Umiditate : {bme_humi}</td>
            </tr>
            <tr>
                <td align="center"> Presiune : {bme_press}</td>
            </tr>
            <tr>
                <td align="center"> Altitudine : {bme_alt}</td>
            </tr>
            <tr>
                <td align="center"> Gaz : {bme_gas}</td>
            </tr>
            </table>
            <table align="center" width="50%" height="50%" border="1">
            <br><br><br><br><br><br><br><br><br><br><br><br>       
            <br><br><br><br><br><br><br><br><br><br><br><br>    
            
            <tr bgcolor="LawnGreen">
                <td align="center"> <a href="/buton?v=1"><button> ENS160+AHT10 </button></a></td>
                <td align="center"><a href="/buton?v=2"><button> BME680 </button></a></td>
                <td align="center"><a href="/buton?v=3"><button> AHT20+BMP280 </button></a></td>
                <td align="center"><a href="/"><button> Pagina principala </button></a></td>
            </tr>
           
           </table>

        </body>
    </html>
    """


pagina_aht="""
    <!doctype html>
    <meta http-equiv="refresh" content="10">
    <html>
        <head>
            <title> Titlu </title>
        </head>
        <body bgcolor="aqua">
            <h1 align="center"> Date senzor {nume_senzor}</h1>
            <br><br><br><br><br>
            <table align="center" width="50%" height="50%" border="1" bgcolor="white">
            <tr bgcolor="blue">
                <td align="center"> <b> AHT20 </b></font></td>
            </tr>
            <tr>
                <td align="center"> Temperatura : {aht2_temp}</td>
            </tr>
            <tr>
                <td align="center"> Umiditate : {aht2_humi}</td>
            </tr>
            <tr>
                <td align="center" bgcolor="blue"> BMP280</td>
            </tr>
            <tr>
                <td align="center"> Temperatura : {bmp2_temp}</td>
            </tr>
            <tr>
                <td align="center"> Presiune : {bmp2_press}</td>
            </tr>
            </table>
             <table align="center" width="50%" height="50%" border="1">
            <br><br><br><br><br><br><br><br><br><br><br><br>        
            <br><br><br><br><br><br><br><br><br><br><br>  
            
            <tr bgcolor="yellow">
                <td align="center"> <a href="/buton?v=1"><button> ENS160+AHT10 </button></a></td>
                <td align="center"><a href="/buton?v=2"><button> BME680 </button></a></td>
                <td align="center"><a href="/buton?v=3"><button> AHT20+BMP280 </button></a></td>
                <td align="center"><a href="/"><button> Pagina principala </button></a></td>
            </tr>
           
           </table>
        </body>
    </html>
    """

def get_ENS160():
    tvoc=senzor_ens.get_tvoc()
    co2=senzor_ens.get_eco2()
    temp=senzor_aht10.temperature
    humi=senzor_aht10.relative_humidity
    return round(temp,2), round(humi,2), co2, tvoc
    

def get_BME680():
    return round(senzor_bme680.temperature,2), round(senzor_bme680.humidity,2), round(senzor_bme680.pressure,2), round(senzor_bme680.altitude,2), senzor_bme680.gas


def get_AHT():
    return round(senzor_aht20.temperature,2), round(senzor_aht20.relative_humidity,2), round(senzor_bmp280.temperature,2), round(senzor_bmp280.pressure,2)
    
    
app=Microdot()
ip_meu=conectare("WEB_SENZORI","12345678")
print("IP-ul de conectare la pagina = ",ip_meu)

@app.route('/')
def index(request):
    raspuns=pagina.format(nume_senzor="")
    return raspuns,{'Content-type':'text/html'}


"""
senzor_aht_temp
senzor_aht_rel_humi
senzor_ens_eco2
senzor_ens_tvoc

bme_temp=bme_temp, bme_humi=bme_humi, bme_press=bme_press, bme_alt=bme_alt, bme_gas=bme_gas


aht2_temp, aht2_humi, bmp2_temp, bmp2_press
aht2_temp=aht2_temp, aht2_humi=aht2_humi, bmp2_temp=bmp2_temp, bmp2_press=bmp2_press

"""


@app.route('/buton')
def index(request):
    valoare=int(request.args['v'])
    if valoare==1:
        senzor_aht_temp,senzor_aht_rel_humi,senzor_ens_eco2,senzor_ens_tvoc=get_ENS160()
        raspuns=pagina_ens_aht.format(nume_senzor="ENS160+AHT10", senzor_aht_temp=senzor_aht_temp,senzor_aht_rel_humi=senzor_aht_rel_humi,senzor_ens_eco2=senzor_ens_eco2,senzor_ens_tvoc=senzor_ens_tvoc)
        return raspuns,{'Content-type':'text/html'}
    elif valoare==2:
       bme_temp, bme_humi, bme_press, bme_alt, bme_gas=get_BME680()
       raspuns=pagina_bme.format(nume_senzor="BME680", bme_temp=bme_temp, bme_humi=bme_humi, bme_press=bme_press, bme_alt=bme_alt, bme_gas=bme_gas)
       return raspuns,{'Content-type':'text/html'}
    elif valoare==3:
        aht2_temp, aht2_humi, bmp2_temp, bmp2_press=get_AHT()
        raspuns=pagina_aht.format(nume_senzor="AHT20+BMP280",aht2_temp=aht2_temp, aht2_humi=aht2_humi, bmp2_temp=bmp2_temp, bmp2_press=bmp2_press)
        return raspuns,{'Content-type':'text/html'}
    else:
        pass
    
try:
    app.run(port=80)
except KeyboardInterrupt as err:
    print('Bye bye! ')
    app.shutdown()

