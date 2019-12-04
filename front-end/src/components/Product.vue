<template>
  <el-card class="product-card">
    <div class="first_line">
      <div>Product ID: {{p['productId']}}</div>
      <div v-if="getCurUser.type === 0 || getCurUser.type === 1">
        <el-button @click="dialogFormVisible = true">Update</el-button>
        <el-button @click="deleteP">Delete</el-button>
      </div>
    </div>
    <div class="second-line">
      <div>Name: {{p.productName}}</div>
      <div>Type: {{p.type}}</div>
      <div>Inventory: {{p.inventory}}</div>
      <div>Description: {{p.description}}</div>
      <div class="price">${{ p.price }}</div>
    </div>
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
  </el-card>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "Product",
  computed: {
    ...mapGetters(["getCurUser"])
  },
  props: {
    p: {
      productId: "",
      productName: "",
      inventory: "",
      price: "",
      type: "",
      description: ""
    }
  },
  data() {
    return {
      dialogFormVisible: false,
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
  mounted() {
    this.form = this.p;
  },
  methods: {
    async submitProduct() {
      const r = await this.$api.put("/api/product", {data: this.form})
      if (r.data.status === true) {
        alert("Update Success!")
      } else {
        alert("Operation failed!")
      }
      this.dialogFormVisible = false;
    },
    async deleteP() {
      const r = await this.$api.delete("/api/product?productId=" + this.form.productId);
      if (r.data.status === true) {
        alert("Operation Success!")
        this.form = {}
      } else {
        alert("Operation failed!")
      }
    }
  }
};
</script>
<style scoped>
.product-card {
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

.price {
  color: #b12704;
  text-align: right;
}
</style>
<style>
.product-card > .el-card__body {
  padding: 0;
}
</style>
