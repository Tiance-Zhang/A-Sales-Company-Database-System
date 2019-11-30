import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    index: "1",
  },
  mutations: {
    setIndex(state, index) {
      state.index = index;
    }
  },
  actions: {
    updateCurrentTabIndex(context, index) {
      context.commit('setIndex', index)
    },
  },
  getters: {
    getIndex(state) {
      return state.index
    }
  },
  modules: {}
})
