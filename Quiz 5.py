import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Definisikan model pertumbuhan pengguna ponsel
def phone_user_growth(Users, time, growth_rate, saturation_point):
    dUsers_dt = growth_rate * Users * (1 - Users / saturation_point)
    return dUsers_dt

# Rentang waktu simulasi (tahun)
time_span = np.linspace(0, 5, 61)  # 5 tahun (2019-2024) dengan interval 0,1 tahun

# Parameter
initial_users = 10e6  # Jumlah awal pengguna (10 juta pada tahun 2019)
growth_rate = 0.35    # Laju pertumbuhan per tahun
saturation_point = 100e6  # Titik jenuh, jumlah maksimum pengguna (100 juta)

# Menyelesaikan ODE
Users = odeint(phone_user_growth, initial_users, time_span, args=(growth_rate, saturation_point))

# Konversi jumlah pengguna ke bilangan bulat
Users = Users.astype(int)

# Menampilkan hasil dalam grafik
plt.figure()
plt.plot(time_span + 2019, Users, 'b-', linewidth=2, label='Pengguna Ponsel')
plt.xlabel('Tahun')
plt.ylabel('Jumlah Pengguna')
plt.title('Proyeksi Pertumbuhan Pengguna Ponsel di Indonesia (2019-2024)')
plt.legend(loc='best')
plt.grid()
plt.show()