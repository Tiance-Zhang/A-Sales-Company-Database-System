<template>
  <div class="container">
    <el-radio-group v-model="pageType" class="pageType">
      <el-radio :label="false" border>Search existing customer</el-radio>
      <el-radio :label="true" border>Add a new customer</el-radio>
    </el-radio-group>
    <el-card v-if="pageType" class="newCustomer">
      <el-form label-width="80px" :model="form" :rules="rules" ref="form">
        <el-form-item label="Name" :label-width="formLabelWidth" prop="name">
          <el-input v-model="form.name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="Street" :label-width="formLabelWidth" prop="street">
          <el-input v-model="form.street" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="City" :label-width="formLabelWidth" prop="city">
          <el-input v-model="form.city" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="State" :label-width="formLabelWidth" prop="state">
          <el-input v-model="form.state" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="Type" :label-width="formLabelWidth" prop="type">
          <el-radio-group v-model="form.kind">
            <el-radio :label="1" border>Business Customer</el-radio>
            <el-radio :label="2" border>Home Customer</el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="Category" v-if="form.kind===1" :label-width="formLabelWidth">
          <el-input v-model="form.category"></el-input>
        </el-form-item>
        <el-form-item label="Gross" v-if="form.kind===1" :label-width="formLabelWidth">
          <el-input v-model="form.gross"></el-input>
        </el-form-item>
        <el-form-item label="Marriage" v-if="form.kind===2" :label-width="formLabelWidth">
          <el-select v-model="form.marriage" placeholder="Select">
            <el-option
              v-for="item in marriageOptions"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            ></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="Gender" v-if="form.kind===2" :label-width="formLabelWidth">
          <el-select v-model="form.gender" placeholder="Select">
            <el-option
              v-for="item in genderOptions"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            ></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="Age" v-if="form.kind===2" :label-width="formLabelWidth">
          <el-input v-model="form.age"></el-input>
        </el-form-item>
        <el-form-item label="Income" v-if="form.kind===2" :label-width="formLabelWidth">
          <el-input v-model="form.income"></el-input>
        </el-form-item>
      </el-form>
      <el-button @click="submitNewCustomer">Confirm</el-button>
    </el-card>
    <el-card v-if="!pageType" class="searchCustomer">
      <el-input v-model="customerId" placeholder="Enter customer ID"></el-input>
      <el-button class="submit" @click="submitCustomerSearch">Search</el-button>
    </el-card>
    <el-card v-if="showCustomerInfo && !pageType" class="customerInfo">
      <div slot="header">
        <div v-if="info.kind === 1">
          <b>Business Customer</b>
        </div>
        <div v-if="info.kind === 2">
          <b>Home Customer</b>
        </div>
      </div>
      <div class="infoBody">
        <div>Name</div>
        <div>{{info.name}}</div>
      </div>
      <div class="infoBody">
        <div>Customer ID</div>
        <div>{{info.customerId}}</div>
      </div>
      <div class="infoBody">
        <div>Street</div>
        <div>{{info.street}}</div>
      </div>
      <div class="infoBody">
        <div>City</div>
        <div>{{info.city}}</div>
      </div>
      <div class="infoBody">
        <div>State</div>
        <div>{{info.state}}</div>
      </div>
      <div class="infoBody">
        <div>Zip</div>
        <div>{{info.zip}}</div>
      </div>
      <div v-if="info.kind === 1">
        <div class="infoBody">
          <div>Category</div>
          <div>{{parsedCategory}}</div>
        </div>
        <div class="infoBody">
          <div>Gross</div>
          <div>{{info.gross}}</div>
        </div>
      </div>
      <div v-if="info.kind === 2">
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
    </el-card>
  </div>
</template>

<script>
var data = {
  customerId: 12345,
  name: "KFC",
  street: "1234 1th Ave",
  city: "Pitt",
  state: "P.A.",
  zip: "12345",
  kind: 1,
  category: "food",
  gross: 12345
};

export default {
  name: "Customers",
  data() {
    return {
      formLabelWidth: "120px",
      pageType: false,
      showCustomerInfo: true,
      info: data,
      customerId: "",
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
    this.$store.dispatch("updateCurrentTabIndex", "6");
  },
  methods: {
    submitCustomerSearch() {
      console.log(this.customerId);
    },
    submitNewCustomer() {
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
  },
  computed: {
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
      if (this.info.marriage === 1) {
        return "Single";
      } else if (this.info.marriage === 2) {
        return "Married";
      } else if (this.info.marriage === 3) {
        return "Unknown";
      }
    },
    parsedGender: function() {
      if ("gender" in this.info === false) {
        return "Unknown";
      } else if (this.info.gender === 1) {
        return "Male";
      } else if (this.info.gender === 2) {
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
.container {
  margin: 20px auto;
  text-align: center;
  width: 600px;
}

.searchCustomer,
.newCustomer,
.customerInfo {
  margin: 20px auto;
}

.newCustomer {
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
