class Task:
    def __init__(self, title: str, description: str, due_date: str, status: str):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

task = Task('Make Invitations', 'Doing the design of invitations and print 100 copies', '12.11.2025', 'undone')
task.description



from typing import List

class Task:
    def __init__(self, title: str, description: str, due_date: str, status: str = 'undone'):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def mark_complete(self):
        self.status = 'done'
        return f'The status changed from undone to done. The task name is {self.title}.'

class todolist:
     
    def __init__(self):
        self.tasks: List[Task] = []
        
    def add_task(self, task: Task):
        self.tasks.append(task)
        print(f" Task '{task.title}' added!")

    def show_list(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("\n All tasks:")
            for task in self.tasks:
                print(f" - {task}")

    def show_undone(self):
        undone = [task for task in self.tasks if task.status == "undone"]
        if not undone:
            print(" All tasks are done!")
        else:
            print("\nundone tasks:")
            for task in undone:
                print(f" - {task}")



from typing import List

class Task:
    def __init__(self, title: str, description: str, due_date: str, status: str = 'undone'):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def mark_complete(self):
        self.status = 'done'
        return f"✅ The status changed from undone to done. Task: {self.title}"

    def __str__(self):
        return f"{self.title} — {self.description} (Due: {self.due_date}, Status: {self.status})"


class ToDoList:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        self.tasks.append(task)
        print(f"🟢 Task '{task.title}' added!")

    def show_list(self):
        if not self.tasks:
            print("📭 No tasks in the list.")
        else:
            print("\n📋 All Tasks:")
            for task in self.tasks:
                print(f" - {task}")

    def change_status(self, title: str):
        for task in self.tasks:
            if task.title == title:
                print(task.mark_complete())
                return
        print(f"⚠️ Task '{title}' not found.")

    def show_incomplete(self):
        incomplete = [task for task in self.tasks if task.status == 'undone']
        if not incomplete:
            print("🎉 All tasks are complete!")
        else:
            print("\n⏳ Incomplete Tasks:")
            for task in incomplete:
                print(f" - {task}")



todo = ToDoList()

todo.add_task(Task("Сделать ДЗ", "Математика, стр. 45", "2025-10-29"))
todo.add_task(Task("Купить продукты", "Хлеб, молоко, сыр", "2025-10-28"))
todo.add_task(Task("Позвонить маме", "Узнать про поездку", "2025-10-30"))
todo.add_task(Task("Прибрать комнату", "Убрать одежду и пыль", "2025-10-31"))
todo.add_task(Task("Прочитать книгу", "Глава 5 из романа", "2025-11-01"))

todo.show_list()

todo.change_status("Купить продукты")

todo.show_incomplete()



from typing import List

class Post:
    def __init__(self, title: str, content: str, author: str):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"📖 {self.title} — by {self.author}\n   {self.content}"


class Blog:
    def __init__(self):
        self.posts: List[Post] = []

    def add_post(self, post: Post):
        self.posts.append(post)
        print(f"✅ Post added! Title: '{post.title}'")

    def show_all_posts(self):
        if not self.posts:
            print("📭 No posts yet.")
        else:
            print("\n📰 All posts:")
            for post in self.posts:
                print(post)

    def author_posts(self, author_name: str):
        author_posts = [post for post in self.posts if post.author == author_name]
        if not author_posts:
            print(f"⚠️ No posts found by author '{author_name}'.")
        else:
            print(f"\n✍️ Posts by {author_name}:")
            for post in author_posts:
                print(post)

    def delete_post(self, title: str):
        for post in self.posts:
            if post.title == title:
                self.posts.remove(post)
                print(f"🗑️ Post '{title}' deleted.")
                return
        print(f"⚠️ Post '{title}' not found.")

    def edit_post(self, title: str, new_content: str):
        for post in self.posts:
            if post.title == title:
                old_content = post.content
                post.content = new_content
                print(f"✏️ Post '{title}' updated.\nOld content: {old_content}\nNew content: {new_content}")
                return
        print(f"⚠️ Post '{title}' not found.")

    def show_latest_posts(self, count: int = 3):
        if not self.posts:
            print("📭 No posts available.")
        else:
            print(f"\n🕓 Latest {count} posts:")
            for post in self.posts[-count:]:
                print(post)

blog = Blog()

blog.add_post(Post("Мой первый пост", "Сегодня я учусь Python!", "Иван"))
blog.add_post(Post("Путешествие", "Поездка в горы была супер!", "Анна"))
blog.add_post(Post("Советы по коду", "Не бойся ошибок — они учат!", "Иван"))
blog.add_post(Post("Рецепт дня", "Пробую новый торт с клубникой.", "Анна"))
blog.add_post(Post("Новости", "Я начинаю вести блог!", "Иван"))

blog.show_all_posts()

blog.author_posts("Иван")

blog.delete_post("Рецепт дня")

blog.edit_post("Путешествие", "Теперь я хочу поехать к морю!")

blog.show_latest_posts(3)




from typing import List

class Account:
    def __init__(self, account_no: int, holder: str, balance: int):
        self.account_no = account_no
        self.holder = holder
        self.balance = balance
    
    def __str__(self):
        return f'{self.account_no}, {self.holder}, {self.balance}'


class Management:
    def __init__(self):
        self.accounts: List[Account] = []

    def add_account(self, account: Account):
        self.accounts.append(account)
        print(f'your account added {account.account_no}')

    def show_all(self):
        if not self.accounts:
            print('No accounts here yet')
        else:
            print('this all accounts with info')
            for account in self.accounts:
                print(account)

    def check_balance(self, account_no: int):
        found = False
        for account in self.accounts:
            if account.account_no == account_no:
                print(f'Your balance is {account.balance}')
                found = True
                break
        if not found:
            print('Your account can not be find')

    def deposit(self, account_no: int, amount: int):
        for account in self.accounts:
            if account.account_no == account_no:
                account.balance += amount
                print(f'You added {amount}. Now your balance is {account.balance}')
                return
        print('Your account can not be find')

    def withdraw(self, account_no: int, amount: int):
        for account in self.accounts:
            if account.account_no == account_no:
                if account.balance >= amount:
                    account.balance -= amount
                    print(f'You withdrew {amount}. Now your balance is {account.balance}')
                else:
                    print('Not enough money in your balance')
                return
        print('Your account can not be find')

    def transfer(self, from_acc: int, to_acc: int, amount: int):
        sender = None
        receiver = None

        for account in self.accounts:
            if account.account_no == from_acc:
                sender = account
            elif account.account_no == to_acc:
                receiver = account

        if sender and receiver:
            if sender.balance >= amount:
                sender.balance -= amount
                receiver.balance += amount
                print(f'You transferred {amount} from {sender.holder} to {receiver.holder}')
                print(f'Your new balance is {sender.balance}')
            else:
                print('Not enough money to transfer')
        else:
            print('One of the accounts can not be find')











































