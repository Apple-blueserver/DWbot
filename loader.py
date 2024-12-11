# run_multiple_bots.py
import subprocess

if __name__ == "__main__":
    bot_files = ['ไฟล์ที่1.py', 'ไฟล์ที่2.py'] # ชื่อไฟล์ (เพิ่มได้)

    processes = []
    for bot_file in bot_files:
        process = subprocess.Popen(['python', bot_file])
        processes.append(process)

    for process in processes:
        process.wait()
