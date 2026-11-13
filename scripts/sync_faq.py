#!/usr/bin/env python3
"""post.html 의 화면 FAQ(<h3>질문</h3><p>답</p>)로 FAQPage JSON-LD 를 다시 만든다.

화면 문구와 JSON-LD 문구가 글자까지 같아야 하므로, JSON-LD 는 손으로 쓰지 말고 이 스크립트로 만든다.
  python3 scripts/sync_faq.py tools/<도구>/post.html          # JSON-LD 갱신
  python3 scripts/sync_faq.py --check tools/*/post.html       # 일치 여부만 검사 (불일치 시 종료코드 1)
FAQ 구역: <h2>자주 묻는 질문</h2> 다음부터 다음 <h2> 또는 JSON-LD 스크립트 전까지의 h3/p 쌍.
"""
import html, json, re, sys

LD_RE = re.compile(r'<script type="application/ld\+json">.*?</script>\n?', re.S)

def text(fragment):
    return html.unescape(re.sub(r"<[^>]+>", "", fragment)).strip()

def extract(doc):
    start = doc.find("<h2>자주 묻는 질문</h2>")
    if start < 0:
        raise SystemExit("FAQ 구역(<h2>자주 묻는 질문</h2>)이 없어요")
    body = doc[start + len("<h2>자주 묻는 질문</h2>"):]
    body = re.split(r"<h2>|<script type=\"application/ld\+json\">", body)[0]
    pairs = re.findall(r"<h3>(.*?)</h3>\s*<p>(.*?)</p>", body, re.S)
    if not 4 <= len(pairs) <= 5:
        print(f"경고: FAQ가 {len(pairs)}개예요 (4~5개 권장)", file=sys.stderr)
    return [(text(q), text(a)) for q, a in pairs]

def build(pairs):
    data = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in pairs]}
    return '<script type="application/ld+json">\n' + json.dumps(data, ensure_ascii=False, indent=1) + "\n</script>\n"

def main(argv):
    check = "--check" in argv
    bad = 0
    for path in [a for a in argv if a != "--check"]:
        doc = open(path, encoding="utf-8").read()
        pairs = extract(doc)
        m = LD_RE.search(doc)
        if check:
            current = json.loads(re.sub(r"^<script[^>]*>|</script>\s*$", "", m.group(0).strip())) if m else None
            want = json.loads(re.sub(r"^<script[^>]*>|</script>\s*$", "", build(pairs).strip()))
            ok = current == want
            bad += not ok
            print(("OK   " if ok else "DIFF ") + path)
        else:
            new = build(pairs)
            doc = LD_RE.sub(lambda _: new, doc, count=1) if m else doc.rstrip("\n") + "\n\n" + new
            open(path, "w", encoding="utf-8").write(doc)
            print(f"갱신 {path} ({len(pairs)}개)")
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
