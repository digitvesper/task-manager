# Задача: Создай класс `Task`, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач,
# отметки выполненных задач и вывода списка текущих (не выполненных) задач.

class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def print_task(self):
        status = "выполнено" if self.completed else "не выполнено"
        return f"Задача: {self.description}\nСрок выполнения: {self.deadline}\nСтатус: {status}"

class TaskManager:
    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_as_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_as_completed()
        else:
            print("Некорректный индекс задачи")

    def print_current_tasks(self):
        current_tasks = [task for task in self.tasks if not task.completed]
        if current_tasks:
            print("Текущие задачи:")
            for index, task in enumerate(current_tasks):
                print(f"{index + 1}. {task.print_task()}")
        else:
            print("Нет текущих задач")

# Пример использования класса Task и функций управления задачами
print("Привет\n")
task_manager = TaskManager()
print("Создали TaskManager")
# Добавление задач
task_manager.add_task(Task("Погулять с собакой", "10.04.2024"))
task_manager.add_task(Task("Сделать покупки", "12.04.2024"))
task_manager.add_task(Task("Закончить проект", "15.04.2024"))
print("Добавили три задачи")

task_manager.mark_task_as_completed(0)
print("Отметили нулевую задачу как выполненную")

task_manager.print_current_tasks()
