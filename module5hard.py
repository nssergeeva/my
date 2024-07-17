from time import sleep
class User:
    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title: str, duration: int, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __eq__(self, other):
        return self.title == other.title

    def __contains__(self, item):  # item - string
        return item in self.title  # 'aa' in 'aannn'


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_out(self):
        self.current_user = None

    def log_in(self, nickname: str, password: int):
        for user in self.users:
            if nickname == user.nickname and password == user.password:
                self.current_user = user
                return

    def register(self, nickname: str, password: int, age: int):
        password = hash(password)
        for user in self.users:
            if nickname == user.nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f"Пользователь {nickname} зарегистрирован и вошел в систему.")

    def add(self, *args):  # args - tuple, внутри которого лежат Video
        for movie in args:  # movie это объект класса Video
            if movie.title not in [video.title for video in self.videos]:
                self.videos.append(movie)

    def get_videos(self, text: str):
        list_movie = []
        for video in self.videos:
            if text.upper() in video.title.upper():
                list_movie.append(video.title)
        return list_movie

    def watch_video(self, title):
        if self.current_user == None:
            print("Войдите в аккаунт чтобы смотреть видео")
            return
        for i in self.videos:
            if title == i.title:
                if i.adult_mode == True:
                    if self.current_user.age < 18:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
                        break
                for t in range(1, i.duration + 1):
                    sleep(1)
                    print(t, end=' ')
                    i.time_now += 1
                print("Конец видео")
                i.time_now = 0
                break


if __name__ == '__main__':
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
ur.register('vasya_pupkin', 'IDOPWE999', 10)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'EGFHI6UHEIUHF', 20)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'efjoijoEIjr3', 40)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')