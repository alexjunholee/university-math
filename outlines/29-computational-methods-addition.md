# Ch 29 Computational Methods — 추가: 행렬 분해

## 삽입 위치
29.1 (Condition Numbers) 뒤, 29.2 (Iterative Methods) 앞에 새 h4 섹션.

## 선수지식
- Ch 7: 선형대수 (행렬 연산, 고유값, SVD 개념)
- Ch 29 기존: 조건수

## 아웃라인

### 29.x Direct Methods: Matrix Factorizations (직접법: 행렬 분해)

1. **Definition (LU Decomposition)**: A = LU (하삼각 × 상삼각). 부분 피벗팅: PA = LU.
2. **Theorem**: LU 분해의 존재 조건 (주요 소행렬식이 0이 아닌 경우) 및 비용 O(n³/3).
3. **Example**: 3×3 LU 분해 + 전진/후진 대입으로 Ax = b 풀기.

4. **Definition (QR Decomposition)**: A = QR (직교 × 상삼각). Gram-Schmidt, Householder, Givens 방법.
5. **Theorem**: 임의의 m×n 행렬 (m ≥ n)에 대해 QR 분해 존재. 비용 O(2mn² - 2n³/3).
6. **Example**: 최소제곱 문제 min ‖Ax - b‖₂를 QR로 풀기.

7. **Definition (SVD, Singular Value Decomposition)**: A = UΣV^T. 특이값의 의미.
8. **Theorem**: 임의의 m×n 실수 행렬에 대해 SVD 존재. rank(A) = 양의 특이값 개수.
9. **Example**: 2×3 행렬의 SVD 계산.
10. **Theorem (Eckart-Young)**: rank-k 최적 근사는 SVD의 처음 k개 특이값으로 주어짐.
11. **Remark**: 응용 — 데이터 압축(이미지), 의사역행렬(pseudoinverse), PCA.

## 핵심 정리
- LU 존재: statement
- QR 존재: statement
- SVD 존재: statement
- Eckart-Young: statement + 직관

## 예제 난이도
- LU 3×3 풀이: 상세 계산
- QR 최소제곱: 계산
- SVD 2×3: 계산
