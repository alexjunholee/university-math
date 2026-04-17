# Ch 27 Linear Programming — 추가: 풀이 예제

## 삽입 위치
Theorem 27.3 (Fundamental Theorem) 뒤, source-tag 앞.

## 선수지식
- Ch 27 기존: LP 정의, BFS, 심플렉스 방법 설명, 쌍대성

## 아웃라인

### 풀이 예제

1. **Example (Simplex Method 2변수)**: 
   - max 5x₁ + 4x₂ s.t. 6x₁ + 4x₂ ≤ 24, x₁ + 2x₂ ≤ 6, x₁,x₂ ≥ 0
   - 슬랙 변수 도입 → 초기 tableau → 피벗 2회 → 최적해
   - 기하학적 해석: 실행 가능 영역의 꼭짓점 이동

2. **Example (Dual 구성과 해석)**:
   - 위 문제의 쌍대 구성
   - 쌍대해 구하기 (상보 여유 조건 사용)
   - 경제학적 해석: 쌍대 변수 = 자원의 그림자 가격

3. **Example (Sensitivity Analysis / 감도분석)**:
   - b 벡터 변화 시 최적해 변동 범위
   - c 벡터 변화 시 기저 유지 조건

## 핵심 정리
- 기존 정리들의 예제 적용 (새 정리 없음)

## 예제 난이도
- Simplex tableau 풀이: 계산 (상세 단계)
- 쌍대 해석: 계산 + 경제학적 해석
- 감도분석: 계산
