<template>
  <el-card class="container">
    <div v-if="getCurUser.userId === ''">
      <el-input v-model="info.userId" placeholder="Enter Youer ID"></el-input>
      <el-button class="submit" @click="login">Login</el-button>
    </div>
    <div v-else>
      <UserInfo :info="getCurUser"></UserInfo>
    </div>
    <el-button v-if="getCurUser.userId !== ''" class="submit" @click="logout">Logout</el-button>
  </el-card>
</template>

<script>
import UserInfo from "@/components/UserInfo";
import { mapGetters } from "vuex";

export default {
  name: "Login",
  components: {UserInfo},
  data() {
    return {
      showUserInfo: false,
      info: {
        userId: ""
      }
    };
  },
  mounted() {
    this.$store.dispatch("updateCurrentTabIndex", "6");
  },
  computed: {
    ...mapGetters(["getCurUser"])
  },
  methods: {
    async login() {
      const r = await this.$api.get("/api/user?id=" + this.info.userId);
      if (r.data.status == true) {
        this.$store.dispatch("updateCurUser", r.data);
      } else {
        alert("Login Failed");
      }
    },
    logout() {
        this.$store.dispatch("updateCurUser", {"userId": "", "type": ""});
    }
  }
};
</script>

<style scoped>
.container {
  margin: 20px auto;
  text-align: center;
  width: 600px;
}

.submit {
  margin-top: 20px;
}

.infoBody {
  display: flex;
  justify-content: space-between;
  padding: 14px 18px;
}
</style>