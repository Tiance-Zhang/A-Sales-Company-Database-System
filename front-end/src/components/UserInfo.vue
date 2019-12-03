<template>
  <div>
    <div slot="header">
      <div v-if="info.type === 0">
        <b>Administrator</b>
      </div>
      <div v-if="info.type === 1">
        <b>Salesperson</b>
      </div>
      <div v-if="info.type === 2">
        <b>Business Customer</b>
      </div>
      <div v-if="info.type === 3">
        <b>Home Customer</b>
      </div>
    </div>

    <!-- common attributes -->

    <div class="infoBody">
      <div>Name</div>
      <div>{{info.name}}</div>
    </div>
    <div class="infoBody">
      <div>ID</div>
      <div>{{info.userId}}</div>
    </div>
    <div class="infoBody">
      <div>address</div>
      <div>{{info.address}}</div>
    </div>
    <div class="infoBody">
      <div>Zip</div>
      <div>{{info.zip}}</div>
    </div>

    <!-- administrator -->

    <div v-if="info.type === 0"></div>

    <!-- salesperson -->

    <div v-if="info.type === 1">
      <div class="infoBody">
        <div>Email</div>
        <div>{{info.email}}</div>
      </div>
      <div class="infoBody">
        <div>Job Title</div>
        <div>{{parsedJobTitle}}</div>
      </div>
    </div>

    <!-- business customer -->

    <div v-if="info.type === 2">
      <div class="infoBody">
        <div>Category</div>
        <div>{{parsedCategory}}</div>
      </div>
      <div class="infoBody">
        <div>Gross</div>
        <div>{{info.gross}}</div>
      </div>
    </div>

    <!-- home customer -->

    <div v-if="info.type === 3">
      <div class="infoBody">
        <div>Marriage</div>
        <div>{{parsedMarriage}}</div>
      </div>
      <div class="infoBody">
        <div>Gender</div>
        <div>{{parsedGender}}</div>
      </div>
      <div class="infoBody">
        <div>Age</div>
        <div>{{parsedAge}}</div>
      </div>
      <div class="infoBody">
        <div>Income</div>
        <div>{{parsedIncome}}</div>
      </div>
    </div>

    <el-button v-if="info != {} && (getCurUser.type === 0 || getCurUser.userId === info.userId)" class="submit" @click="deleteU">Delete User</el-button>
    <el-button
      v-if="getCurUser.type === 0 || getCurUser.userId === info.userId"
      class="submit"
      @click="dialogFormVisible = true"
    >Update User Information</el-button>
    <el-dialog title="User Information" :visible.sync="dialogFormVisible">
      <NewUser :info="info"></NewUser>
    </el-dialog>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import NewUser from "@/components/NewUser";

export default {
  name: "UserInfo",
  components: { NewUser },
  props: {
    info: {
      name: "",
      userId: "",
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
  },
  data() {
    return {
    dialogFormVisible: false
    }
  },
  methods: {
    async deleteU() {
      const r = await this.$api.delete("/api/user?id=" + this.info.userId);
      if (r.data.status == true) {
        alert("Operation succeed!");
        this.info = {};
        console.log(this.info.userId)
      } else {
        alert("Operation failed!\nCannot delete user due to foreign key constrain!");
      }
    },
  },
  computed: {
    ...mapGetters(["getCurUser"]),
    parsedJobTitle: function() {
      if (this.info.jobTitle === 1) {
        return "Salesperson";
      } else if (this.info.jobTitle === 2) {
        return "Manager";
      }
    },
    parsedCategory: function() {
      if ("category" in this.info === false) {
        return "Unknown";
      } else {
        return this.info.category;
      }
    },
    parsedGross: function() {
      if ("gross" in this.info === false) {
        return "Unknwon";
      } else {
        return this.info.gross;
      }
    },
    parsedMarriage: function() {
      if ("marriage" in this.info === false) {
        return "Unknwon";
      } else {
        return this.info.marriage;
      }
    },
    parsedGender: function() {
      if ("gender" in this.info === false) {
        return "Unknown";
      } else if (this.info.gender === 0) {
        return "Male";
      } else if (this.info.gender === 1) {
        return "Female";
      }
    },
    parsedAge: function() {
      if ("age" in this.info === false) {
        return "Unknown";
      } else {
        return this.info.age;
      }
    },
    parsedIncome: function() {
      if ("income" in this.info === false) {
        return "Unknown";
      } else {
        return this.info.income;
      }
    }
  }
};
</script>

<style scoped>
.infoBody {
  display: flex;
  justify-content: space-between;
  padding: 14px 18px;
}

.submit {
  margin-top: 20px;
}
</style>