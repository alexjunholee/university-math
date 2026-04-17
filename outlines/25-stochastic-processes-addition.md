# Ch 25 Stochastic Processes — 추가 섹션

## 삽입 위치
기존 Remark (확률론의 핵심 관계 요약) 앞에 삽입.

## 선수지식
- Ch 23: 확률론 (기댓값, 조건부 기댓값)
- Ch 25 기존: 마르코프 체인, 포아송 과정, 브라운 운동

## 아웃라인

### 25.x Martingales (마팅게일)

1. **Definition (Filtration)**: 정보의 증가를 나타내는 σ-대수 열 {F_n}.
2. **Definition (Martingale)**: E[X_{n+1} | F_n] = X_n. Submartingale, supermartingale.
3. **Example**: 공정한 도박 — 누적 상금이 마팅게일.
4. **Example**: 조건부 기댓값 마팅게일 — X_n = E[Y | F_n].
5. **Theorem (Optional Stopping Theorem)**: 유계 정지시간에서 마팅게일의 기댓값 보존.
6. **Example**: 도박사 파산 문제를 마팅게일로 풀기.

### 25.y Itô Calculus (이토 미적분) 기초

1. **Definition (Itô Integral)**: ∫₀ᵗ f(s) dW(s) — 브라운 운동에 대한 확률적분. 비예측적 피적분함수.
2. **Theorem (Itô's Lemma)**: df(W_t) = f'(W_t)dW_t + ½f''(W_t)dt. 확률미적분의 연쇄법칙.
3. **Example**: d(W_t²) = 2W_t dW_t + dt 유도.
4. **Definition (SDE)**: 확률미분방정식 dX_t = μ(X_t)dt + σ(X_t)dW_t.
5. **Example (Geometric Brownian Motion)**: dS = μS dt + σS dW → S_t = S_0 exp((μ-σ²/2)t + σW_t). 금융수학의 기본 모형.

### 25.z Ergodic Theorem

1. **Theorem (Birkhoff Ergodic Theorem)**: 정상 에르고딕 과정에서 시간 평균 = 앙상블 평균 (a.s.).
2. **Example**: 에르고딕 마르코프 체인에서의 시간 평균 수렴.

## 핵심 정리
- Optional Stopping Theorem: statement + 조건 명시
- Itô's Lemma: statement + 증명 스케치 (이차변동항이 핵심)
- Birkhoff Ergodic Theorem: statement만

## 예제 난이도
- 도박사 마팅게일: 계산
- Itô W_t²: 계산
- GBM: 계산 + 응용 설명
