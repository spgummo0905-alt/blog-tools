# blog-tools 작업 규칙

## 새 도구를 만들 때 반드시 함께 만들 것
`tools/<도구 이름>/` 폴더에 아래 4개 파일을 모두 만든다.

1. `widget.html`: 계산기만. 외부 라이브러리 없이 동작하고, CSS 클래스는 도구 고유 접두어를 쓴다.
2. `post.html`: 도입부 + 위젯 + 설명 + FAQ + FAQPage JSON-LD.
3. `README.md`: 제목·태그 추천, 계산 기준.
4. `PUBLISH.md`: 발행용 프롬프트. Chrome이 연결된 세션(데스크톱 앱, Cowork)에 그대로 붙여 넣으면 예약발행까지 끝나게 쓴다. 형식은 `tools/age-calculator/PUBLISH.md`를 따른다.
   - 본문은 raw 주소(`https://raw.githubusercontent.com/spgummo0905-alt/blog-tools/main/tools/<도구>/post.html`)로 지정한다.
   - 제목과 태그는 README.md 추천값을 프롬프트 안에 그대로 적는다.
   - 대상: 연결된 블로그 전부(스레드 제외).
   - 카테고리 기본값: `생활 계산기`
   - 예약 시간: 이전 도구 발행일에서 이틀 뒤 오전 9시를 기본값으로 제안한다(블로그끼리는 같은 날, 도구끼리는 간격을 둔다).

루트 `README.md`의 도구 목록에도 추가한다.
