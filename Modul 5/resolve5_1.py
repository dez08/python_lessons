# Дополнительное практическое задание по модулю: "Классы и объекты."

class UrTube:

    def __init__(self):
        self.users = {}
        self.videos = []
        self.current_user = None

    def log_in(self, login, password):
        if login in self.users:
            get_pass = self.users.get(login)[0]
            if hash(password) == get_pass:
                self.current_user = login

    def register(self, nickname, password, age):
        if nickname in self.users:
            print(f'Пользователь с {nickname} уже существует.')
        else:
            self.users[nickname] = [hash(password), age]
            self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        if args[0] not in self.videos:
            self.videos = [args]

    def get_videos(self, words):
        same_video = []
        for obj in self.videos:
            for i in obj:
                if words.lower() in i.title.lower():
                    same_video.append(i.title)
        return same_video

    def watch_video(self, title):
        if self.current_user == None:
            print('Войдите в аккаунт чтобы смотреть видео.')
        else:
            for obj in self.videos:
                for i in obj:
                    if title == i.title:
                        if i.adult_mode == True:
                            get_age = self.users.get(self.current_user)[1]
                            if get_age < 18:
                                print('Вам нет 18 лет, пожалуйста покиньте страницу.')
                            else:
                                for j in range(1, i.duration + 1):
                                    print(j, ' ',  end='')
                                    import time
                                    time.sleep(1)
                                print('Конец видео')


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
