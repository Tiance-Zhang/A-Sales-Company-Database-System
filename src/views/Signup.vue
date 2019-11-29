<template>
  <el-card class="input">
    <el-form label-width="80px" :model="form" :rules="rules" ref="form">
      <el-form-item label="Name" prop="name">
        <el-input v-model="form.name"></el-input>
      </el-form-item>
      <el-form-item label="Street" prop="street">
        <el-input v-model="form.street"></el-input>
      </el-form-item>
      <el-form-item label="City" prop="city">
        <el-input v-model="form.city"></el-input>
      </el-form-item>
      <el-form-item label="State" prop="state">
        <el-input v-model="form.state"></el-input>
      </el-form-item>
      <el-form-item label="Zip" prop="zipcode">
        <el-input v-model="form.zipcode"></el-input>
      </el-form-item>
      <el-form-item label="Type" prop="type">
        <el-radio-group v-model="form.kind">
          <el-radio :label="1" border>Business Customer</el-radio>
          <el-radio :label="2" border>Home Customer</el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item label="Category" v-if="form.kind===1">
        <el-input v-model="form.category"></el-input>
      </el-form-item>
      <el-form-item label="Gross" v-if="form.kind===1">
        <el-input v-model="form.gross"></el-input>
      </el-form-item>
      <el-form-item label="Marriage" v-if="form.kind===2">
        <el-select v-model="form.marriage" placeholder="Select">
          <el-option
            v-for="item in marriageOptions"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          ></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="Gender" v-if="form.kind===2">
        <el-select v-model="form.gender" placeholder="Select">
          <el-option
            v-for="item in genderOptions"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          ></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="Age" v-if="form.kind===2">
        <el-input v-model="form.age"></el-input>
      </el-form-item>
      <el-form-item label="Income" v-if="form.kind===2">
        <el-input v-model="form.income"></el-input>
      </el-form-item>
    </el-form>

    <el-button class="submit" @click="submitSignup">Submit</el-button>
  </el-card>
</template>

<script>
export default {
  name: "Signup",
  data() {
    return {
      form: {
        name: "",
        street: "",
        city: "",
        state: "",
        zipcode: "",
        kind: 1,
        category: "",
        gross: "",
        marriage: "",
        gender: "",
        age: "",
        income: ""
      },
      marriageOptions: [
        {
          value: 1,
          label: "Married"
        },
        {
          value: 0,
          label: "Single"
        }
      ],
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
        name: [{ required: true, message: "Required", trigger: "blur" }],
        street: [{ required: true, message: "Required", trigger: "blur" }],
        city: [{ required: true, message: "Required", trigger: "blur" }],
        state: [{ required: true, message: "Required", trigger: "blur" }],
        zipcode: [{ required: true, message: "Required", trigger: "blur" }]
      }
    };
  },
  mounted() {
    this.$store.dispatch("updateCurrentTabIndex", "5");
  },
  methods: {
    submitSignup(formName) {
      this.$refs["form"].validate(valid => {
        if (valid) {
          alert("submit!");
        } else {
          console.log("error submit!!");
          return false;
        }
      });
      console.log(this.form);
    }
  }
};
</script>

<style scoped>
.input {
  text-align: center;
  width: 600px;
  margin: 50px auto;
  padding: 50px;
}

.submit {
  margin-top: 20px;
}

.el-select {
  width: 100%;
}
</style>
