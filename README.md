# Covid Assistant - CoAss

# TK PBP Django B03

## Anggota Kelompok B03:

- 2006482445	Zidan Amukti Rajendra
- 2006481953	Amanda Putri Khairunnisa
- 2006463843	Hilmi Al-biruni
- 2006464184	Karlina Rana Salsabila
- 2006485945	Raditya Hanif Yudha Prathama
- 2006464461	Muhammad Athif
- 2006481972	Danela Syafika Desideria

## Link HerokuApp
https://co-ass.herokuapp.com/

## Cerita Aplikasi

Aplikasi ini bernama Covid Assistant (CoAss) yang merupakan aplikasi reminder dan tracking untuk pasien yang terpapar Covid-19. Tujuan dari aplikasi ini sama seperti namanya yaitu asisten untuk para pejuang Covid-19 dan membantu mereka dalam progress penyembuhan. Latar belakang kami membuat aplikasi ini yaitu adanya salah satu anggota kelompok kami yang pernah terpapar virus Covid-19 dan menyadari pentingnya adanya rutinitas dan perekaman data secara teratur untuk melihat progress tiap harinya. Maka dari itu, kami membuat aplikasi ini untuk membantu para pasien Covid-19 dalam masa penyembuhan dengan track record yang terstruktur. Pada aplikasi ini, terdapat beberapa fitur, yaitu reminder atau pengingat untuk mengonsumsi obat dan aktivitas pendukung lainnya, seperti makan, minum, olahraga, berjemur, serta beristirahat. Selain itu, juga terdapat fitur catatan kesehatan yang meliputi derajat suhu tubuh, saturasi, denyut jantung, tensi, dan gula darah. Kemudian, aplikasi ini juga memiliki pencatatan tanggal, hasil, serta CT value dari test swab yang pernah dilakukan. Terakhir, aplikasi ini juga menyediakan fitur jurnal harian mengenai keluhan yang dirasakan tiap harinya.

## Daftar Modul

- Halaman signup dan login

Dev : Bersama


Pada halaman login, user diminta untuk mengisi username serta password yang telah terdaftar. Apabila user belum terdaftar, maka terdapat tombol signup yang berisi halaman untuk user mengisi username serta password pendaftaran.
- Halaman utama

Dev : Muhammad Athif

Menampilkan teks halaman awal yang berisi segala informasi mengenai Covid-19. Pada halaman ini juga menampilkan fitur-fitur yang terdapat pada aplikasi ini, tetapi user diwajibkan untuk login terlebih dahulu. Terdapat juga tombol login dan signup pada halaman ini.
- Reminder konsumsi obat

Dev : Hilmi Al Biruni

Halaman berisi tampilan jadwal konsumsi obat tiap harinya yang telah diinput. Terdapat juga tombol yang akan redirect ke halaman untuk menambahkan jadwal konsumsi obat, yang kemudian akan ditambilkan pada jadwal konsumsi obat pada halaman sebelumnya. Data yang diminta kepada user yaitu nama obat, waktu konsumsi, serta berapa lama (hari) user harus mengkonsumsi obat tersebut. Apabila waktu telah sesuai dengan waktu jadwal konsumsi obat, maka akan terdapat notifikasi atau reminder untuk mengingatkan user mengkonsumsi obat tersebut.
- Reminder istirahat & aktivitas lainnya (terdapat timer)

Dev : Danela Syafika Desideria

Halaman berisi tampilan jadwal aktivitas yang akan dilakukan user tiap harinya. Untuk memasukkan jadwal aktivitas tersebut, akan terdapat tombol yang akan redirect ke halaman untuk user memasukkan aktivitasnya. Data yang diminta kepada user yaitu nama aktivitas, waktu mengerjakannya, serta pilihan apakah aktivitas tersebut ingin di-timer selama durasi yang ditentukan atau tidak. Apabila waktu telah sesuai dengan waktu jadwal aktivitas, maka akan terdapat notifikasi atau reminder untuk mengingatkan user mengerjakan aktivitas tersebut. Jika aktivitas tersebut dipilih untuk menggunakan timer, maka pada waktu tersebut, user dapat menekan tombol start untuk memulai waktu untuk pengerjaan aktivitasnya, dan aplikasi akan menghitung mundur selama durasi yang ditentukan.
- Reminder dan catatan makan minum

Dev : Zidan Amukti Rajendra

Halaman berisi tampilan jadwal makan dan minum tiap harinya. Untuk memasukkan jadwal makan dan minum tersebut, akan terdapat tombol yang akan redirect ke halaman untuk user memasukkan jadwal makan dan minum tersebut. Data yang diminta kepada user yaitu kapan saja waktu makan tiap harinya. Apabila waktu telah sesuai dengan waktu jadwal makan dan minum, maka akan terdapat notifikasi atau reminder untuk mengingatkan user. Selain itu, terdapat juga halaman untuk me-track apakah user telah minum air yang cukup atau belum. Halaman tersebut akan menampilkan sebanyak apa air yang telah diminum oleh user. Setiap reminder untuk minum telah muncul, maka selanjutnya akan terdapat checkbox berapa banyak air yang telah diminum oleh user.
- Catatan kesehatan (suhu, saturasi & denyut jantung, tensi, darah)

Dev : Karlina Rana Salsabila

Halaman berisi tampilan berupa catatan kesehatan user tiap harinya. Untuk memasukkan catatan tersebut, akan terdapat tombol yang akan redirect ke halaman untuk user memasukkan data catatan kesehatan. User dapat memilih ingin mencatat data apa, antara suhu, saturasi & denyut jantung, tensi, serta darah. 
- Riwayat swab (tanggal, hasil, CT value (swab PCR))

Dev : Amanda Putri Khairunnisa

Halaman berisi tampilan berupa riwayat swab yang telah dilakukan oleh user. Untuk memasukkan riwayat tersebut, akan terdapat tombol yang akan redirect ke halaman untuk user memasukkan riwayat swab. Data yang diminta kepada user yaitu tanggal melakukan swab, hasil, serta CT value apabila user melakukan swab PCR.
- Jurnal harian (checkbox & textbox apa keluhan tiap harinya)

Dev : Raditya Hanif Yudha Prathama

Halaman berisi tampilan berupa jurnal harian yang mencatat keluhan yang dirasakan oleh user. Untuk memasukkan jurnal tersebut, akan terdapat tombol yang akan redirect ke halaman untuk user memasukkan segala keluhannya. Terdapat checkbox untuk keluhan-keluhan umum, seperti batuk, demam, pusing, dan lain-lain agar memudahkan user dengan hanya memilih keluhan tersebut. Terdapat juga textbox yang dapat diisi oleh user terkait detail keluhan ataupun keluhan lain yang dirasakan.

## Persona
https://docs.google.com/spreadsheets/d/1u75mStUk-715mEJxjCcKqRL3ftLZr0XDlg7FurLYzZU/edit?usp=sharing
