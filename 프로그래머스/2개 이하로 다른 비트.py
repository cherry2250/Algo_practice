def solution(numbers):
    answer = []
    for number in numbers:
        if number % 2 == 0 :
            binary = list(bin(number)[2:])
            binary[-1] = "1"
        else :
            binary = bin(number)[2:]
            binary = "0" + binary
            a = binary.rfind("0")
            binary = list(binary)
            binary[a] = "1"
            binary[a + 1] = "0"
        ans = int("".join(binary), 2)
        answer.append(ans)
    return answer