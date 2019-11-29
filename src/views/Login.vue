<template>
  <el-card class="input">
    <el-input v-model="userId" placeholder="Your ID"></el-input>
    <el-button class="submit" @click="submitLogin">Login</el-button>
  </el-card>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      userId: ""
    };
  },
  mounted() {
    this.$store.dispatch("updateCurrentTabIndex", "6");
  },
  methods: {
    submitLogin() {
      if (this.userId === "1") {
        this.$store.dispatch("updateUserType", "1");
      } else {
        this.$store.dispatch("updateUserType", "2");
      }
    }
  }
};
</script>

<style scoped>
.input {
  height: 200px;
  text-align: center;
  width: 400px;
  margin: 50px auto;
  padding: 50px;
}

.submit {
  margin-top: 50px;
}
</style>
