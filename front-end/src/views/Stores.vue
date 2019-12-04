<template>
  <div>
    <div v-if="getCurUser.type === 0" class="newStore">
      <el-button type="text" @click="dialogFormVisible = true">Create a new store</el-button>
      <el-dialog title="New Store" :visible.sync="dialogFormVisible">
        <el-form :model="form">
          <el-form-item label="Store Id" :label-width="formLabelWidth">
            <el-input v-model="form.id" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="Address" :label-width="formLabelWidth">
            <el-input v-model="form.address" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="Region Id" :label-width="formLabelWidth">
            <el-input v-model="form.regionId" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="Manager Id" :label-width="formLabelWidth">
            <el-input v-model="form.managerId" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="Number of Salesperson" :label-width="formLabelWidth">
            <el-input v-model="form.numberOfSalesperson" autocomplete="off"></el-input>
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

export default {
  name: "Stores",
  components: { Store },
  data() {
    return {
      stores: {},
      dialogFormVisible: false,
      form: {
        id: "",
        address: "",
        managerId: "",
        numberOfSalesperson: "",
        regionId: ""
      },
      formLabelWidth: "120px"
    };
  },
  async mounted() {
    this.$store.dispatch("updateCurrentTabIndex", "2");
    const r = await this.$api.get("/api/stores");
    this.stores = r.data.data;
  },
  methods: {
    async submitStore() {
      const r = await this.$api.post("/api/store", { data: this.form });
      if (r.data.status === true) {
        const r2 = await this.$api.get("/api/stores");
        this.stores = r2.data.data;
        this.dialogFormVisible = false;
        alert("Update Success!");
      } else {
        alert("Operation failed!");
      }
      this.dialogFormVisible = false;
    }
  },
  computed: {
    ...mapGetters(["getCurUser"])
  }
};
</script>

<style scoped>
.newStore {
  text-align: center;
  margin-top: 20px;
}
</style>
