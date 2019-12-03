<template>
  <div class="container">
    <el-radio-group v-model="pageType" class="pageType">
      <el-radio :label="false" border>Search existing user</el-radio>
      <el-radio :label="true" border>Create a new user</el-radio>
    </el-radio-group>
    <el-card v-if="pageType" class="newUser">
      <div
        v-if="getCurUser.userId !== '' && getCurUser.type !== 0"
      >Sorry you don't have the permission to create user, or you should log out first.</div>
      <NewUser v-else :info="info"></NewUser>
    </el-card>
    <el-card
      v-if="!pageType && (getCurUser.type === 0 || getCurUser.type === 1)"
      class="searchUser"
    >
      <el-input v-model="userId" placeholder="Enter User ID"></el-input>
      <el-button class="submit" @click="submitSearch">Search</el-button>
    </el-card>
    <el-card
      v-if="!pageType && getCurUser.type !== 0 && getCurUser.type !== 1"
      class="userInfo"
    >Sorry you don't have the permission to search user.</el-card>
    <el-card v-else-if="!pageType && showUserInfo" class="userInfo">
      <UserInfo :info="info"></UserInfo>
    </el-card>
  </div>
</template>

<script>
import UserInfo from "@/components/UserInfo";
import NewUser from "@/components/NewUser";
import { mapGetters } from "vuex";

export default {
  name: "Users",
  components: { UserInfo, NewUser },
  data() {
    return {
      pageType: false,
      showUserInfo: false,
      userId: "",
      info: {
        name: "",
        id: "",
        userId: "",
        type: "",
        address: "",
        zip: "",
        email: "",
        jobTitle: "",
        category: "",
        gross: "",
        marriage: "",
        gender: "",
        age: "",
        income: ""
      }
    };
  },
  mounted() {
    this.$store.dispatch("updateCurrentTabIndex", "4");
    this.showUserInfo = false;
    this.pageType = false;
  },
  computed: {
    ...mapGetters(["getCurUser"])
  },
  methods: {
    async submitSearch() {
      const r = await this.$api.get("/api/user?id=" + this.userId);
      if (r.data.status == true) {
        this.showUserInfo = true;
        this.info = r.data;
      } else {
        alert("No result!");
      }
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

.searchUser,
.newUser,
.userInfo {
  margin: 20px auto;
}

.newUser {
  width: 600px;
}

.submit {
  margin-top: 20px;
}

.el-select {
  width: 100%;
}

.infoBody {
  display: flex;
  justify-content: space-between;
  padding: 14px 18px;
}
</style>
