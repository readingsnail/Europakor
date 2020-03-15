# HOI4KOR
Hearts Of Iron 4 한글화

[필수 숙지] 번역작업 유의사항
<h1>[필수 숙지] 번역 작업 유의사항</h1>

<h2>번역문의 아래 특수문자 포함시 번역에 주의!</h2>
<h3>1. [ 기호와 ] 기호 사의의 문장</h3>  

    예시 원문) Germany refuses to split [CZE.GetName]
    예시 번역문) [CZE.GetName] 분할을 거부한 독일

<h3>2. $ 기호와 $기호 사이의 문장(게임에서 사용되는 변수명 이므로)은 번역하지 않는다.</h3>

    예시 원문) $NAME$ supports $WHO|Y$  
    예시 번역문) $NAME$ 지원 $WHO|Y$

<h3>3. § 기호와 §기호 사이의 문장은 첫문자를 제외한 글자는 번역한다.</h3>
- §기호 뒤의 첫 글자는 글자색 구분글자 이므로, 첫글자 이후 단어만 번역합니다.

    예시 원문) re you sure want to §RDelete files§ ?
    예시 번역문) 정말 §R파일삭제§를 원하십니까?

<h3>4. £기호 표시가 있고난 다음 한 단어는 건들지 않는다</h3>
- £이후 한단어는 게임내 그림 아이콘 지칭단어으로 표시되기 때문

    예시 원문) Click to sort by £prod_eff Production Efficiency
    예시 번역문) 클릭으로 £prod_eff 생산효율 정렬

<h2> $기호와 같은 변수기호 뒤에는 가변적인 조사를 삽입한다.</h2>
  - (은)는, (이)가, (을)를, (으)로 등등...  
  
    예시 원문) @war_icon! declare $NAME|Y$  
    예시 번역문) @war_icon! $NAME|Y$(이)가 선언하다.
