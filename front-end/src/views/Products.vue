<template>
  <div class="container">
    <div v-if="getCurUser.type === 0" class="newProduct">
      <el-button type="text" @click="dialogFormVisible = true">Create a new Product</el-button>
      <el-dialog title="New Product" :visible.sync="dialogFormVisible">
        <el-form :model="form">
          <el-form-item label="Product Id" :label-width="formLabelWidth">
            <el-input v-model="form.productId" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="Product Name" :label-width="formLabelWidth">
            <el-input v-model="form.productName" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="Product Type" :label-width="formLabelWidth">
            <el-select v-model="form.type" placeholder="Select">
              <el-option
                v-for="item in typeOptions"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              ></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="Price" :label-width="formLabelWidth">
            <el-input v-model="form.price" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="Inventory" :label-width="formLabelWidth">
            <el-input v-model="form.inventory" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="Description" :label-width="formLabelWidth">
            <el-input v-model="form.description" autocomplete="off"></el-input>
          </el-form-item>
        </el-form>
        <span slot="footer" class="dialog-footer">
          <el-button @click="dialogFormVisible = false">Cancel</el-button>
          <el-button type="primary" @click="submitProduct">Confirm</el-button>
        </span>
      </el-dialog>
    </div>
    <el-card class="searchProduct">
      <el-input v-model="keyword" placeholder="Keyword"></el-input>
      <el-button class="submit" @click="submitSearch">Search</el-button>
    </el-card>
    <div v-for="p in products" v-bind:key="p.productId">
      <Product :p="p"></Product>
    </div>
  </div>
</template>

<script>
import Product from "@/components/Product";
import { mapGetters } from "vuex";

export default {
  name: "Products",
  components: { Product },
  data() {
    return {
      products: "",
      dialogFormVisible: false,
      keyword: "",
      form: {
        productId: "",
        productName: "",
        inventory: "",
        price: "",
        type: "",
        description: ""
      },
      typeOptions: [
        {
          value: 1,
          label: "sedan"
        },
        {
          value: 2,
          label: "SUV"
        },
        {
          value: 3,
          label: "coupe"
        },
        {
          value: 4,
          label: "truck"
        }
      ],
      formLabelWidth: "120px"
    };
  },
  async mounted() {
    const r = await this.$api.get("/api/products");
    if (r.data.status === true) {
      this.products = r.data.data;
    } else {
      alert("Operation failed!");
    }
  },
  methods: {
    async submitProduct() {
      const r = await this.$api.post("/api/product", { data: this.form });
      if (r.data.status === true) {
        const r2 = await this.$api.get("/api/products");
        this.products = r2.data.data;
      } else {
        alert("Operation failed!");
      }
      this.dialogFormVisible = false;
    },
    async submitSearch() {
      const r = await this.$api.get("/api/product?productName=" + this.keyword);
      if (r.data.status === true) {
        this.products = r.data.data;
      } else {
        alert("No result");
      }
    }
  },
  computed: {
    ...mapGetters(["getCurUser"])
  }
};
</script>

<style scoped>
.container {
  margin: 20px auto;
  width: 800px;
}

.newProduct {
  text-align: center;
  margin-top: 20px;
}

.searchProduct {
  margin: 20px auto;
  text-align: center;
}

.submit {
  margin-top: 20px;
}

.el-select {
  width: 100%;
}
</style>
