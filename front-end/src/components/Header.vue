<template>
  <div>
    <el-menu :default-active="getIndex" mode="horizontal">
      <h1 class="logo">LOGO</h1>
      <el-menu-item index="1">
        <router-link to="/" class="nav-link">Products</router-link>
      </el-menu-item>
      <el-menu-item index="2">
        <router-link to="stores" class="nav-link">Stores</router-link>
      </el-menu-item>
      <el-menu-item index="3">
        <router-link to="transactions" class="nav-link">Transactions</router-link>
      </el-menu-item>
      <el-menu-item index="4">
        <router-link to="users" class="nav-link">Users</router-link>
      </el-menu-item>
      <el-menu-item index="5">
        <router-link to="statistics" class="nav-link">Statistics</router-link>
      </el-menu-item>
      <el-menu-item index="6">
        <router-link to="login" class="nav-link">Login</router-link>
      </el-menu-item>
    </el-menu>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "Header",
  data() {
    return {
      activeIndex: "1"
    };
  },
  computed: {
    ...mapGetters(["getIndex"])
  }
};
</script>

<style scoped>

.logo {
  align-self: center;
  margin: 0;
  outline: none;
}

.el-menu {
  display: flex;
  justify-content: space-between;
}

.el-menu-item {
  padding: 0;
}
</style>
