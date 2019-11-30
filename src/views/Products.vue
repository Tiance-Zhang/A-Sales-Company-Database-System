<template>
  <div>
    <div class="newProduct">
      <el-button type="text" @click="dialogFormVisible = true">Create a new Product</el-button>
      <el-dialog title="New Product" :visible.sync="dialogFormVisible">
        <el-form :model="form">
          <el-form-item label="Product Name" :label-width="formLabelWidth">
            <el-input v-model="form.productName" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="Product Type" :label-width="formLabelWidth">
            <el-input v-model="form.type" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="Price" :label-width="formLabelWidth">
            <el-input v-model="form.price" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="Inventory" :label-width="formLabelWidth">
            <el-input v-model="form.inventoryAmount" autocomplete="off"></el-input>
          </el-form-item>
        </el-form>
        <span slot="footer" class="dialog-footer">
          <el-button @click="dialogFormVisible = false">Cancel</el-button>
          <el-button type="primary" @click="submitProduct">Confirm</el-button>
        </span>
      </el-dialog>
    </div>
    <div v-for="p in products" v-bind:key="p.productId">
      <Product :p="p"></Product>
    </div>
  </div>
</template>

<script>
import Product from "@/components/Product";
import { mapGetters } from "vuex";


var data = [
  {
    productId: "1234",
    productName: "Dog",
    inventoryAmount: "1",
    price: "500",
    type: "Animal"
  },
  {
    productId: "12",
    productName: "Cat",
    inventoryAmount: "100",
    price: "200",
    type: "SSS"
  }
]

  export default {
    name: "Products",
    components: {Product},
    data() {
      return {
        products: data,
        dialogFormVisible: false,
        form: {
          productId: "",
          productName: "",
          inventoryAmount: "",
          price: "",
          type: ""
        },
        formLabelWidth: "120px"
      };
    },
    methods: {
      submitProduct() {
        console.log(this.form);
        this.dialogFormVisible = false;
      }
    }
  }
</script>

<style scoped>
.newProduct {
  text-align: center;
  margin-top: 20px;
}
</style>
