class Twitter:

    def __init__(self):
        self.tweets = 0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.tweets, tweetId])
        self.tweets -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        heap = []
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                idx = len(self.tweetMap[followeeId])
                count, tweetId = self.tweetMap[followeeId][-1]
                heap.append([count, tweetId, followeeId, idx-1])
        heapq.heapify(heap)
        while heap and len(feed)<10:
            cnt, tweetId, followeeId, pos = heapq.heappop(heap)
            feed.append(tweetId)
            if pos>0:
                prevCnt, prevTweetId = self.tweetMap[followeeId][pos-1]
                heapq.heappush(heap, [prevCnt, prevTweetId, followeeId, pos-1])
        return feed


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
