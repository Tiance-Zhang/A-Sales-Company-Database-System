<template>
  <div>
    <div v-if="getCurUser.typeype === 0 || getCurUser.typeype === 1" class="newTransaction">
      <el-button type="text" @click="dialogFormVisible = true">Create a new transaction</el-button>
      <el-dialog title="New transaction" :visible.sync="dialogFormVisible">
        <el-form :model="form">
          <el-form-item label="Customer Id" :label-width="formLabelWidth">
            <el-input v-model="form.customerId" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="Date" :label-width="formLabelWidth">
            <el-input v-model="form.date" autocomplete="off"></el-input>
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
          <el-button type="primary" @click="submitTransaction">Confirm</el-button>
        </span>
      </el-dialog>
    </div>
    <div v-for="t in transactions" v-bind:key="t.orderNumber">
      <Transaction :t="t"></Transaction>
    </div>
  </div>
</template>

<script>
import Transaction from "@/components/Transaction";
import { mapGetters } from "vuex";

var data = [
  {
    orderNumber: 1,
    date: "11-25-2019",
    salespersonName: "Jack",
    productName:
      "2 of Move Free Joint Health Supplement Tablets, (120 count in a bottle), Supports Mobility, Flexibility, Strength, Lubrication and Comfort",
    price: 50000,
    quantity: 1
  },
  {
    orderNumber: 2,
    date: "11-23-2019",
    salespersonName: "Ben",
    productName: "Benz",
    price: 100000,
    quantity: 2
  }
];

export default {
  name: "Transactions",
  components: { Transaction },
  data() {
    return {
      transactions: data,
      dialogFormVisible: false,
      form: {
        customerId: "",
        date: "",
        productName: "",
        price: "",
        quantity: ""
      },
      formLabelWidth: "120px"
    };
  },
  mounted() {
    console.log("mounted");
    this.$store.dispatch("updateCurrentTabIndex", "3");
  },
  methods: {
    submitTransaction() {
      console.log(this.form);
      this.dialogFormVisible = false;
    }
  },
  computed: {
    ...mapGetters(["getCurUser"])
  },
};
</script>

<style scoped>
.newTransaction {
  text-align: center;
  margin-top: 20px;
}
</style>
