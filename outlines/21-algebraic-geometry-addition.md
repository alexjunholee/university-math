# Ch 21 Algebraic Geometry — 확장 아웃라인

## 삽입 위치
기존 Theorem 21.3 (Affine–Projective Dictionary) 뒤, `</section>` 앞.

## 선수지식
- Ch 14: 환과 체 이론 (아이디얼, 몫환)
- Ch 21 기존: 아핀 다양체, 자리스키 위상, Nullstellensatz, 좌표환

## 아웃라인

### 추가 내용

1. **Definition (Dimension)**: Krull 차원 — 소아이디얼 체인의 최대 길이. dim V(y² - x³) = 1.
2. **Definition (Tangent Space)**: Zariski 접선공간 — m_p/m_p² 의 쌍대공간. 
3. **Definition (Smooth/Singular Point)**: dim T_p V = dim V이면 매끈, 아니면 특이.
4. **Example**: cusp y² = x³ 의 원점에서 접선공간 차원 = 2 > 1 → 특이점. node y² = x²(x+1)의 원점도 특이.
5. **Theorem (Bézout's Theorem)**: P² 에서 차수 d, e인 두 곡선의 교점 수는 (중복도 포함) de개. 
6. **Example**: 직선과 원뿔곡선의 교점 = 2개, 두 원뿔곡선 = 4개.
7. **Definition (Genus)**: 매끈 사영 곡선의 종수. 차수 d 평면곡선: g = (d-1)(d-2)/2.
8. **Remark**: 종수에 따른 분류 — g=0 유리곡선, g=1 타원곡선, g≥2 일반형.

## 핵심 정리
- Bézout's Theorem: statement + 증명 없이 직관 설명 (사영 공간에서 "무한원점"을 포함해야 성립)
- 차원/접선공간/특이점: 정의 + 예제

## 예제 난이도
- cusp/node 특이점 판정: 계산
- Bézout 적용: 계산
- 종수 공식: statement
