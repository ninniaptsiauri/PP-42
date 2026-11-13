class YoutubeChanel:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, user):
        self.subscribers.append(user)

    def upload_video(self, title):
        print(f"Video '{title}' uploaded.")

        for user in self.subscribers:
            user.notify(title)


class User:
    def __init__(self, name):
        self.name = name

    def notify(self, video_title):
        print(f"{self.name} received notification: "
              f"{video_title} uploaded")
        
chanel = YoutubeChanel()
user1 = User("John")
user2 = User("Jane")
chanel.subscribe(user1)
chanel.subscribe(user2)
chanel.upload_video("Python for beginners") 