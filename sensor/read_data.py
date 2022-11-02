# 1. import arduinoMega nya ke python melalui pyfirmata caranya lihat dibwh
from pyfirmata import ArduinoMega
# 2. apabila menggunakan yang analog maka tambah sebagai berikut
# untuk langkah 1 dan 2 pilih salah 1 saja.
from pyfirmata import ArduinoMega, util
# 3. import waktu untuk melakukan delay yaitu import time caranya sebagai berikut
import time

# 4. definisikan arduino nya ke dalam variabel, berikut ini arduino di masukkan ke dalam variabel "board"
#    untuk isi dalam kurung arduinoMega merupakan port yang digunakan di arduino
board = ArduinoMega("COM4")
# 5. Definisikan pin yang disambungkan ke dalam variabel dan variabel yang digunakan adalah "pin", 
# contoh dibawah ini
# board itu bertanda kita menggunakan pin dari si arduino yang kita definisikan
# "get_pin merupakan cara untuk kita mengakses si pin di arduino"
# untuk isi di dalam () adalah :
# ("(ini diisikan dengan a yang bermakna analog atau d yang bermakna digital):(ini merupakan angka pin
# pada arduino yang kita gunakan):(diisikan dengan 
# "i" yang merupakan input = pc menerima data 
#                    atau
# "o" yang merupakan ouput = pc memberi data)")
pin = board.get_pin("a:1:i")

# 6. Koding dibawah ini wajib apabila menggunakan sensor analog yang dimasukkan kedalam variabel bebas 
# untuk contoh dibawah digunakan variabel "it"
it = util.Iterator(board)
it.start()

# 7. kemudian membuat loop untuk menjalan arduino nya dan didalam ini bisa dimasukkan rumus yang 
#    diperlukan untuk mendapatkan hasil
while True:
    # 8. pembacaan input dari sensor dan dimasukkan ke variabel dan dibwh ini diberikan nama "sensor"
    #    read() berfungsi untuk membaca data dari sensor
    sensor = pin.read()
    # 9. untuk menampilkan angka yang didapat di cmd
    print(sensor)
    # 10. membuat jeda atau delay ketika bekerja yaitu dengan cara dibawah ini dan untuk dalam kurungannya 
    #     merupakan detik yang diperlukan
    time.sleep(1)


