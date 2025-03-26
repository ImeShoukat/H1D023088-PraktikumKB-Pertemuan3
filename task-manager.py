import random
import datetime

tasks = []

def add_task(name):
    estimated_time = random.randint(10, 120) 
    created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    task = {"name": name, "estimated_time": estimated_time, "created_at": created_at, "completed": False}
    tasks.append(task)
    print(f"Tugas '{name}' berhasil ditambahkan!")

def show_tasks():
    if not tasks:
        print("Belum ada tugas yang ditambahkan.")
        return
    print("\nDaftar Tugas:")
    for i, task in enumerate(tasks, 1):
        status = "✔ Selesai" if task["completed"] else "Belum selesai"
        print(f"{i}. {task['name']} - Estimasi {task['estimated_time']} menit - Ditambahkan {task['created_at']} - {status}")

def complete_task(index):
    if 1 <= index <= len(tasks):
        tasks[index - 1]["completed"] = True
        print(f"Tugas '{tasks[index - 1]['name']}' telah diselesaikan!")
    else:
        print("Nomor tugas tidak valid!")

def main():
    while True:
        print("\nMenu:")
        print("1. Tambah Tugas")
        print("2. Lihat Tugas")
        print("3. Tandai Selesai")
        print("4. Keluar")
        choice = input("Pilih menu (1-4): ")
        
        if choice == "1":
            name = input("Masukkan nama tugas: ")
            add_task(name)
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            show_tasks()
            index = int(input("Masukkan nomor tugas yang telah selesai: "))
            complete_task(index)
        elif choice == "4":
            print("Terima kasih, sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid, coba lagi!")

if __name__ == "__main__":
    main()
