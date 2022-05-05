"""
다리: que([0]*n)
트럭: que
다리 0도 pop
"""
from collections import deque


def solution(bridge_length, weight, truck_weights):
    bridge = deque([0 for _ in range(bridge_length)])
    truck_weights = deque(truck_weights)
    bridge_sum = 0
    time = 0

    def can_go(w):
        return bridge_sum + w <= weight

    while truck_weights:
        bridge_sum -= bridge.popleft()
        if can_go(truck_weights[0]):
            truck = truck_weights.popleft()
            bridge.append(truck)
            bridge_sum += truck
        else:
            bridge.append(0)
        time += 1

    return time + bridge_length


if __name__ == '__main__':
    print(solution(2, 10, [7,4,5,6]))