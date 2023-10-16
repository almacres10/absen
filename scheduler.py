from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess

# Buat objek scheduler
scheduler = BlockingScheduler()

# Fungsi untuk menjalankan absen.py
def run_absen():
    subprocess.run(["python", "absen.py"])

# Jadwal penjadwalan: Setiap jam 7 pagi dan jam 7 malam
scheduler.add_job(run_absen, 'cron', hour=8, minute=25, second=0)
scheduler.add_job(run_absen, 'cron', hour=20, minute=17, second=0)

# Jalankan scheduler
scheduler.start()