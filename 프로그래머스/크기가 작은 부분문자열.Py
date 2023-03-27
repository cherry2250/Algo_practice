def solution(t, p):
    LENGTH = len(p)
    target_number = int(p)

    count = 0

    for i in range(0, len(t) - LENGTH + 1):
        number = int(t[i : i + LENGTH])
        if number <= target_number:
            count += 1

    return count