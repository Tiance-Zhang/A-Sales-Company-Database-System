<template>
<div class="container">
    <el-card>
        <div class="infoBody">
            <div>Total Sales</div>
            <div>${{data.totalSales}}</div>
        </div>
        <div class="infoBody">
            <div>Customer Buys Most</div>
            <div>{{data.mostBuyer}}</div>
        </div>
        <div class="infoBody">
            <div>{{data.mostBuyer}} spent</div>
            <div>${{data.mostBuyerSpent}}</div>
        </div>
        <div class="infoBody">
            <div>Most Popular Product</div>
            <div>{{data.mostPopularProduct}}</div>
        </div>
        <div class="infoBody">
            <div>{{data.mostPopularProduct}} sold</div>
            <div>${{data.mostPopularProductSales}}</div>
        </div>
        <div class="infoBody">
            <div>Most Popular Store</div>
            <div>Store {{data.mostPopularStore}}</div>
        </div>
        <div class="infoBody">
            <div>Store {{data.mostPopularStore}} transaction</div>
            <div>{{data.mostPopularStoreCount}}</div>
        </div>
    </el-card>
</div>
</template>

<script>
export default {
  name: "Statistics",
  data() {
      return {
          data: {}
      }
  },
  async mounted() {
    this.$store.dispatch("updateCurrentTabIndex", "5");
    const r = await this.$api.get("/api/statistics")
    this.data = r.data
  }
};
</script>

<style scoped>
.container {
  margin: 20px auto;
  text-align: center;
  width: 600px;
}

.infoBody {
  display: flex;
  justify-content: space-between;
  padding: 14px 18px;
}
</style>