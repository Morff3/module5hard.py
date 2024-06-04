import time


class UrTube:
    USERS = []
    VIDEOS = []
    CURRENT_USER = None

    def log_in(self, login, password):
        for user in self.USERS:
            if login == user.nickname and password == user.password:
                self.CURRENT_USER = user

    def register(self, nickname, password, age):
        for user in self.USERS:
            if nickname in user.nickname:
                print(f"Пользователь {nickname} уже существует")
                break
        else:
            user = User(nickname, password, age)
            self.USERS.append(user)
            self.log_out()
            self.log_in(user.nickname, user.password)

    def log_out(self):
        self.CURRENT_USER = None

    def add(self, *args):
        for movie in args:
            self.VIDEOS.append(movie)

    def get_videos(self, world):
        list_video = []
        for roll in self.VIDEOS:
            if world.lower() in roll.title.lower():
                list_video.append(roll.title)
        return list_video

    def watch_video(self, movie):

        if self.CURRENT_USER and self.CURRENT_USER.age < 18:
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
        elif self.CURRENT_USER:
            for roll in self.VIDEOS:
                if movie in roll.title:
                    for i in range(1, 11):
                        print(i, end=' ')
                        time.sleep(1)
                    print('Конец видео')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')


class Video:

    def __init__(self, title, duration, time_now: int = 0, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class User:

    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __hash__(self):
        return hash(self.password)


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
print(ur.CURRENT_USER)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
