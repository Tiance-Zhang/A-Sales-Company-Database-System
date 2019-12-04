<template>
<div class="container">
    <el-card>
        <div class="infoBody">
            <div>Most Popular Product</div>
            <div>{{data.mostPopularProduct}}</div>
        </div>
        <div class="infoBody">
            <div>Business Customer Buys Most</div>
            <div>Mia</div>
        </div>
        <div class="infoBody">
            <div>Home Customer Buys Most</div>
            <div>Ivan</div>
        </div>
        <div class="infoBody">
            <div>Total Sales</div>
            <div>33,331</div>
        </div>
        <div v-for="(value, key) in data.regions" v-bind:key="key">
            <div class="infoBody">
                <div>Store {{key}}</div>
                <div>{{value}}</div>
            </div>
        </div>
    </el-card>
</div>
</template>

<script>
var data = {
    mostPopularProduct: "458 spider",
    mostBuyer: "KFC",
    regions: {
        "1": 1,
        "2": 3
    }
}


export default {
  name: "Statistics",
  data() {
      return {
          data: data
      }
  },
  mounted() {
    this.$store.dispatch("updateCurrentTabIndex", "5");
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