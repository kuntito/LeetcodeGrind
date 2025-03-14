# https://leetcode.com/problems/design-twitter/description/
import heapq


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
        self.count = 0



    def postTweet(self, userId: int, tweetId: int) -> None:
        self.create_user_if_not_exists(userId)

        self.count += 1
        tweet = (
            -1 * self.count,
            userId,
            tweetId
        )

        heapq.heappush(self.tweets, tweet)
        

    def getNewsFeed(self, userId: int) -> list[int]:
        self.create_user_if_not_exists(userId)

        count = min(10, len(self.tweets))
        user = self.users[userId]

        feed = []
        putback = []
        while count and self.tweets:
            tweet = heapq.heappop(self.tweets)
            _, tweet_user_id, tweetId = tweet
            if user.is_following(tweet_user_id):
                count -= 1
                feed.append(tweetId)

            putback.append(tweet)

        while putback:
            heapq.heappush(
                self.tweets,
                putback.pop()
            )
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