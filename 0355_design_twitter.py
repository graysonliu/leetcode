# Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see the 10 most recent tweets in the user's news feed. Your design should support the following methods:
#
# postTweet(userId, tweetId): Compose a new tweet.
# getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
# follow(followerId, followeeId): Follower follows a followee.
# unfollow(followerId, followeeId): Follower unfollows a followee.
# Example:
#
# Twitter twitter = new Twitter();
#
# // User 1 posts a new tweet (id = 5).
# twitter.postTweet(1, 5);
#
# // User 1's news feed should return a list with 1 tweet id -> [5].
# twitter.getNewsFeed(1);
#
# // User 1 follows user 2.
# twitter.follow(1, 2);
#
# // User 2 posts a new tweet (id = 6).
# twitter.postTweet(2, 6);
#
# // User 1's news feed should return a list with 2 tweet ids -> [6, 5].
# // Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
# twitter.getNewsFeed(1);
#
# // User 1 unfollows user 2.
# twitter.unfollow(1, 2);
#
# // User 1's news feed should return a list with 1 tweet id -> [5],
# // since user 1 is no longer following user 2.
# twitter.getNewsFeed(1);

from typing import List


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        import collections
        self.followings = collections.defaultdict(set)
        self.posts = collections.defaultdict(list)
        self.post_index = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.posts[userId].append((tweetId, self.post_index))
        self.post_index += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        positions = {}
        for followeeId in self.followings[userId] | {userId}:
            positions[followeeId] = len(self.posts[followeeId]) - 1
        res = []
        while len(res) < 10 and len(positions) > 0:
            max_index = -float('inf')
            max_index_followee = None
            neg_pos_followees = []
            for followeeId, pos in positions.items():
                if pos < 0:
                    neg_pos_followees.append(followeeId)
                elif self.posts[followeeId][pos][1] > max_index:
                    max_index = self.posts[followeeId][pos][1]
                    max_index_followee = followeeId
            if max_index_followee:
                res.append(self.posts[max_index_followee][positions[max_index_followee]][0])
                positions[max_index_followee] -= 1
            for followee in neg_pos_followees:
                del positions[followee]
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.followings[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        self.followings[followerId].discard(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
