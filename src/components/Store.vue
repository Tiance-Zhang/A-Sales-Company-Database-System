<template>
  <el-card class="store-card">
    <div class="first_line">
      <div>No. {{s.storeId}}</div>
    </div>
    <div class="second-line">
      <div>Region: {{ s.region }}</div>
      <div>Address: {{ s.address }}</div>
      <div>Manager: {{ s.manager }}</div>
      <div>Number of Salesperson: {{ s.numOfSalesperson }}</div>
    </div>
  </el-card>
</template>

<script>
export default {
  name: "Store",
  props: {
    s: {
      storeId: "",
      address: "",
      manager: "",
      numOfSalesperson: "",
      region: ""
    }
  }
};
</script>
<style scoped>
.store-card {
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
</style>
<style>
.store-card > .el-card__body {
  padding: 0;
}
</style>
