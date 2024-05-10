# PC와 모바일에서 검색한 횟수를 기반으로 국내 여행지의 인기순위를 예측및 추천
날씨가 좋아져 여행을 가는 사람들이 많아지기 시작하면서
국내여행을 가는 사람들에게 검색횟수에 따른 인기지역을 소개하고자 합니다.

검색횟수를 통한 국내 인기지역 순위 데이터를 사용하였습니다.
jupyter notebook을 사용하였으며 학습과 테스트를 통하여 모델의 
정확도와 예측 성능의 정확성을 높였습니다.
vscode를 이용하여 커밋과 푸시를 하기 전, 학습된 모델의 성능을 확인합니다.

깃허브에 커밋과 푸시는 꼭 해야합니다. 

배포하기 전 aws ec2 인스턴스 보안의 인바운드 규칙 설정을 하고
문제없이 배포할 수 있게 방화벽을 설정합니다.

putty의 스트림릿서버를 실행하여 깃허브의 소스파일을 clone합니다.
"nohup streamlit run (이름) &" 코드를 입력하여 서버가 꺼지지 않게 합니다.