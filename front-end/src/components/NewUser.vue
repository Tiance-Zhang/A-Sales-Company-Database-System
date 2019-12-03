<template>
  <div>
    <el-form label-width="80px" :model="info" :rules="rules" ref="infoForm">
      <el-form-item label="User ID" :label-width="formLabelWidth" prop="userId">
        <el-input v-model="info.userId" autocomplete="off" placeholder="Numbers Only"></el-input>
      </el-form-item>
      <el-form-item label="Name" :label-width="formLabelWidth" prop="name">
        <el-input v-model="info.name" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="Address" :label-width="formLabelWidth" prop="address">
        <el-input v-model="info.address" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="Zip" :label-width="formLabelWidth" prop="zip">
        <el-input v-model="info.zip" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item
        v-if="getCurUser.userId === '' || getCurUser.type === 0"
        label="Type"
        :label-width="formLabelWidth"
      >
        <el-radio-group v-model="info.type">
          <el-radio :label="0" border>Administrator</el-radio>
          <el-radio :label="1" border>Salesperson</el-radio>
          <el-radio :label="2" border>Business Customer</el-radio>
          <el-radio :label="3" border>Home Customer</el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item label="Email" v-if="info.type===1" :label-width="formLabelWidth">
        <el-input v-model="info.email"></el-input>
      </el-form-item>
      <el-form-item label="Category" v-if="info.type===2" :label-width="formLabelWidth">
        <el-input v-model="info.category"></el-input>
      </el-form-item>
      <el-form-item label="Gross" v-if="info.type===2" :label-width="formLabelWidth">
        <el-input v-model="info.gross"></el-input>
      </el-form-item>
      <el-form-item label="Marriage" v-if="info.type===3" :label-width="formLabelWidth">
        <el-input v-model="info.Marriage"></el-input>
      </el-form-item>
      <el-form-item label="Gender" v-if="info.type===3" :label-width="formLabelWidth">
        <el-select v-model="info.gender" placeholder="Select">
          <el-option
            v-for="item in genderOptions"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          ></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="Age" v-if="info.type===3" :label-width="formLabelWidth">
        <el-input v-model="info.age"></el-input>
      </el-form-item>
      <el-form-item label="Income" v-if="info.type===3" :label-width="formLabelWidth">
        <el-input v-model="info.income"></el-input>
      </el-form-item>
    </el-form>
    <el-button @click="submitNewUser">Confirm</el-button>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "NewUser",
  props: {
    info: {
      name: "",
      id: "",
      userId: "",
      type: "",
      address: "",
      zip: "",
      email: "",
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
      formLabelWidth: "120px",
      genderOptions: [
        {
          value: 1,
          label: "Male"
        },
        {
          value: 0,
          label: "Female"
        }
      ],
      rules: {
        userId: [{ required: true, message: "Required", trigger: "blur" }],
        name: [{ required: true, message: "Required", trigger: "blur" }],
        address: [{ required: true, message: "Required", trigger: "blur" }],
        zip: [{ required: true, message: "Required", trigger: "blur" }]
      },
      postdata: this.info
    };
  },
  mounted() {
    this.info.id = this.getCurUser.userId;
    this.info.type = this.getCurUser.type;
  },
  computed: {
    ...mapGetters(["getCurUser"])
  },
  methods: {
    async submitNewUser() {
      this.$refs["infoForm"].validate(async valid => {
        if (valid) {
          if (this.getCurUser.userId === "" || this.getCurUser.type === 0) {
            this.info.id = this.info.userId
            const r = await this.$api.post("/api/user", this.postdata);
          } else {
            const r = await this.$api.put("/api/user", this.info);
          }
          if (this.info.status == true) {
            alert("Operation Succeed!");
          } else {
            alert("Operation Failed!");
          }
        } else {
          console.log("error submit!!");
          return false;
        }
      });
    }
  }
};
</script>

<style scoped>
.el-select {
  width: 100%;
}
.el-radio{
  width: 50%;
  margin: 0px;
}

.el-radio.is-bordered+.el-radio.is-bordered {
  margin-left: 0px;
}
</style>