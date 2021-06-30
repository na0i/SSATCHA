# SSATCHA

- 개발일지 

  https://www.notion.so/SSATCHA-da494cdfe46b4b4787a4bec855d72dbe

<br>

#### 1. 참여자 

	- 박나영
	- 조정원



#### 2. 일정 

```	
21. 05. 20 - 21. 05. 27 
```



#### 3. 프로젝트 개요 

- Vue.js 와 Django를 이용하여 
- TMDB API를 기반으로 
- 영화 추천 서비스를 구현한다



#### 4. 기능 

- 영화 좋아요 및 리뷰 생성
  - 로그인한 회원의 경우, 영화에 좋아요를 누르거나, 
  - 리뷰를 작성하며 평점을 등록할 수 있다. 
  - 또한, 리뷰에 좋아요를 누르거나 댓글 혹은 대댓글을 생성할 수 있다. 
- 스트리밍 혹은 구매 사이트로 연결 
  - 각 영화의 상세 정보 페이지에서 스트리밍 혹은 구매사이트로 직접 연결이 가능하다. 
- 유저 프로필 
  - 개인 프로필 페이지에서 현재까지 작성한 리뷰, 좋아요를 누른 리뷰, 좋아요를 누른 영화 목록을 확인할 수 있다. 
  - 회원가입시 등록한 영화 장르를 기준으로 개인 맞춤 영화 추천을 받아볼 수 있다. 
- 영화 검색 
  - 제목으로 영화를 검색하여 영화 상세 페이지를 확인할 수 있다. 
- 영화 정보 
  - 영화 상세 페이지에서는 영화 포스터, 개봉일, 줄거리 등의 정보를 확인할 수 있다. 
  - 영화를 시청하거나 구매가 가능한 사이트들이 아이콘으로 제공되며, 해당 아이콘을 누르는 경우 시청 가능한 페이지로 이동한다. 



#### 5. 개발과정에서 마주한 고충들 및 잊지 말아야 할 개발기록 

- [회원가입 (Django Rest-Auth customization)](Readme/rest_auth_customize.md)
  - [회원가입시 many-to-many 필드 연결](Readme/many-to-many.md) 
- [Circular import error](Readme/circular_import_error.md) 
- [영화 검색](Readme/search_movie.md) 
- [Broken pipe from ..](Readme/broken_pipe.md)
- [영화 감상 사이트 연결](Readme/web_crawling.md) 

