22 марта 2024 15:30 commit 3 Алексей Терехин - Изменена верстка базовой страницы
- Добавлена заглушка sidebar
- Добавлена заглушка хлебные крошки


22 марта 2024 15:30 commit 2 Алексей Терехин - Изменение поля для аутентификации на email
Изменения:
1. В приложение users добавлен сервис аутентификации через email - auth_for_email.py 
2. Изменена форма регистрации.
	- поле username заменено на email
	- добавлена проверка уникальности вводимого email
	- добавлена проверка что введенный email является почтовым ящиком АРМ ГС
	- поле email сделано обязательным для заполнения
3. В шаблонах аутентификации и регистрации изменено поле логин на почтовый ящик АРМ ГС


20 марта 2024 11:47 commit 1 Алексей Терехин - Добавление системы авторизации и регистрации пользователей
Изменения:
1. Создано новое приложение users.
	- Добавлено view RegisterView - для страницы с регистрацией
	- Переопределена базовая аутентификация пользователя. Теперь при входе авторизованного пользователя на страницу аутентификации будет редиректить на главную страницу
	- Джанговская система аутентификации подключена по маршруту localhost/accounts
2. Изменены настройки приложения settings.py:
	- убрана все требования к паролю
	- добавлена страница на которую редиректит после успешной аутентификации
	- изменен язык джанго на русский
	- изменен часовой пояс на Московский
3. Изменен базовый шаблон:
	- добавлена кнопка входа/выхода из аккаунта в главном меню





