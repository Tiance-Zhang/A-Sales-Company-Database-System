<template>
  <el-card class="trans-card">
    <div class="first_line">
      <div>{{t.date}}</div>
      <div>Order #{{t.orderNumber}}</div>
    </div>
    <div class="second-line">
      <div>{{ t.productName }}</div>

      <div class="soldby">Sold by: {{t.salespersonName}}</div>
      <div class="price_quantity">
        <div class="price">${{ t.price }}</div>
        <div>x {{t.quantity}}</div>
      </div>
      <div class="total">${{ t.price * t.quantity }}</div>
    </div>

  </el-card>
</template>

<script>
  export default {
    name: "Transaction",
    props: {
      t: {
        orderNumber: "",
        date: "",
        salespersonName: "",
        productName: "",
        price: "",
        quantity: ""
      }
    }
  }
</script>
<style scoped>
  .trans-card{
    margin-top: 20px;
  }
  .first_line {
    display: flex;
    justify-content: space-between;
    background: #f6f6f6;
    padding: 14px 18px
  }

  .second-line {
    padding: 14px 18px;
    line-height: 25px;

  }

  .soldby {
    color: #555;
  }

  .price {
    color: #B12704;
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
