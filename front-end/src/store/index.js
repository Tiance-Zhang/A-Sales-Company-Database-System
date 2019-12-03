import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    index: "1",
    curUser: {
      userId: "",
      type: ""
    }
  },
  mutations: {
    setIndex(state, index) {
      state.index = index;
    },
    setCurUser(state, curUser) {
      state.curUser = curUser;
    }
  },
  actions: {
    updateCurrentTabIndex(context, index) {
      context.commit('setIndex', index);
    },
    updateCurUser(context, curUser) {
      context.commit('setCurUser', curUser);
    }
  },
  getters: {
    getIndex(state) {
      return state.index;
    },
    getCurUser(state) {
      return state.curUser;
    }
  },
  modules: {}
})
