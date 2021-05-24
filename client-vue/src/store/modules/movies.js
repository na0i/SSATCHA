import axios from "axios";
// import router from "@/router";
// 장고 서버 url
import DRF from '@/api/drf'

const state = {
  movies: []
}

const getters = {

}

const mutations = {
  SET_MOVIES: (state, movies) => {
    console.log(movies)
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