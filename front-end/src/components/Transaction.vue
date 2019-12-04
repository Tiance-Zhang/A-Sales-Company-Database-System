<template>
  <el-card class="trans-card">
    <div class="first_line">
      <div>{{t.date}}</div>
      <div>Order #{{t.id}}</div>
      <div v-if="getCurUser.type === 0 || getCurUser.type === 1">
        <el-button @click="dialogFormVisible = true">Update</el-button>
        <el-button v-if="getCurUser.type === 0" @click="deleteT">Delete</el-button>
      </div>
    </div>
    <div class="second-line">
      <div>Buyer: {{ t.customerName }}</div>
      <div>{{t.productName}}</div>
      <div class="soldby">Sold by {{t.salespersonName}} At Store {{t.storeId}}</div>
      <div class="price_quantity">
        <div class="price">${{ t.price }}</div>
        <div>x {{t.quantity}}</div>
      </div>
      <div class="total">${{t.price * t.quantity}}</div>
    </div>
    <el-dialog title="New Tansaction" :visible.sync="dialogFormVisible">
      <el-form :model="form">
        <el-form-item label="Tansaction Id" :label-width="formLabelWidth">
          <el-input v-model="form.id" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="Date" :label-width="formLabelWidth">
          <el-input v-model="form.date" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="Salesperson Id" :label-width="formLabelWidth">
          <el-input v-model="form.salespersonId" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="Store Id" :label-width="formLabelWidth">
          <el-input v-model="form.storeId" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="Customer Id" :label-width="formLabelWidth">
          <el-input v-model="form.customerId" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="Product Name" :label-width="formLabelWidth">
          <el-input v-model="form.productName" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="Price" :label-width="formLabelWidth">
          <el-input v-model="form.price" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="Quantity" :label-width="formLabelWidth">
          <el-input v-model="form.quantity" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">Cancel</el-button>
        <el-button type="primary" @click="submitTansaction">Confirm</el-button>
      </span>
    </el-dialog>
  </el-card>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "Transaction",
  props: {
    t: {
      id: "",
      date: "",
      salespersonId: "",
      salespersonName: "",
      storeId: "",
      customerId: "",
      customerName: "",
      productName: "",
      price: "",
      quantity: ""
    }
  },
  data() {
    return {
      dialogFormVisible: false,
      form: {
        id: "",
        date: "",
        salespersonId: "",
        storeId: "",
        customerId: "",
        productName: "",
        price: "",
        quantity: ""
      },
      formLabelWidth: "120px"
    };
  },
  mounted() {
    this.form = this.t
  },
  computed: {
    ...mapGetters(["getCurUser"])
  },
  methods: {
    async submitTansaction() {
      const r = await this.$api.put("/api/transaction", { data: this.form });
      if (r.data.status === true) {
        alert("Update Success!");
      } else {
        alert("Operation failed!");
      }
      this.dialogFormVisible = false;
    },
    async deleteT() {
      const r = await this.$api.delete("/api/transaction?id=" + this.form.id);
      if (r.data.status === true) {
        alert("Operation Success!");
        this.form = {};
      } else {
        alert("Operation failed!");
      }
    }
  }
};
</script>
<style scoped>
.trans-card {
  margin-top: 20px;
}
.first_line {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #f6f6f6;
  padding: 14px 18px;
}

.second-line {
  padding: 14px 18px;
  line-height: 25px;
}

.soldby {
  color: #555;
}

.price {
  color: #b12704;
}

.price_quantity {
  display: flex;
  justify-content: space-between;
}

.total {
  text-align: end;
  border-top: 2px solid #dddddd;
}
</style>
<style>
.trans-card > .el-card__body {
  padding: 0;
}
</style>
