# https://leetcode.com/problems/design-twitter/description/


class User:
    def __init__(self, userId) -> None:
        self.userId = userId
        self.followers = set()
        self.following = set()

    def add_follower(self, user_id):
        self.followers.add(user_id)

    def remove_follower(self, user_id):
        if user_id in self.followers:
            self.followers.remove(user_id)

    def follow(self, user_id):
        self.following.add(user_id)

    def unfollow(self, user_id):
        if user_id in self.following:
            self.following.remove(user_id)

    def is_following(self, user_id):
        a = user_id == self.userId
        b = user_id in self.following
        return a or b

    def __repr__(self) -> str:
        return str(self)
    
    def __str__(self) -> str:
        return f'({self.userId})'


class Twitter:
    def __init__(self):
        self.users = {}
        self.tweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.create_user_if_not_exists(userId)

        tweet = (userId,tweetId)
        self.tweets.append(tweet)
        

    def getNewsFeed(self, userId: int) -> list[int]:
        self.create_user_if_not_exists(userId)

        count = min(10, len(self.tweets))
        user = self.users[userId]

        feed = []
        for idx in range(len(self.tweets)-1, -1, -1):
            tweet_user_id, tweet_id = self.tweets[idx]
            if user.is_following(tweet_user_id):
                feed.append(tweet_id)
            
            if len(feed) == 10:
                break

        return feed


    def follow(self, followerId: int, followeeId: int) -> None:
        self.create_user_if_not_exists(followerId)
        self.create_user_if_not_exists(followeeId)

        follower = self.users[followerId]
        followee = self.users[followeeId]

        follower.follow(followeeId)
        followee.add_follower(followerId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            return
        if followeeId not in self.users:
            return

        follower = self.users[followerId]
        followee = self.users[followeeId]
        
        follower.unfollow(followeeId)
        followee.remove_follower(followerId)


    def create_user_if_not_exists(self, userId):
        if userId not in self.users:
            self.users[userId] = User(userId)


sol = Twitter()
sol.postTweet(1, 4)
sol.postTweet(2, 5)
sol.unfollow(1, 2)
print(sol.getNewsFeed(1))