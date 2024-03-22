def max_meetings(meetings):
    # 끝나는 시간 기준으로 오름차순 정렬. 같은 경우 시작 시간으로 정렬.
    sorted_meetings = sorted(meetings, key=lambda x: (x[1], x[0]))
    last_end_time = 0
    selected_meetings = 0

    for start, end in sorted_meetings:
        if start >= last_end_time:  # 이전 회의가 끝난 후 시작되는 경우
            selected_meetings += 1
            last_end_time = end

    # 전체 회의 수에서 선택된 회의 수를 빼서 취소해야 하는 회의 수를 구함
    return len(meetings) - selected_meetings

# 입력 예시
n = int(input())
meetings = []
for _ in range(n):
    s, e = map(int, input().split())
    meetings.append((s, e))

# 최소 취소 회의 수 출력
print(max_meetings(meetings))