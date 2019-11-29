<template>
  <div id="account">
    <div class="basicInfoContainer">
      <span>Name </span>
      <span class="spanTwoItem">{{ info.name }}</span>
      <span>Customer ID </span>
      <span class="spanTwoItem">{{ info.customerID }}</span>
      <span>Customer Type </span>
      <span class="spanTwoItem" v-if="info.kind === 1">Bussiness Customer</span>
      <span class="spanTwoItem" v-if="info.kind === 2">Home Customer</span>
      <span>Address </span>
      <span class="spanTwoItem">{{ info.street }}, {{ info.city }}, {{ info.state }}, {{ info.zip }}</span>
    </div>
    <div v-if="info.kind === 1" class="businessInfoContainer">
      <span>Category </span>
      <span class="spanTwoItem">{{ parsedCategory }}</span>
      <span>Gross </span>
      <span class="spanTwoItem">{{ parsedGross }}</span>
    </div>

    <div v-if="info.kind === 2" class="homeInfoContainer">
      <span>Marriage</span>
      <span class="spanTwoItem">{{ parsedMarriage }}</span>
      <span>Gender</span>
      <span class="spanTwoItem">{{ parsedGender }}</span>
      <span>Age</span>
      <span class="spanTwoItem">{{ parsedAge }}</span>
      <span>Income</span>
      <span class="spanTwoItem">{{ parsedIncome }}</span>
    </div>

  </div>
</template>

<script>
  import {mapMutations} from "vuex";

  var data1 = {
    "customerID": 12345,
    "name": "KFC",
    "street": "1234 1th Ave",
    "city": "Pitt",
    "state": "P.A",
    "zip": "12345",
    "kind": 1,
    "category": "food",
    "gross": 12345
  }

  export default {
    name: "Account",
    data() {
      return {
        info: data1,
      }
    },
    mounted() {
      this.$store.dispatch("updateCurrentTabIndex", "4")
    },
    computed: {
      parsedCategory: function () {
        if ("category" in this.info === false) {
          return "Unknown";
        } else {
          return this.info.category;
        }
      },
      parsedGross: function () {
        if ("gross" in this.info === false) {
          return "Unknwon";
        } else {
          return this.info.gross;
        }
      },
      parsedMarriage: function () {
        if (this.info.marriage === 1) {
          return "Single";
        } else if (this.info.marriage === 2) {
          return "Married";
        } else if (this.info.marriage === 3) {
          return "Unknown";
        }
      },
      parsedGender: function () {
        if ("gender" in this.info === false) {
          return "Unknown";
        } else if (this.info.gender === 1) {
          return "Male";
        } else if (this.info.gender === 2) {
          return "Female";
        }
      },
      parsedAge: function () {
        if ("age" in this.info === false) {
          return "Unknown";
        } else {
          return this.info.age;
        }
      },
      parsedIncome: function () {
        if ("income" in this.info === false) {
          return "Unknown";
        } else {
          return this.info.income;
        }
      }
    }

  }
</script>

<style scoped>
  .basicInfoContainer, .businessInfoContainer, .homeInfoContainer {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
  }

  .basicInfoContainer {
    padding: 20px 0 0 0;
    grid-template-rows: repeat(4, 30px);
  }

  .businessInfoContainer {
    grid-template-rows: repeat(2, 30px);
  }

  .homeInfoContainer {
    grid-template-rows: repeat(4, 30px);
  }

  .spanTwoItem {
    grid-column-start: span 2;
    justify-self: end;
  }
</style>
