# html5 css3 첫 실습

![image](https://user-images.githubusercontent.com/48462044/76524933-4997e580-64ae-11ea-9541-f44652740f03.png)

위 이미지를 만들기 위한 코드:

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="index.css">
    <title>homework</title>
```



   주어진 가장 기본 코드

index.css를 만들어 보기 깔끔하게 하고 title에 homework를 작성하여 페이지를 열었을 때, homework이 페이지 이름으로 들어간다.

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="index.css">
    <title>homework</title>
   
</head>
<body>
    <div class="header">
        <div id="logo">
            <h1>BIKESHARE </h1>
        </div>
        <div class="nav">
            <h1>ABOUT LOGIN SIGNUP</h1>
        </div>
    </div>
    <div class="main">
        <img src="bicycles.jpg" alt="bicycle" id="bicycle">
    </div>
    <div class="sub_main">
        <div class="section1">
            
        </div>
        <div class="section2">
            <div class="mention">
                <h1>자전거로 도심을 누벼보세요</h1>
            </div>
            <div class="commute">
                <img src="images/commuter.jpg" alt="commuter" id="com">
            </div>
        </div>
        <div class="section3">

        </div>
    </div>
</body>
</html>
```

크게 header, main, sub_main으로 세개의 div로 구역을 분리해주었다.

- header:

  logo라는 이름을 주어 bikeshare를 구분해 주고 왼쪽으로 정렬(css에서)

  nav 라는 이름을 주어 각각 about login signup을 오른쪽 정렬해주었다.

  위와 같이 nav로 따로 준 이유는 차후 각각의 버튼을 생성하여 눌러주었을 때, 각기 다른 곳으로

  링크를 연결 시켜주기 위함이다.

- main:

  bicycle 사진이 들어가면 끝이기 때문에 간단하게 사진을 넣어주고 alt="bicycle"이 주는 의미는

  만약 링크가 깨졌을 때, 밑에 bicycle이라고 알려주기 위함

- sub_main:

  sub_main은 사진의 가운데 정렬을 위해 빈 div를 좌우에 생성 시켜주었고, 이들이 section1과 section3이다.

  section2를 다시 두개의 div로 나누어 위에는 '자전거로 도심을 누벼보세요'가 들어가고

  아래에는 사진이 들어간다. 

```css
body{
    height: 100%;
    width: 100%;
}
.header{
    width: 100%;
    height: 50px;
}
.header #logo{
    float: left;
    font-style: italic;
}
.header .nav{
    float: right;
    margin-right: 50px;
}
.main{
    height: 50%;
    width: 100%;
}
.main #bicycle{
    height: 100%;
    width: 100%;
}
.sub_main{
    height: 40%;
    width: 100%;
}

.sub_main .section1{
    height: 100%;
    width: 20%;
}
.sub_main .section2{
    height: 100%;
    width: 60%;
    margin-left: 20%;
}
.sub_main .section2 .mention{
    text-align: center;
}
.sub_main .section2 #com{
    height: 100%;
    width: 100%;
}
.sub_main .section3{
    height: 100%;
    width: 20%;
    margin-left: 80%;
}
```

css 부분



body의 전체 크기를 100, 100%로 잡아주었다.

이후 각각의 div 별로 다시 구역을 %로 잡아주고 

logo를 왼쪽 정렬시켜 주기 위해서 `float: left;` 를 해준것. 또한 이것 저것 공부하기 위해 폰트를 바꾸어 이탈릭체로 바꾸어 주었다.

nav 부분은 `float: right;` 만 해주었을때 signup의 p부분이 오른쪽으로 너무 붙어서 어색하기 때문에 

오른쪽 마진을 50px주어서 어색을 없애 주었다.

그 다음으로 section2에서 글씨를 가운데 정렬 시켜주기 위해 `text-align: center`를 해주었고

좌우의 빈 div 부분들이 `margin-left: 20%` `margin-right: 80%` 없이는 겹쳐지기 때문에 추가해주었다.





완성된 모습

![image](https://user-images.githubusercontent.com/48462044/76525838-f3c43d00-64af-11ea-8895-a3bab03b5e31.png)



한줄평: 처음 배운 html과 css를 통해 웹에 대한 관심이 생겼다. 어렵지만 배우는 재미를 원동력으로 좋은 웹 개발자가 되기 위해 더 노력해야겠다.