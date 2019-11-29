<template>
  <div id="app">
    <Header></Header>
    <router-view></router-view>
  </div>
</template>

<style>
  body {
    width: 800px;
    margin: 0 auto;
    font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "微软雅黑", Arial, sans-serif;

  }

  a {
    text-decoration: none;
  }

  .nav-link {
    display: block;
    height: 100%;
    padding: 0 20px;
  }

</style>
<script>
  import Header from "@/components/Header";

  export default {
    components: {Header}
  }
</script>
