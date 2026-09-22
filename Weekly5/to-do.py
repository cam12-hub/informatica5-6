def main():
  tasks = [] #Empty list
  command = ""
  completed = []
  while True:
    print(f"Tasks to do: {len(tasks)}")
    print(tasks)
    command = input("What do you want to do? (add, complete, exit): " ).capitalize().strip()
    if command == "Exit":
      break
    elif command == "Add":
      new_task = input("Enter new task: ")
      tasks.append(new_task)
    elif command == "Complete":
      task_completed = input("Enter task completed: ")
      tasks.remove(task_completed)
      print("Task completed")
      completed.append(task_completed)
      print(completed)


if __name__=="__main__":
  main()
