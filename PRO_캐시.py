# LRU Cache
from collections import deque


def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5

    cache = deque()
    time = 0
    for city in cities:
        city = city.lower()
        if city in cache:
            time += 1
            cache.remove(city)
            cache.append(city)
        else:
            time += 5
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                cache.popleft()
                cache.append(city)

    return time


if __name__ == '__main__':
    print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))