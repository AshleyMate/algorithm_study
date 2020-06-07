# 소수를 크기 순으로 나열하면 2, 3, 5, 7, 11, 13, ... 과 같이 됩니다. 이 때 100번째 소수까지 구하시면 됩니다.
# 참고 : https://53perc.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%86%8C%EC%88%98-%ED%8C%90%EB%B3%84%ED%95%98%EA%B8%B0


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return False
    if n == 2:
        return True
    for i in range(3, n, 2):
        if n % i is 0:
            return False
    return True


def prime_number_list(length):
    result = []
    num = 2
    result.append(num)
    while len(result) != length:
        if is_prime(num):
            result.append(num)
        num += 1
    return result


length = int(input('Length? '))
print(prime_number_list(length))
