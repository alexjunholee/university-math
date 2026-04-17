# university-math

대학공업수학 종합 레퍼런스.

## 구조

- `index.html` — 빌드 결과물 (직접 편집하지 않음)
- `chapters/` — 챕터별 HTML 파일 (00-about.html ~ 32-math-history.html, 총 33개)
- `chapters/manifest.txt` — 빌드 순서
- `shared/head.html` — CSS, 사이드바, `<main>` 시작까지
- `shared/footer.html` — `</main>`, JS, `</body>` 끝까지
- `outlines/` — 구상 단계의 아웃라인 파일
- `writing-status.json` — 콘텐츠 작성 파이프라인 현황
- `build.py` — 챕터 조립 → index.html 생성
- `split.py` — index.html → 챕터 분해 (역방향, 초기화용)

## 작업 규칙

- **편집은 `chapters/` 또는 `shared/` 파일에서만.** index.html은 `python3 build.py`로 생성.
- 수학 표기는 KaTeX 문법을 따름.
- Ch 1~18: `<h2 id="...">` + `<h3 id="...">`으로 구분.
- Ch 19~32 (Part VII~XI): `<section id="...">` + `<h3>`으로 구분.
- git push 전 반드시 확인 요청.

---

## 글쓰기 파이프라인 (4단계)

이 프로젝트의 콘텐츠는 반드시 4단계 파이프라인을 따라 작성한다.
**단계를 절대 합치지 않는다.** 각 단계는 별도의 세션/요청에서 수행한다.

### 작업 시작 프로토콜

1. `writing-status.json`을 읽는다.
2. 사용자가 지정한 섹션(`section:xxx`)의 현재 stage를 확인한다.
3. **해당 stage의 체크리스트만 수행한다.**
4. 작업 완료 후 `writing-status.json`을 업데이트한다.

사용자가 stage를 지정하지 않으면 현재 stage를 보고하고 확인을 요청한다.

---

### Stage 1: 구상 (Prewriting) — 사용자 주도

**목표**: 수학 섹션의 범위와 구조를 확정.

체크리스트:
- [ ] 토픽 범위 명확 (예: "chain complex부터 derived functor까지")
- [ ] 선수지식이 이 레퍼런스의 어느 섹션에 해당하는지 명시
- [ ] 정의(Definition) → 정리(Theorem) → 예제(Example) → 증명(Proof) 순서 계획
- [ ] 핵심 정리 목록 (증명할 것 vs statement만 제시할 것)
- [ ] 예제 난이도 계획 (계산, 증명, 반례)
- [ ] index.html에서 삽입될 위치 확인
- [ ] `outlines/{section_id}.md`에 저장
- [ ] `writing-status.json` 업데이트 → `2-drafting`

**하지 않는 것**: 수식 작성, HTML 코딩, 정리 증명

---

### Stage 2: 초고 (Drafting) — Claude

**목표**: 아웃라인의 모든 정의/정리/예제를 HTML로 작성.
**핵심**: 완벽함보다 완성. 아웃라인에 있으면 불완전해도 지금 쓴다.

체크리스트:
- [ ] 아웃라인의 모든 항목이 본문에 반영 (누락 금지)
- [ ] 정의 → `<div class="definition">`, 정리 → `<div class="theorem">`
- [ ] 증명 → `<div class="proof">`, 예제 → `<div class="example">`
- [ ] KaTeX 수식이 렌더링 가능한 문법인가 (기본 검증만)
- [ ] 정의 → 정리 → 예제 → 증명의 자연스러운 흐름
- [ ] 목차 반영될 `<h3 id="...">` 태그 포함
- [ ] `writing-status.json` → `3-revising`, `drafting_date` 기록

**절대 하지 않는 것**:
- 수식을 미려하게 정렬하려는 시도
- 기존 섹션과의 표기 통일
- 증명 생략하고 "자명하다"로 넘기기
- 내용 축약

---

### Stage 3: 수정 (Revising) — Claude

**목표**: 수학적 정확성과 논리적 완결성 검증. 내용(substance)만 본다.

체크리스트:
- [ ] **정의 정확성**: 필요충분조건, 정의역/공역, 공리 누락 없는가
- [ ] **정리 정확성**: 가정이 불필요하게 강하거나 빠진 것 없는가, 결론이 약화되지 않았는가
- [ ] **증명 검증**: 논리적 비약, 보조정리 적용 가능성, 반례 존재 여부
- [ ] **예제 검증**: 계산 답이 맞는가, 실제 계산 추적
- [ ] **선수지식 연결**: 이전 섹션 개념을 올바르게 참조하는가
- [ ] **흐름**: 정의 → 직관 → 정리 → 증명 → 예제 순서가 자연스러운가
- [ ] `writing-status.json` → `4-editing`, `revising_date` 기록

**하지 않는 것**: KaTeX 정렬, 오타 수정, CSS 클래스 교정, 문체 다듬기

---

### Stage 4: 교정 (Editing) — Claude (검수자)

**목표**: 프로젝트 전체와의 일관성 확보, 표면 품질 완성. 내용은 건드리지 않는다.

체크리스트:
- [ ] **KaTeX 표기 통일** (index.html 기존 섹션 기준):
  - 집합: `\mathbb{R}`, `\mathbb{Z}`, `\mathbb{C}`
  - 사상: `f`, `g`, `\varphi`, `\psi`
  - 다중 행: `\begin{aligned}...\end{aligned}`
  - 행렬: `\begin{pmatrix}` or `\begin{bmatrix}` — 기존 방식 따름
- [ ] **정리/정의 번호**: 기존 넘버링 체계와 일관 (예: "정리 16.3.2")
- [ ] **한영 혼용 패턴**: 기존 패턴 따름 (예: "환(Ring)")
- [ ] **HTML 구조**: h2/h3 레벨, section id (kebab-case), box 클래스 올바른가
- [ ] **사이드바 목차**: 새 섹션이 목차에 올바르게 반영되는가
- [ ] **오타/문법**: 한국어 맞춤법, 영어 스펠링, 수식 내 오타
- [ ] **시각적 확인**: 브라우저에서 레이아웃 깨지지 않는가
- [ ] `writing-status.json` → `done`, `editing_date` 기록
