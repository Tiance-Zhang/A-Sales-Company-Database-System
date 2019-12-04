<template>
  <div>
    <div v-if="getCurUser.type === 0 || getCurUser.type === 1" class="newTransaction">
      <el-button type="text" @click="dialogFormVisible = true">Create a new transaction</el-button>
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
          <el-form-item label="Customer Id" :label-width="formLabelWidth">
            <el-input v-model="form.customerId" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="Store Id" :label-width="formLabelWidth">
            <el-input v-model="form.storeId" autocomplete="off"></el-input>
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
    </div>
    <el-card
      v-if="typeof getCurUser.id === 'undefined'"
      style="text-align: center; margin: 20px auto; width: 400px;"
    >Please login first</el-card>
    <div v-else v-for="t in transactions" v-bind:key="t.orderNumber">
      <Transaction :t="t"></Transaction>
    </div>
  </div>
</template>

<script>
import Transaction from "@/components/Transaction";
import { mapGetters } from "vuex";

export default {
  name: "Transactions",
  components: { Transaction },
  data() {
    return {
      transactions: {},
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
  async mounted() {
    this.$store.dispatch("updateCurrentTabIndex", "3");
    if (this.getCurUser.type === 1) {
      const r = await this.$api.get(
        "/api/transactionsSalesperson?salespersonId=" + this.getCurUser.id
      );
      this.transactions = r.data.data;
    } else if (this.getCurUser.type === 2 || this.getCurUser.type === 3) {
      const r = await this.$api.get(
        "/api/transactionsCustomer?customerId=" + this.getCurUser.id
      );
      this.transactions = r.data.data;
    } else if (this.getCurUser.type === 0) {
      const r = await this.$api.get("/api/transaction");
      this.transactions = r.data.data;
    }
  },
  methods: {
    async submitTansaction() {
      const r = await this.$api.post("/api/transaction", { data: this.form });
      if (r.data.status === true) {
        alert("Update Success!");
      } else {
        alert("Operation failed!");
      }
      this.dialogFormVisible = false;
    }
  },
  computed: {
    ...mapGetters(["getCurUser"])
  }
};
</script>

<style scoped>
.newTransaction {
  text-align: center;
  margin-top: 20px;
}
</style>
