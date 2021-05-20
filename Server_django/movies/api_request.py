URL = 'https://api.themoviedb.org/3'
api_key = '1f6f8f7d643eea003df9f19e38d13c3d'




'''
장르 요청 url = https://api.themoviedb.org/3/genre/movie/list?api_key=1f6f8f7d643eea003df9f19e38d13c3d&language=ko-kr

popular = https://api.themoviedb.org/3/movie/popular?api_key=1f6f8f7d643eea003df9f19e38d13c3d&language=ko-KR&page=1&region=KR

top_rated = https://api.themoviedb.org/3/movie/top_rated?api_key=1f6f8f7d643eea003df9f19e38d13c3d&language=ko-KR&page=1&region=KR

upcomming = https://api.themoviedb.org/3/movie/upcoming?api_key=1f6f8f7d643eea003df9f19e38d13c3d&language=ko-KR&page=1&region=KR

now_playing = https://api.themoviedb.org/3/movie/now_playing?api_key=1f6f8f7d643eea003df9f19e38d13c3d&language=ko-KR&page=1&region=KR

어디서 볼 수 있는지 여기서 가져올 수 있다!! 
https://api.themoviedb.org/3/movie/{movie_id}/watch/providers?api_key=1f6f8f7d643eea003df9f19e38d13c3d
보면 results > KR 여기 보면 provider 나옵니다.. 
flatrate == 스트리밍, buy == 구매, rent == 대여 
netflix, wavve, watcha, naver_store, google play movies 는 있는 거 확인했음 
왠지 다 된 것 같은 기분이 든다 ㅇㅅㅇ...!!

일단 기생충 보면 
<a href="https://click.justwatch.com/a?cx=eyJzY2hlbWEiOiJpZ2x1OmNvbS5zbm93cGxvd2FuYWx5dGljcy5zbm93cGxvdy9jb250ZXh0cy9qc29uc2NoZW1hLzEtMC0wIiwiZGF0YSI6W3sic2NoZW1hIjoiaWdsdTpjb20uanVzdHdhdGNoL2NsaWNrb3V0X2NvbnRleHQvanNvbnNjaGVtYS8xLTItMCIsImRhdGEiOnsicHJvdmlkZXIiOiJXYXRjaGEiLCJtb25ldGl6YXRpb25UeXBlIjoiZmxhdHJhdGUiLCJwcmVzZW50YXRpb25UeXBlIjoiaGQiLCJjdXJyZW5jeSI6IktSVyIsInByaWNlIjowLCJvcmlnaW5hbFByaWNlIjowLCJhdWRpb0xhbmd1YWdlIjoiIiwic3VidGl0bGVMYW5ndWFnZSI6IiIsImNpbmVtYUlkIjowLCJzaG93dGltZSI6IiIsImlzRmF2b3JpdGVDaW5lbWEiOmZhbHNlLCJwYXJ0bmVySWQiOjYsInByb3ZpZGVySWQiOjk3LCJjbGlja291dFR5cGUiOiJqdy1jb250ZW50LXBhcnRuZXItZXhwb3J0LWFwaSJ9fSx7InNjaGVtYSI6ImlnbHU6Y29tLmp1c3R3YXRjaC90aXRsZV9jb250ZXh0L2pzb25zY2hlbWEvMS0wLTAiLCJkYXRhIjp7InRpdGxlSWQiOjQxNDE3MCwib2JqZWN0VHlwZSI6Im1vdmllIiwiandFbnRpdHlJZCI6InRtNDE0MTcwIiwic2Vhc29uTnVtYmVyIjowLCJlcGlzb2RlTnVtYmVyIjowfX1dfQ&amp;r=https%3A%2F%2Fwatcha.com%2Fcontents%2FmdRL4eL&amp;uct_country=kr" title="Watch 기생충 on Watcha" target="_blank" rel="noopener"><img src="/t/p/original/cNi4Nv5EPsnvf5WmgwhfWDsdMUd.jpg" width="50" height="50"></a>
이거 눌러서 왓챠 스트리밍으로 연결되는데, 어떻게 되는 건지는 모르겠네유...

이거는 넷플릭스 연결 에이태그 
<a href="https://click.justwatch.com/a?cx=eyJzY2hlbWEiOiJpZ2x1OmNvbS5zbm93cGxvd2FuYWx5dGljcy5zbm93cGxvdy9jb250ZXh0cy9qc29uc2NoZW1hLzEtMC0wIiwiZGF0YSI6W3sic2NoZW1hIjoiaWdsdTpjb20uanVzdHdhdGNoL2NsaWNrb3V0X2NvbnRleHQvanNvbnNjaGVtYS8xLTItMCIsImRhdGEiOnsicHJvdmlkZXIiOiJOZXRmbGl4IiwibW9uZXRpemF0aW9uVHlwZSI6ImZsYXRyYXRlIiwicHJlc2VudGF0aW9uVHlwZSI6ImhkIiwiY3VycmVuY3kiOiJLUlciLCJwcmljZSI6MCwib3JpZ2luYWxQcmljZSI6MCwiYXVkaW9MYW5ndWFnZSI6IiIsInN1YnRpdGxlTGFuZ3VhZ2UiOiIiLCJjaW5lbWFJZCI6MCwic2hvd3RpbWUiOiIiLCJpc0Zhdm9yaXRlQ2luZW1hIjpmYWxzZSwicGFydG5lcklkIjo2LCJwcm92aWRlcklkIjo4LCJjbGlja291dFR5cGUiOiJqdy1jb250ZW50LXBhcnRuZXItZXhwb3J0LWFwaSJ9fSx7InNjaGVtYSI6ImlnbHU6Y29tLmp1c3R3YXRjaC90aXRsZV9jb250ZXh0L2pzb25zY2hlbWEvMS0wLTAiLCJkYXRhIjp7InRpdGxlSWQiOjQ1ODI5Miwib2JqZWN0VHlwZSI6Im1vdmllIiwiandFbnRpdHlJZCI6InRtNDU4MjkyIiwic2Vhc29uTnVtYmVyIjowLCJlcGlzb2RlTnVtYmVyIjowfX1dfQ&amp;r=http%3A%2F%2Fwww.netflix.com%2Ftitle%2F81094067&amp;uct_country=kr" title="Watch 승리호 on Netflix" target="_blank" rel="noopener"><img src="/t/p/original/9A1JSVmSxsyaBK4SUFsYVqbAYfW.jpg" width="50" height="50"></a>

대충 보니까.. 
#app > div.content > div.jw-info-box > div > div.col-sm-8.col-sm-push-4 > div.stream-cinematickets-switcher > div > div:nth-child(2) > div > div > div.price-comparison__grid__row.price-comparison__grid__row--stream > div.price-comparison__grid__row__holder > div > div > a
이거 셀렉터 통해서 html 가져올 수 있을 것 같은 기분이 듭니다.. 약간.... 해보면 되지 않을까 싶은데... 

#app > div.content > div.jw-info-box > div > div.col-sm-8.col-sm-push-4 > div.stream-cinematickets-switcher > div > div:nth-child(2) > div > div > div.price-comparison__grid__row.price-comparison__grid__row--stream > div.price-comparison__grid__row__holder > div > div > a
맞네요.. 이거 미나리 셀렉터인데 이거 셀렉터 그냥 그대로 작동하는거 보니까 크롤링하면서 이거 가져와서 어떻게 하면 잘 될 거 같은 그런 기분이 들어유 만들 수 있을 것 같아 



detail = https://api.themoviedb.org/3/movie/{movie_id}?api_key=1f6f8f7d643eea003df9f19e38d13c3d&language=ko-KR

credit == cast & crew 
https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=1f6f8f7d643eea003df9f19e38d13c3d&language=ko-KR

이거는 장르랑 이런거? 좀 고려된 추천 비슷한 거  similar 
https://api.themoviedb.org/3/movie/496243/similar?api_key=1f6f8f7d643eea003df9f19e38d13c3d&language=ko-KR&page=1


검색하는 법 
'''
search = f'https://api.themoviedb.org/3/search/movie?api_key=1f6f8f7d643eea003df9f19e38d13c3d&language=ko-KR&query={search_data}&page={page}&include_adult={include_adult}&region={region}&year=year&primary_release_year={primary_release_year}'

'''

'''