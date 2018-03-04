유로파 까페의 한글모드 변환기 / 한글모드 관련 파일 저장소입니다.

Copyright 2018, Copyright (c) 2001~2018 Contributors & Daum Europa Cafe. Under & Distribute by MIT Licenses.

Copyright (C) @WovNyx(StellarisTranstaleSupporter.py) - properity - Paradox's pseudo yaml converter 
일단 스텔라리스 변환기의 저작권은 이 분에게 있습니다. 이 자리를 빌러서 감사 말씀을 전합니다.

* Transifex 로의 전환/이익
  * 기존 까페에서 벌어지던 모든 번역 모드(까페가 아니라도 상관없습니다) 내용들을 포괄가능합니다. 이전엔 새로 프로젝트를 파야했지만, 여기선 하나의 큰 프로젝트아래 다른 프로젝트가 삽입되는 구조입니다.
  * Transifex의 사용자 계층이 Zanata 보다 더 많다는데 있습니다. ipTime의 NAS 한글 번역이 이 Transifex로 돌아가고 있습니다.
  * Call of Duty 의 편리성 - 사람들에게 알릴때 더 쉽게 알릴수 있습니다. 이전엔 한명한명 찾거나 혹은 까페에 글을 올려야 했지만, Transifex의 경우 Resource 파일 변경시 자동으로 메일이 가도록 되어 있습니다. (안 받으실 분은 설정에서 이를 끌 수 있습니다)
  * 기계번역의 편이성 - Zanata에는 기계번역을 삽입할수 없지만, Transifex에선 기계 번역 API를 삽입할 수 있습니다. 현재 MS 번역 API가 삽입되어 있습니다.
  * 기타 번역의 편리성 - Resource 파일을 하나하나 받아서 이를 수정하여 번역을 수정할수 있으며, 또한 오프라인 클라이언트를 이용하여 전부 다 받아서 자신만의 패치를 만들수 있습니다.

* 컨버터 공개
  * 컨버터를 공개함으로써 다른 이들이 컨버터에 대해 접근하여 더 나은 내용으로 교체할 수 있습니다.
  * Headless 번역이 가능해집니다.

번역 사이트
-------------------
<https://www.transifex.com/europa/public/> - Transifex 번역 사이트

파이선 스크립트 사용법
-------------------
* 파이선 스크립트는 Python3을 사용하고 있습니다. Python3은 <https://www.python.org/downloads/> 에서 받으실수 있습니다.
* StellarisTranstaleSupporter.py
> 설정파일 수정 - File Format 항목 두개를 고치면 작동하도록 되어 있습니다. 기타 디렉토리를 변경하실수 있습니다.

> python3(혹은 python) StellarisTranstaleSupporter.py

기타 문의사항
-------------------
* Github Pull Request 이용 - 스크립트를 고치고자 하시는 분들은 이걸 사용해주세요. Pull Reuqest를 거치지 않은 내용은 되돌려질수 있습니다.
* 까페 한글화 게시판 이용 - Transifex에 대한 설명 / 번역 관련 도움말은 여기에서 이용해주세요