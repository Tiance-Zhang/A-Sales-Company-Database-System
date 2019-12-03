<template>
  <el-card class="product-card">
    <div class="first_line">
      <div>Product ID: {{p['product Id']}}</div>
      <div v-if="getCurUser.type === 0 || getCurUser.type === 1">
        <el-button @click="updateP">Update</el-button>
        <el-button @click="deleteP">Delete</el-button>
      </div>
    </div>
    <div class="second-line">
      <div>Name: {{p.productname}}</div>

      <div>Type: {{p.type}}</div>
      <div>Inventory: {{p.inventory}}</div>
      <div>Description: {{p.description}}</div>
      <div class="price">${{ p.price }}</div>
    </div>
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
      "product Id": "",
      productname: "",
      price: "",
      type: "",
      inventory: "",
      description: ""
    }
  },
  methods: {
    updateP() {

    },
    deleteP() {
      console.log(this.t);
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
