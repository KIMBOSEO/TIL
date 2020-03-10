# 0218 python



## OOP with python 



- 클래스 : 객체를 표현하는 타입
- 인스턴스 : 클래스에서 정의한 행위를 수행할 수 있다.
- 속성 : 클래스/ 인스턴스가 가지고 있는 속성
- 메서드 : 클래스/ 인스턴스가 할 수 있는 행위



![image](https://user-images.githubusercontent.com/48462044/74693307-a812d080-522e-11ea-9766-fec084b5ed5e.png)

complex라는 객체 안에 img_number 라는 인스턴스



```py
help(complex)
# 메서드
Data descriptors defined here:
imag
the imaginary part of a complex number
real
the real part of a complex number
```



### snake case(변수, 함수) and camel case(클래스명)





파이썬에서의 생성은 (`__new__`/`__init__`)

new	=>	create

init	=>	customize(init) (초기화)	->

new + init	=>	constructor(생성자) 



new 인스턴스가 만들어 질때 자동으로 호출 (우리가 작성하지 않아도, 인스턴스의 생성에 직접관여)



기술서적 : init 생성자 함수를 쓸건데 실제로는 생성자가 아닙니다. 다만 편의를 위해 앞으로 생성자 함수라고 표현하겠습니다. 