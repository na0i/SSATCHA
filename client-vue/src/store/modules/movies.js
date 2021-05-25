import axios from "axios";
import _ from 'lodash'
// import router from "@/router";
// 장고 서버 url
import DRF from '@/api/drf'


const state = {
  movies: [],
  selectedMovie: {},
  selectedMovieProviders: {
        buy: [],
        flatrate: [],
        rent: [],
      },
}


const getters = {
  fetchTopRated() {
    return _.sortBy(state.movies.filter(movie => movie.vote_count > 300), 'vote_average').reverse().slice(0, 40)
  },
  fetchPopularity() {
    return _.sortBy(state.movies, 'popularity').reverse().slice(0, 40)
  },
  fetchKorean() {
    // 한국 영화 중에서 평점 높은 순 40개
    return _.sortBy(state.movies.filter(movie => movie.original_language === 'ko'), 'vote_average').reverse().slice(0, 40)
  },
  fetchClassic() {
    // 70~ 80 년대 영화 추천
    return _.sortBy(state.movies.filter(movie => {
      let regex = new RegExp('^197|^198')
      return regex.test(movie.release_date)}, 'vote_average').reverse().slice(0, 40)
    )
  },
}


const mutations = {
  SET_MOVIES: (state, movies) => {
    state.movies = movies
  },
  SET_MOVIE_DETAIL: (state, movie) => {
    state.selectedMovie = movie
  },
  SET_PROVIDERS: (state, data) => {
    if (data === undefined) {
      state.selectedMovieProviders.buy = []
      state.selectedMovieProviders.flatrate = []
      state.selectedMovieProviders.rent = []
    } else {
      if (data.buy) {
        state.selectedMovieProviders.buy = data.buy
      }
      if (data.flatrate) {
        state.selectedMovieProviders.flatrate = data.flatrate
      }
      if (data.rent) {
        state.selectedMovieProviders.rent = data.rent
      }
    }
  },
}


const actions = {
  fetchMovies({commit}) {
    axios.get(DRF.URL)
      .then(res => {
        commit('SET_MOVIES', res.data)
      })
      .catch(err => console.log(err))
  },
  setMovieDetail({commit}, movie) {
    commit('SET_MOVIE_DETAIL', movie)
    axios.get(`https://api.themoviedb.org/3/movie/${movie.id}/watch/providers?api_key=1f6f8f7d643eea003df9f19e38d13c3d&language=ko-KR&page=1`)
    .then(res => { commit('SET_PROVIDERS', res.data.results.KR)})
    .catch(err => console.log(err))
  }
}


export default {
  state, getters, mutations, actions
}