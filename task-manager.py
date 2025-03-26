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
        print("Ga ada tugas nih.")
        return
    print("\nDaftar Tugas:")
    for i, task in enumerate(tasks, 1):
        status = "Bagus, ga deadlineders" if task["completed"] else "Belum selesai nih, ayo dikerjain dulu"
        print(f"{i}. {task['name']} - Estimasi {task['estimated_time']} menit - Ditambahkan {task['created_at']} - {status}")

def complete_task(index):
    if 1 <= index <= len(tasks):
        tasks[index - 1]["completed"] = True
        print(f"Keren, tugas '{tasks[index - 1]['name']}' udah kamu selesein!")
    else:
        print("salah masukin nomor kayanya kamu")

def main():
    while True:
        print("\nMenu:")
        print("1. Tambah Tugas")
        print("2. Lihat Tugas")
        print("3. Tandai Selesai")
        print("4. Keluar")
        choice = input("Pilih menu (1-4): ")
        
        if choice == "1":
            name = input("Ada tugas apa nih kamu: ")
            add_task(name)
        elif choice == "2":
            show_tasks()
            print("\ngagean digarap yang belum")
        elif choice == "3":
            show_tasks()
            index = int(input("\nkewren kamu, tugas apa tu yg kelar: "))
            complete_task(index)
            print("\ncie nambah 1 yang kelar, digarap juga yang lain")
        elif choice == "4":
            print("okoklah, ciao dan jangan jadi deadlineders!")
            break
        else:
            print("Opsi yang kamu pilih ga ada, coba lagi!")

if __name__ == "__main__":
    main()
