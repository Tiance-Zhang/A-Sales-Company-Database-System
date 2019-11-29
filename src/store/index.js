import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    userId: "123",
    index: "1",
    userType: "1"
  },
  mutations: {
    setUserId(state, userId) {
      state.userId = userId;
    },
    setIndex(state, index) {
      state.index = index;
    },
    setUserType(state, userType) {
      state.userType = userType;
    }
  },
  actions: {
    updateCurrentTabIndex(context, index) {
      context.commit('setIndex', index)
    },
    updateUserType(context, userType) {
      context.commit('setUserType', userType)
    }
  },
  getters: {
    getUserId(state) {
      return state.userId
    },
    getIndex(state) {
      return state.index
    },
    getUserType(state) {
      return state.userType
    }
  }
  ,
  modules: {}
})
