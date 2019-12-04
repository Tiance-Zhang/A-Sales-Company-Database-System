<template>
  <el-card class="store-card">
    <div class="first_line">
      <div>No. {{s.id}}</div>
      <div v-if="getCurUser.type === 0">
        <el-button @click="dialogFormVisible = true">Update</el-button>
        <el-button @click="deleteS">Delete</el-button>
      </div>
    </div>
    <div class="second-line">
      <div>Region: {{ s.regionId }}</div>
      <div>Address: {{ s.address }}</div>
      <div>Manager: {{ s.managerId }}</div>
      <div>Number of Salesperson: {{ s.numberOfSalesperson }}</div>
    </div>
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
  </el-card>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "Store",
  computed: {
    ...mapGetters(["getCurUser"])
  },
  props: {
    s: {
      id: "",
      address: "",
      managerId: "",
      numberOfSalesperson: "",
      regionId: ""
    }
  },
  data() {
    return {
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
  mounted() {
    this.form = this.s;
  },
  methods: {
    async submitStore() {
      const r = await this.$api.put("/api/store", { data: this.form });
      if (r.data.status === true) {
        alert("Update Success!");
      } else {
        alert("Operation failed!");
      }
      this.dialogFormVisible = false;
    },
    async deleteS() {
      const r = await this.$api.delete("/api/store?id=" + this.form.id);
      if (r.data.status === true) {
        alert("Operation Success!");
        this.form = {};
      } else {
        alert("Operation failed!");
      }
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
  align-items: center;
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
