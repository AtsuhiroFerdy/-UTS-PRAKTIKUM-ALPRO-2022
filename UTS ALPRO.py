from selenium import webdriver
import time
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


def GUI():
    # WINDOW
    window = tk.Tk()
    window.configure(bg='grey')
    window.geometry('400x400')
    window.resizable(False, False)
    window.title('UTS ALPRO')

    # FRAME
    frame = ttk.Frame(window)
    frame.pack(padx=10, pady=10, fill='x', expand=True)

    # LINK
    label = ttk.Label(frame, text='Masukkan Link')
    label.pack(padx=10, fill='x', expand=True)

    link = tk.StringVar()
    input_link = ttk.Entry(frame, textvariable=link)
    input_link.pack(padx=10, pady=5, fill='x', expand=True)

    # LOOP
    label_2 = ttk.Label(frame, text='Masukkan Loop')
    label_2.pack(padx=10, fill='x', expand=True)

    loop = tk.IntVar()
    input_loop = ttk.Entry(frame, textvariable=loop)
    input_loop.pack(padx=10, pady=5, fill='x', expand=True)

    def UTS_alpro():

        # Driver, URL, Looping
        lokasi_driver = 'C:/Users/THINKPAD X1 CARBON/Documents/ChromeDriver/106.0.5249.61/chromedriver.exe'
        link_web = link.get()
        looping = loop.get()
        # Data yang mau dimasukkan
        nama = 'M. Raihan Ferdyansyah'
        nim = '4332201036'
        x = 'xpath'
        list_xpath = [
            # kelas 1
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[1]/div[1]/span',
            # kelas 2
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[2]/div[4]/span',
            # nama
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input',
            # nim
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input',
            # skor
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div',
            # kirim
            '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span',
        ]

        if link_web in ['https://forms.gle/gUNAfgqb7znZCLCFA', 'https://docs.google.com/forms/d/e/1FAIpQLSdVf6DHW92lAzgTboffTNg43VLcbTKah46iafNfiXML46sfRw/viewform']:
            # Mengakses letak web driver yang sudah didownload
            driver = webdriver.Chrome(lokasi_driver)
            for i in range(1+looping):
                # Mengakses URL yang ingin dibuka web driver
                driver.get(link_web)
                time.sleep(1)

                # Memilih kelas di form
                input_kelas = driver.find_element(x, list_xpath[0]).click()
                time.sleep(1)
                input_kelas_2 = driver.find_element(x, list_xpath[1]).click()
                time.sleep(1)

                # Mengisi nama di form
                input_nama = driver.find_element(
                    x, list_xpath[2]).send_keys(nama)
                time.sleep(1)

                # Mengisi nim di form
                input_nim = driver.find_element(
                    x, list_xpath[3]).send_keys(nim)
                time.sleep(1)

                # Skor nilai
                tombol_nilai = driver.find_element(x, list_xpath[4]).click()
                time.sleep(1)

                # Kirim
                tombol_kirim = driver.find_element(x, list_xpath[5]).click()
                time.sleep(1)

            driver.quit()
            pesan = 'Berhasil Mengirim\nUTS Alpro Selesai'
            showinfo(title='Pemberitahuan!', message=pesan)
            window.quit()

        elif link_web == '' and looping in range(0, 100):
            driver = False
            showinfo(title='Pemberitahuan!', message='Harap Masukkan Link')

        else:
            driver = False

    # TOMBOL START & Quit
    tombol = ttk.Button(frame, text='Start', command=UTS_alpro).pack(
        padx=100, pady=1, fill='x', expand=True)
    tombol_2 = ttk.Button(frame, text="Quit", command=window.quit).pack(
        padx=100, pady=1, fill='x', expand=True)

    window.mainloop()


GUI()
