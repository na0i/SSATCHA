import axios from "axios";
import _ from 'lodash'
// import router from "@/router";
// 장고 서버 url
import DRF from '@/api/drf'

const state = {
  movies: []
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
  }
}

const actions = {
  fetchMovies({commit}) {
    axios.get(DRF.URL)
      .then(res => {
        commit('SET_MOVIES', res.data)
      })
      .catch(err => console.log(err))
  }
}

export default {
  state, getters, mutations, actions
}