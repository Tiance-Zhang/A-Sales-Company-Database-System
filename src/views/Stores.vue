<template>
  <div> Something about stores</div>
</template>

<script>
  export default {
    name: "Stores",
    mounted() {
      this.$store.dispatch("updateCurrentTabIndex", "2")
    }
  }
</script>

<style scoped>

</style>
