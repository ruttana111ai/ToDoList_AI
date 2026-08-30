tasks = []


def add_task():
    title = input("ชื่อเรื่อง: ").strip()
    description = input("รายละเอียด: ").strip()
    due_date = input("วันครบกำหนด (YYYY-MM-DD): ").strip()

    task = {
        "id": len(tasks) + 1,
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False,
    }

    tasks.append(task)
    print("เพิ่มงานเรียบร้อยแล้ว")


def view_tasks():
    if not tasks:
        print("ยังไม่มีงานในรายการ")
        return

    print("\n=== รายการงานทั้งหมด ===")
    for index, task in enumerate(tasks, start=1):
        status = "เสร็จแล้ว" if task["completed"] else "ยังไม่เสร็จ"
        print(f"{index}. {task['title']} | วันครบกำหนด: {task['due_date']} | สถานะ: {status}")


def edit_task():
    pass


def delete_task():
    pass


def main_menu():
    while True:
        print("\n=== To-Do List Menu ===")
        print("1. เพิ่มงานใหม่")
        print("2. ดูงานทั้งหมด")
        print("3. แก้ไขงาน")
        print("4. ลบงาน")
        print("5. ออกจากโปรแกรม")

        choice = input("เลือกเมนู: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            edit_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("ออกจากโปรแกรม")
            break
        else:
            print("เมนูไม่ถูกต้อง กรุณาเลือกใหม่")


if __name__ == "__main__":
    main_menu()

