# blog-tools

생활 속에서 자주 검색하는 계산기와 도구를 만들어 블로그(티스토리, 블로거, 워드프레스)에 올리는 사이드 프로젝트입니다.

## 구조

```
tools/
  <도구 이름>/
    widget.html   계산기만 (다른 글에 끼워 넣을 때)
    post.html     블로그 글 본문 전체 (HTML 모드에 통째로 붙여 넣기)
    README.md     제목·태그 추천, 붙여 넣는 방법
    PUBLISH.md    예약발행 프롬프트 (Chrome 연결 세션에 붙여 넣기)
```

## 도구 목록

| 도구 | 폴더 | 상태 |
|---|---|---|
| 만 나이 계산기 | `tools/age-calculator` | 완성 |
| 주휴수당 계산기 | `tools/weekly-holiday-pay` | 완성 |
| 평수 계산기 | `tools/pyeong-converter` | 완성 |
| 퇴직금 계산기 | `tools/severance-calculator` | 완성 |
| 디데이 계산기 | `tools/dday-calculator` | 완성 |
| 연봉 실수령액 계산기 | `tools/salary-calculator` | 완성 |
| 대출 이자 계산기 | `tools/loan-calculator` | 완성 |
| 글자수 세기 | `tools/character-counter` | 완성 |
| 연차 계산기 | `tools/annual-leave-calculator` | 완성 |
| 실업급여 계산기 | `tools/unemployment-benefit-calculator` | 완성 |
| 2027년 나이 조견표 (띠·학년) | `tools/age-table-2027` | 완성 |
| 2027 공휴일·연휴 달력 (연차 꿀조합) | `tools/holidays-2027` | 완성 |
| 2027 정부 지원금 신청 일정·지원금 찾기 | `tools/support-calendar-2027` | 완성 |
| 2027 연말정산 일정·공제 체크리스트 | `tools/year-end-tax-2027` | 완성 |
| 헷갈리는 맞춤법 모음 + 퀴즈 | `tools/spelling-quiz` | 완성 |
| 랜덤 뽑기 모음 (사다리타기·돌림판·제비뽑기·팀 나누기) | `tools/random-picker` | 완성 |
| 전역일 계산기 (복무율·D-day) | `tools/discharge-date-calculator` | 완성 |
| 육아휴직 급여 계산기 (월별 지급액·6+6·한부모) | `tools/parental-leave-pay` | 완성 |
| 부동산 중개수수료(복비) 계산기 | `tools/brokerage-fee-calculator` | 완성 |
| 청약 가점 계산기 (84점 만점, 점수 오르는 날) | `tools/subscription-score-calculator` | 완성 |

## 작업 규칙

- `main`에는 완성된 도구만 둡니다.
- 새 도구는 작업용 브랜치에서 만들고 PR로 합칩니다.
- 위젯은 외부 라이브러리 없이 HTML 파일 하나로 동작해야 합니다(블로그에 붙여 넣기 위해).
- `post.html`의 FAQ JSON-LD는 `python3 scripts/sync_faq.py`로 만듭니다(화면 FAQ와 글자까지 같게).
- 자세한 규칙은 `CLAUDE.md`에 있습니다.
- CSS 클래스는 도구마다 고유한 접두어를 씁니다(예: 만 나이 계산기는 `kac-`). 한 글에 여러 계산기를 넣어도 스타일이 섞이지 않게 하기 위해서예요.
