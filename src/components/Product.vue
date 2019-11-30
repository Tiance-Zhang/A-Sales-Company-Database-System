<template>
  <el-card class="product-card">
    <div class="first_line">Product ID: {{p.productId}}</div>
    <div class="second-line">
      <div>{{p.productName}}</div>

      <div>Type: {{p.type}}</div>
      <div>Inventory Amount: {{p.inventoryAmount}}</div>
      <div class="price">${{ p.price }}</div>
    </div>
  </el-card>
</template>

<script>
export default {
  name: "Product",
  props: {
    p: {
      productId: "",
      productName: "",
      price: "",
      type: "",
      inventoryAmount: ""
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
