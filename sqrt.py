def my_sqrt(n):
    x, y = 1, n # 양의 정수니까 1부터 입력된 양의 정수까지
    result = 1 # 우리가 추측하는 제곱근 / 근사치의 시작을 1로 둔다 (양의 정수)

    # 제곱근의 제곱(result**2)과 입력 값(n)의 차이가 적어도 0.000000000001 차이보다 적다면,
    while abs(result**2 - n) > 0.0000000001: # 1e-10
        result = (x+y) / 2 # 양쪽 끝을 더해서 2로 나눈다. 이를 추측하는 값으로 변경
        if result**2 < n : # 제곱근의 제곱이 입력 값보다 작으면, 앞 범위가 제곱근(result)으로 변경
            x = result
        else:              # 반대로 입력 값보다 크다면 뒷 범위를 제곱근(result)로 변경
            y= result
    return result

print(my_sqrt(2))
    