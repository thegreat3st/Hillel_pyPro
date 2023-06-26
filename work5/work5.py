from dataclasses import dataclass
import uuid
from abc import ABC, abstractmethod
import time

@dataclass
class User: #like channel, private or personal acc
    id_: int
    name: str
    surname: str
    age: int
    
@dataclass
class Post: 
    id_: int
    channel: str
    photo: int # amount of photos on the post
    message: str
    
    def __str__ (self) :
        return f"Post: {self.channel}: {self.message}"
    
class SocialChannel(ABC):
    
    @abstractmethod
    def authorize(self, user: User):
        """Authorize to soc media."""
    @abstractmethod
    def checkout (self, post: Post):
        """Payment entrypoint."""
    @property
    @abstractmethod
    def status(self): # if photo uploaded or not
        """Represents the status of a checkout.""" 
    @property
    @abstractmethod
    def process_schedule():
        """Represents the time.""" 
        
    @staticmethod
    def photo_amount():
        PHOTO_AM = int(input("How many photos to upload?\n"))
        return PHOTO_AM 
    @staticmethod
    def your_channel():
        channel = str(input("Name of yr channel?\n"))
        return channel   
    @staticmethod
    def your_id(id_):
        if main:
            id_ += i
        return id_
        
class post_to_youtube(SocialChannel):

    def get_channel(self, channel: str):
        print (f"\nAuthorizing on youtube with {channel}")
        
    def get_message(self, message: str):
        print(f"Your comment is: {message}")
        
    def _send_callback_api (self, token: str):
        print (f"Token for youtube: {token}")
    def _get_token (self, user: User):
        return uuid.uuid3(uuid.NAMESPACE_DNS, str(user.id_))
    
    def authorize (self, user: User) -> bool:
        token = self._get_token(user)
        self._send_callback_api(token)
        return True
    
    def checkout (self, post: Post, PHOTO_AM: int, channel: str, id_: int):
        self.ma_status = True
        post.photo = PHOTO_AM
        post.channel = channel
        post.id_ = id_
        print(f"Checking out the {post =}")
    
    @property
    def status (self):
        time.sleep(5)
        if getattr(self, "ma_status", False):
            return "SUCCESS"
        return "FAILED"
    @property
    def process_schedule(self):
        curr = time.time()
        timestamp = time.ctime(curr)
        print(f"Posted at", timestamp) 
    
class post_to_facebook(SocialChannel):

    def get_channel(self, channel: str):
        print (f"\nAuthorizing on facebook with {channel}")
        
    def get_message(self, message: str):
        print(f"Your comment is: {message}")
        
    def _send_callback_api (self, token: str):
        print (f"Token for facebook: {token}")
    def _get_token (self, user: User):
        return uuid.uuid3(uuid.NAMESPACE_DNS, str(user.id_))
    
    def authorize (self, user: User) -> bool:
        token = self._get_token(user)
        self._send_callback_api(token)
        return True
    
    def checkout (self, post: Post, PHOTO_AM: int, channel: str, id_: int):
        self.ma_status = True
        post.photo = PHOTO_AM
        post.channel = channel
        post.id_ = id_
        print(f"Checking out the {post=}")
    
    @property
    def status (self):
        time.sleep(5)
        if getattr(self, "ma_status", False):
            return "SUCCESS"
        return "FAILED"
    @property
    def process_schedule(self):
        curr = time.time()
        timestamp = time.ctime(curr)
        print(f"Posted at", timestamp) 
    
class post_to_twitter(SocialChannel):

    def get_channel(self, channel: str):
        print (f"\nAuthorizing on twitter with {channel}")
        
    def get_message(self, message: str):
        print(f"Your comment is: {message}")
        
    def _send_callback_api (self, token: str):
        print (f"Token for twitter: {token}")
    def _get_token (self, user: User):
        return uuid.uuid3(uuid.NAMESPACE_DNS, str(user.id_))
    
    def authorize (self, user: User) -> bool:
        token = self._get_token(user)
        self._send_callback_api(token)
        return True
    
    def checkout (self, post: Post, PHOTO_AM: int, channel: str, id_: int):
        self.ma_status = True
        post.photo = PHOTO_AM
        post.channel = channel
        post.id_ = id_
        print(f"Checking out the {post=}")
    
    @property
    def status(self):
        time.sleep(5)
        if getattr(self, "ma_status", False):
            return "SUCCESS"
        return "FAILED"
    @property
    def process_schedule(self):
        curr = time.time()
        timestamp = time.ctime(curr)
        print(f"Posted at", timestamp) 

class UploadingProcessor:
    def __init__(self, soc_media: SocialChannel):
        self._soc_media = soc_media 
    def checkout(self, user: User, post: Post, PHOTO_AM: int, channel: str, id_: int):
        self._soc_media.get_channel(channel)
        self._soc_media.authorize(user)
        self._soc_media.checkout(post, PHOTO_AM, channel, id_)
    def get_status(self):
        return self._soc_media.status
    def get_process_schedule(self):
        self._soc_media.process_schedule
        
def main():
    PHOTO_AM: SocialChannel = SocialChannel.photo_amount()
    channel: SocialChannel = SocialChannel.your_channel()
    id_: SocialChannel = SocialChannel.your_id(0)
    
    john = User(id_= 1, name = "John", surname = "Doe", age = 16)
    mapost = Post(id_ = id_, channel = channel, photo = PHOTO_AM, message = "Ma best post!")

    type = "facebook"
    if type == "youtube":
        soc_media = post_to_youtube()
    elif type == "facebook":
        soc_media = post_to_facebook()
    elif type == "twitter":
        soc_media = post_to_twitter()
    
    upl_processor = UploadingProcessor(soc_media)
    upl_processor.checkout(john, mapost, PHOTO_AM, channel, id_)
    status = upl_processor.get_status()
    upl_processor.get_process_schedule()
    print(status)
    
    
for i in range(3):
    if __name__ == "__main__":
        main()
        SocialChannel.your_id(0)
    
