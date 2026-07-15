

class Twitter:

    def __init__(self):
        self.timer = 0
        self.followers = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timer, tweetId))
        self.timer -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []
        followed = self.followers[userId]
        followed.add(userId)
        for followid in followed:
            if followid in self.tweets:
                idx = len(self.tweets[followid]) - 1
                (timer, tweet) = self.tweets[followid][idx]
                heapq.heappush(heap, (timer, tweet, followid, idx-1))
        
        while heap and len(res) < 10:
            (_, tweetId, followid, idx) = heapq.heappop(heap)
            res.append(tweetId)

            if idx >= 0:
                (timer, tweet) = self.tweets[followid][idx]
                heapq.heappush(heap, (timer, tweet, followid, idx-1))
        
        return res



    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)
        
