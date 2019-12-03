<template>
<div class="container">
    <el-card>
        <div class="infoBody">
            <div>mostPopularProduct</div>
            <div>{{data.mostPopularProduct}}</div>
        </div>
        <div class="infoBody">
            <div>mostBuyer</div>
            <div>{{data.mostBuyer}}</div>
        </div>
        <div v-for="(value, key) in data.regions" v-bind:key="key">
            <div class="infoBody">
                <div>{{key}}</div>
                <div>{{value}}</div>
            </div>
        </div>
    </el-card>
</div>
</template>

<script>
var data = {
    mostPopularProduct: "Chicken",
    mostBuyer: "KFC",
    regions: {
        "CA": 123,
        "US": 13
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