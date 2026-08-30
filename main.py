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


def update_task():
    if not tasks:
        print("ยังไม่มีงานในรายการ")
        return

    view_tasks()

    try:
        index = int(input("เลือกลำดับงานที่ต้องการแก้ไข: "))
    except ValueError:
        print("กรุณาใส่ตัวเลขที่ถูกต้อง")
        return

    if index < 1 or index > len(tasks):
        print("ลำดับงานไม่ถูกต้อง")
        return

    task = tasks[index - 1]

    print("\nเลือกฟิลด์ที่ต้องการแก้ไข:")
    print("1. ชื่อเรื่อง")
    print("2. รายละเอียด")
    print("3. สถานะ")
    field = input("เลือก: ").strip()

    if field == "1":
        new_title = input("ชื่อเรื่องใหม่: ").strip()
        if not new_title:
            print("ชื่อเรื่องไม่สามารถเว้นว่างได้")
            return
        task["title"] = new_title
        print("แก้ไขชื่อเรื่องเรียบร้อยแล้ว")

    elif field == "2":
        new_description = input("รายละเอียดใหม่: ").strip()
        if not new_description:
            print("รายละเอียดไม่สามารถเว้นว่างได้")
            return
        task["description"] = new_description
        print("แก้ไขรายละเอียดเรียบร้อยแล้ว")

    elif field == "3":
        status_choice = input("ระบุสถานะ (1 = เสร็จแล้ว, 0 = ยังไม่เสร็จ): ").strip()
        if status_choice == "1":
            task["completed"] = True
            print("เปลี่ยนสถานะเป็น เสร็จแล้ว")
        elif status_choice == "0":
            task["completed"] = False
            print("เปลี่ยนสถานะเป็น ยังไม่เสร็จ")
        else:
            print("ตัวเลือกสถานะไม่ถูกต้อง")

    else:
        print("ตัวเลือกฟิลด์ไม่ถูกต้อง")


def edit_task():
    update_task()


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
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("ออกจากโปรแกรม")
            break
        else:
            print("เมนูไม่ถูกต้อง กรุณาเลือกใหม่")


if __name__ == "__main__":
    main_menu()

