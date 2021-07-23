#3053번: 택시기하학
#https://www.acmicpc.net/problem/3053

#유클리드 기하학 공식 = n*n*3.1415
#택시기하학 공식: 2*R^2

'''
유클리드 기하학에서의 두 지점의 거리는 좌표평면상의 최단거리를 의미한다.
하지만 실제 도시에서 두 지점의 거리는 좌표평면상의 최단거리와 다르다.

택시가 한 지점에서 다른 지점으로 이동하는 것을 상상해보자.
택시는 건물을 뚫고 지나가지 못하기때문에 좌회전도하고 우회전도한다.
구불구불 굽어진 길을 가다보면 어느새 목적지에 도착하는데,
이 때 출발지점 T1(x1, y1)과 도착지점 T2(x2, y2) 사이의 거리를 구하는 공식은 다음과 같다.
D(T1, T2) = x1-x2+y1-y2
'''


n=int(input())
print('%.6f'% (n*n*3.14159265358979323846))
print('%.6f'% (2*(n*n)))
