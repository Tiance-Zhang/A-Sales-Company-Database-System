<template>
  <div>
    <div class="newStore">
      <el-button type="text" @click="dialogFormVisible = true">Create a new store</el-button>
      <el-dialog title="New Store" :visible.sync="dialogFormVisible">
        <el-form :model="form">
          <el-form-item label="Street" :label-width="formLabelWidth" prop="street">
            <el-input v-model="form.street"></el-input>
          </el-form-item>
          <el-form-item label="City" :label-width="formLabelWidth" prop="city">
            <el-input v-model="form.city"></el-input>
          </el-form-item>
          <el-form-item label="State" :label-width="formLabelWidth" prop="state">
            <el-input v-model="form.state"></el-input>
          </el-form-item>
          <el-form-item label="Zip" :label-width="formLabelWidth" prop="zipcode">
            <el-input v-model="form.zipcode"></el-input>
          </el-form-item>
          <el-form-item label="Manager" :label-width="formLabelWidth" prop="manager">
            <el-input v-model="form.manager"></el-input>
          </el-form-item>
          <el-form-item label="Zip" :label-width="formLabelWidth" prop="zipcode">
            <el-input v-model="form.zipcode"></el-input>
          </el-form-item>
        </el-form>
        <span slot="footer" class="dialog-footer">
          <el-button @click="dialogFormVisible = false">Cancel</el-button>
          <el-button type="primary" @click="submitStore">Confirm</el-button>
        </span>
      </el-dialog>
    </div>
    <div v-for="s in stores" v-bind:key="s.storeId">
      <Store :s="s"></Store>
    </div>
  </div>
</template>

<script>
import Store from "@/components/Store";
import { mapGetters } from "vuex";

var data = [
  {
    storeId: 123,
    address: "test street P.A.",
    manager: "Dam",
    numOfSalesperson: 256,
    region: "US"
  },
  {
    storeId: 12,
    address: "222test street P.A.",
    manager: "Dam111",
    numOfSalesperson: 16,
    region: "CA"
  }
];

export default {
  name: "Stores",
  components: { Store },
  data() {
    return {
      stores: data,
      dialogFormVisible: false,
      form: {
        storeId: "",
        address: "",
        manager: "",
        numOfSalesperson: "",
        region: ""
      },
      formLabelWidth: "120px"
    }
  },
  mounted() {
    this.$store.dispatch("updateCurrentTabIndex", "2");
  },
  methods: {
    submitStore() {
      console.log(this.form);
      this.dialogFormVisible = false;
    }
  }
};
</script>

<style scoped>
.newStore {
  text-align: center;
  margin-top: 20px;
}
</style>
